package translib

import (
	"errors"
	log "github.com/golang/glog"
	"reflect"
	"strconv"
	"strings"
	"translib/db"
	"translib/ocbinds"
	"translib/tlerr"
)

type intfModeType int

const (
	MODE_UNSET intfModeType = iota
	ACCESS
	TRUNK
)

type intfMode struct {
	ifName string
	mode   intfModeType
}

/******* CONFIG FUNCTIONS ********/

func (app *IntfApp) translateCommonPhyIntfSubInterfaces(d *db.DB, ifKey *string, intf *ocbinds.OpenconfigInterfaces_Interfaces_Interface) error {
	var err error
	if intf.Subinterfaces == nil {
		return err
	}
	subIf := intf.Subinterfaces.Subinterface[0]
	if subIf != nil {
		if subIf.Ipv4 != nil && subIf.Ipv4.Addresses != nil {
			for ip, _ := range subIf.Ipv4.Addresses.Address {
				addr := subIf.Ipv4.Addresses.Address[ip]
				if addr.Config != nil {
					log.Info("Ip:=", *addr.Config.Ip)
					log.Info("prefix:=", *addr.Config.PrefixLength)
					if !validIPv4(*addr.Config.Ip) {
						errStr := "Invalid IPv4 address " + *addr.Config.Ip
						err = tlerr.InvalidArgsError{Format: errStr}
						return err
					}
					err = app.translateIpv4(d, *ifKey, *addr.Config.Ip, int(*addr.Config.PrefixLength))
					if err != nil {
						return err
					}
				}
			}
		}
		if subIf.Ipv6 != nil && subIf.Ipv6.Addresses != nil {
			for ip, _ := range subIf.Ipv6.Addresses.Address {
				addr := subIf.Ipv6.Addresses.Address[ip]
				if addr.Config != nil {
					log.Info("Ip:=", *addr.Config.Ip)
					log.Info("prefix:=", *addr.Config.PrefixLength)
					if !validIPv6(*addr.Config.Ip) {
						errStr := "Invalid IPv6 address " + *addr.Config.Ip
						err = tlerr.InvalidArgsError{Format: errStr}
						return err
					}
					err = app.translateIpv4(d, *ifKey, *addr.Config.Ip, int(*addr.Config.PrefixLength))
					if err != nil {
						return err
					}
				}
			}
		}
	} else {
		err = errors.New("Only subinterface index 0 is supported")
		return err
	}
	return err
}

func (app *IntfApp) translateCommonPhyIntfEthernet(d *db.DB, ifKey *string, intf *ocbinds.OpenconfigInterfaces_Interfaces_Interface) error {
	var err error

	if intf.Ethernet == nil {
		return err
	}
	if intf.Ethernet.SwitchedVlan == nil {
		return err
	}

	switchedVlanIntf := intf.Ethernet.SwitchedVlan
	if switchedVlanIntf.Config == nil {
		return err
	}

	log.Info("Entering Switched vlan interface Config")
	if !app.validateIpExistsForInterface(d, ifKey) {
		errStr := "Interface: " + *ifKey + ", IP address cannot exist with L2 modes"
		err = tlerr.InvalidArgsError{Format: errStr}
		return err
	}

	var accessVlanId uint16 = 0
	var trunkVlanSlice []string
	accessVlanFound := false
	trunkVlanFound := false

	/* check whether access VLAN info is present! */
	if switchedVlanIntf.Config.AccessVlan != nil {
		accessVlanId = *switchedVlanIntf.Config.AccessVlan
		log.Infof("Vlan id : %d observed for Member port addition configuration!", accessVlanId)
		accessVlanFound = true
	}
	/* check whether trunk vlan info is present! */
	if switchedVlanIntf.Config.TrunkVlans != nil {
		vlanUnionList := switchedVlanIntf.Config.TrunkVlans
		if len(vlanUnionList) != 0 {
			trunkVlanFound = true
		}
		for _, vlanUnion := range vlanUnionList {
			vlanUnionType := reflect.TypeOf(vlanUnion).Elem()

			switch vlanUnionType {

			case reflect.TypeOf(ocbinds.OpenconfigInterfaces_Interfaces_Interface_Ethernet_SwitchedVlan_Config_TrunkVlans_Union_String{}):
				val := (vlanUnion).(*ocbinds.OpenconfigInterfaces_Interfaces_Interface_Ethernet_SwitchedVlan_Config_TrunkVlans_Union_String)
				trunkVlanSlice = append(trunkVlanSlice, val.String)
			case reflect.TypeOf(ocbinds.OpenconfigInterfaces_Interfaces_Interface_Ethernet_SwitchedVlan_Config_TrunkVlans_Union_Uint16{}):
				val := (vlanUnion).(*ocbinds.OpenconfigInterfaces_Interfaces_Interface_Ethernet_SwitchedVlan_Config_TrunkVlans_Union_Uint16)
				trunkVlanSlice = append(trunkVlanSlice, "Vlan" + strconv.Itoa(int(val.Uint16)))
			}
		}
	}

	/* If access or trunk vlan is present, do the interface mode config */
	/* Note special logic has to be there for access/trunk mode config */
	if switchedVlanIntf.Config.InterfaceMode == ocbinds.OpenconfigVlan_VlanModeType_UNSET {
		return err
	}
	ifMode := switchedVlanIntf.Config.InterfaceMode

	switch ifMode {
	case ocbinds.OpenconfigVlan_VlanModeType_ACCESS:
		/* If Vlan is also present, update the cache! */
		if accessVlanFound {
			log.Info("Access VLAN found!")
			vlanStr := "Vlan" + strconv.Itoa(int(accessVlanId))
			err = app.validateVlanExists(d, &vlanStr)
			if err != nil {
				errStr := "Invalid VLAN: " + strconv.Itoa(int(accessVlanId))
				err = tlerr.InvalidArgsError{Format: errStr}
				return err
			}
			memberPortEntryMap := make(map[string]string)
			memberPortEntry := db.Value{Field: memberPortEntryMap}
			memberPortEntry.Field["tagging_mode"] = "untagged"

			if app.vlanD.vlanMemberTableMap[vlanStr] == nil {
				app.vlanD.vlanMemberTableMap[vlanStr] = make(map[string]dbEntry)
			}
			app.vlanD.vlanMemberTableMap[vlanStr][*ifKey] = dbEntry{entry: memberPortEntry, op: opCreate}
			log.Info("Untagged Port added to cache!")

		} else {
			app.mode = intfMode{ifName: *ifKey, mode: ACCESS}
		}
	case ocbinds.OpenconfigVlan_VlanModeType_TRUNK:
		if trunkVlanFound {
			memberPortEntryMap := make(map[string]string)
			memberPortEntry := db.Value{Field: memberPortEntryMap}
			memberPortEntry.Field["tagging_mode"] = "tagged"
			for _, vlanId := range trunkVlanSlice {
				if app.vlanD.vlanMemberTableMap[vlanId] == nil {
					app.vlanD.vlanMemberTableMap[vlanId] = make(map[string]dbEntry)
				}
				app.vlanD.vlanMemberTableMap[vlanId][*ifKey] = dbEntry{entry: memberPortEntry, op: opUpdate}
				log.Info("Tagged Port added to cache!")
			}
		}

	}
	return err
}

func (app *IntfApp) translateCommonPhyIntf(d *db.DB, ifKey *string, inpOp reqType) ([]db.WatchKeys, error) {

	var err error
	var keys []db.WatchKeys

	app.allIpKeys, _ = app.doGetAllIpKeys(d, app.intfD.intfIPTs)
	intfObj := app.getAppRootObject()
	intf := intfObj.Interface[*ifKey]
	curr, err := d.GetEntry(app.intfD.portTs, db.Key{Comp: []string{*ifKey}})
	if err != nil {
		errStr := "Invalid Interface:" + *ifKey
		ifValidErr := tlerr.InvalidArgsError{Format: errStr}
		return keys, ifValidErr
	}
	if !curr.IsPopulated() {
		log.Error("Interface ", *ifKey, " doesn't exist in DB")
		err = errors.New("Interface: " + *ifKey + " doesn't exist in DB")
		return keys, err
	}
	/* Handling Interface Config updates */
	app.translateCommonIntfConfig(ifKey, intf, &curr)

	/* Handling Interface Ethernet updates */
	err = app.translateCommonPhyIntfEthernet(d, ifKey, intf)
	if err != nil {
		return keys, err
	}

	/* Handling Interface SubInterfaces updates */
	err = app.translateCommonPhyIntfSubInterfaces(d, ifKey, intf)
	if err != nil {
		return keys, err
	}
	return keys, err
}

func (app *IntfApp) processUpdateIfTable(d *db.DB) error {
	var err error
	/* Updating the Interface Table */
	for ifName, ifEntry := range app.ifTableMap {
		if ifEntry.op == opUpdate {
			log.Info("Updating entry for ", ifName)
			err = d.SetEntry(app.intfD.portTs, db.Key{Comp: []string{ifName}}, ifEntry.entry)
			if err != nil {
				errStr := "Updating Interface table for Interface : " + ifName + " failed"
				return errors.New(errStr)
			}
		}
	}
	return err
}

func (app *IntfApp) processUpdateIfIpTableMap(d *db.DB) error {
	var err error
	/* Updating the Interface IP table */
	for ifName, ipEntries := range app.intfD.ifIPTableMap {
		for ip, ipEntry := range ipEntries {
			if ipEntry.op == opCreate {
				log.Info("Creating entry for ", ifName, ":", ip)
				err = d.CreateEntry(app.intfD.intfIPTs, db.Key{Comp: []string{ifName, ip}}, ipEntry.entry)
				if err != nil {
					errStr := "Creating entry for " + ifName + ":" + ip + " failed"
					return errors.New(errStr)
				}
			} else if ipEntry.op == opDelete {
				log.Info("Deleting entry for ", ifName, ":", ip)
				err = d.DeleteEntry(app.intfD.intfIPTs, db.Key{Comp: []string{ifName, ip}})
				if err != nil {
					errStr := "Deleting entry for " + ifName + ":" + ip + " failed"
					return errors.New(errStr)
				}
			}
		}
	}
	return err
}

func (app *IntfApp) updateAccessModeConfig(d *db.DB, ifName *string) error {
	if len(*ifName) == 0 {
		return errors.New("Empty Interface name received!")
	}
	var vlanKeys []db.Key
	vlanTable, err := d.GetTable(app.vlanD.vlanMemberTs)
	if err != nil {
		return err
	}

	vlanKeys, err = vlanTable.GetKeys()
	log.Infof("Found %d VLAN member table keys", len(vlanKeys))
	var vlanSlice []string

	/* Iterate over all vlan member keys, delete the ones which has tagged mode, keep the list of
	   those vlans in a slice */
	for _, vlanKey := range vlanKeys {
		if len(vlanKeys) < 2 {
			continue
		}
		if vlanKey.Get(1) == *ifName {
			entry, err := d.GetEntry(app.vlanD.vlanMemberTs, vlanKey)
			if err != nil {
				log.Errorf("Error found on fetching Vlan member info from App DB for Interface Name : %s", *ifName)
				return err
			}
			tagInfo, ok := entry.Field["tagging_mode"]
			if ok {
				if tagInfo != "tagged" {
					continue
				}
				vlanSlice = append(vlanSlice, vlanKey.Get(0))
				d.DeleteEntry(app.vlanD.vlanMemberTs, vlanKey)
			}
		}
	}

	/* Currently vlanSlice contains list of all vlans containing specific taggedPort */
	/* TODO: Iterate through vlanSlice and update the "members@" key for VLAN table */
	for _, vlan := range vlanSlice {
		vlanEntry, err := d.GetEntry(app.vlanD.vlanTs, db.Key{Comp: []string{vlan}})
		if err != nil {
			log.Errorf("Get Entry for VLAN table with Vlan:%s failed!", vlan)
			return err
		}
		memberPortsInfo, ok := vlanEntry.Field["members@"]
		if ok {
			if !strings.Contains(memberPortsInfo, *ifName) {
				continue
			}
			memberPortsList := strings.Split(memberPortsInfo, ",")
			idx := 0
			memberFound := false

			for idxVal, memberName := range memberPortsList {
				if memberName == *ifName {
					memberFound = true
					idx = idxVal
					break
				}
			}
			if memberFound {
				memberPortsList = append(memberPortsList[:idx], memberPortsList[idx+1:]...)

				memberPortsStr, err := generateMemberPortsStringFromSlice(memberPortsList)
				if err != nil {
					return err
				}

				vlanEntry.Field["members@"] = *memberPortsStr
				d.SetEntry(app.vlanD.vlanTs, db.Key{Comp: []string{vlan}}, vlanEntry)
			} else {
				continue
			}
		}
	}
	return nil
}

func (app *IntfApp) processUpdateInterfaceModeConfig(d *db.DB, ifName *string) error {
	var err error
	switch app.mode.mode {
	case ACCESS:
		err := app.updateAccessModeConfig(d, &app.mode.ifName)
		if err != nil {
			return err
		}
	case TRUNK:
		break
	case MODE_UNSET:
		break
	}
	return err
}

func (app *IntfApp) processCommonPhyIntf(d *db.DB) error {
	var err error
	err = app.processUpdateIfTable(d)
	if err != nil {
		return err
	}

	err = app.processUpdateIfIpTableMap(d)
	if err != nil {
		return err
	}

	err = app.processUpdateVlanMemberTableMap(d)
	if err != nil {
		return err
	}

	err = app.processUpdateInterfaceModeConfig(d, &app.mode.ifName)
	if err != nil {
		return err
	}
	return err
}

/******* DELETE FUNCTIONS ********/

func (app *IntfApp) translateDeletePhyIntf(d *db.DB, ifName string) ([]db.WatchKeys, error) {
	var err error
	var keys []db.WatchKeys
	intfObj := app.getAppRootObject()
	intf := intfObj.Interface[ifName]

	if intf.Subinterfaces == nil {
		return keys, err
	}
	subIf := intf.Subinterfaces.Subinterface[0]
	if subIf != nil {
		if subIf.Ipv4 != nil && subIf.Ipv4.Addresses != nil {
			for ip, _ := range subIf.Ipv4.Addresses.Address {
				addr := subIf.Ipv4.Addresses.Address[ip]
				if addr != nil {
					ipAddr := addr.Ip
					log.Info("IPv4 address = ", *ipAddr)
					if !validIPv4(*ipAddr) {
						errStr := "Invalid IPv4 address " + *ipAddr
						ipValidErr := tlerr.InvalidArgsError{Format: errStr}
						return keys, ipValidErr
					}
					err = app.validateIp(d, ifName, *ipAddr)
					if err != nil {
						errStr := "Invalid IPv4 address " + *ipAddr
						ipValidErr := tlerr.InvalidArgsError{Format: errStr}
						return keys, ipValidErr
					}
				}
			}
		}
		if subIf.Ipv6 != nil && subIf.Ipv6.Addresses != nil {
			for ip, _ := range subIf.Ipv6.Addresses.Address {
				addr := subIf.Ipv6.Addresses.Address[ip]
				if addr != nil {
					ipAddr := addr.Ip
					log.Info("IPv6 address = ", *ipAddr)
					if !validIPv6(*ipAddr) {
						errStr := "Invalid IPv6 address " + *ipAddr
						ipValidErr := tlerr.InvalidArgsError{Format: errStr}
						return keys, ipValidErr
					}
					err = app.validateIp(d, ifName, *ipAddr)
					if err != nil {
						errStr := "Invalid IPv6 address:" + *ipAddr
						ipValidErr := tlerr.InvalidArgsError{Format: errStr}
						return keys, ipValidErr
					}
				}
			}
		}
	} else {
		err = errors.New("Only subinterface index 0 is supported")
		return keys, err
	}
	return keys, err
}

func (app *IntfApp) processDeletePhyIntf(d *db.DB) error {
	/* Delete the elements present in Interface IP table Map */
	var err error
	for ifKey, entrylist := range app.intfD.ifIPTableMap {
		for ip, _ := range entrylist {
			err = d.DeleteEntry(app.intfD.intfIPTs, db.Key{Comp: []string{ifKey, ip}})
			if err != nil {
				return err
			}
			log.Infof("Deleted IP : %s for Interface : %s", ip, ifKey)
		}
	}
	return err
}

/******** SUBSCRIBE FUNCTIONS ******/

func (app *IntfApp) translateSubscribePhyIntf(ifKey *string, pInfo *PathInfo) (*notificationOpts, *notificationInfo, error) {
	var err error
	notifInfo := notificationInfo{dbno: db.ApplDB}

	err = app.validateInterface(app.appDB, *ifKey, db.Key{Comp: []string{*ifKey}})
	if err != nil {
		return nil, nil, err
	}
	if pInfo.HasSuffix("/state/oper-status") {
		notifInfo.table = db.TableSpec{Name: "PORT_TABLE"}
		notifInfo.key = asKey(*ifKey)
		notifInfo.needCache = true
		return &notificationOpts{pType: OnChange}, &notifInfo, nil
	}
	return nil, nil, err
}
