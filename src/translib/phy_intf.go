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

func (app *IntfApp) translateUpdatePhyIntfSubInterfaces(d *db.DB, ifKey *string, intf *ocbinds.OpenconfigInterfaces_Interfaces_Interface) error {
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

func (app *IntfApp) translateUpdatePhyIntfEthernet(d *db.DB, ifKey *string, intf *ocbinds.OpenconfigInterfaces_Interfaces_Interface) error {
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

	if !app.validateIpCfgredForInterface(d, ifKey) {
		errStr := "Interface: " + *ifKey + ", IP address cannot exist with L2 modes"
		err = tlerr.InvalidArgsError{Format: errStr}
		return err
	}

	var accessVlanId uint16 = 0
	var trunkVlanSlice []string
	accessVlanFound := false
	trunkVlanFound := false

	if switchedVlanIntf.Config.AccessVlan != nil {
		accessVlanId = *switchedVlanIntf.Config.AccessVlan
		log.Infof("Vlan id : %d observed for Member port addition configuration!", accessVlanId)
		accessVlanFound = true
	}

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
				trunkVlanSlice = append(trunkVlanSlice, "Vlan"+strconv.Itoa(int(val.Uint16)))
			}
		}
	}

	/* Note special logic has to be there for access/trunk mode config alone without VLANs present */
	if switchedVlanIntf.Config.InterfaceMode == ocbinds.OpenconfigVlan_VlanModeType_UNSET {
		return err
	}
	ifMode := switchedVlanIntf.Config.InterfaceMode

	switch ifMode {
	case ocbinds.OpenconfigVlan_VlanModeType_ACCESS:
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

			if app.vlanD.vlanMembersTableMap[vlanStr] == nil {
				app.vlanD.vlanMembersTableMap[vlanStr] = make(map[string]dbEntry)
			}
			app.vlanD.vlanMembersTableMap[vlanStr][*ifKey] = dbEntry{entry: memberPortEntry, op: opCreate}
			log.Info("Untagged Port added to cache!")

		} else {
			/* Configuring Interface Mode as ACCESS only without VLAN info*/
			app.mode = intfMode{ifName: *ifKey, mode: ACCESS}
		}
	case ocbinds.OpenconfigVlan_VlanModeType_TRUNK:
		if trunkVlanFound {
			memberPortEntryMap := make(map[string]string)
			memberPortEntry := db.Value{Field: memberPortEntryMap}
			memberPortEntry.Field["tagging_mode"] = "tagged"
			for _, vlanId := range trunkVlanSlice {
				if app.vlanD.vlanMembersTableMap[vlanId] == nil {
					app.vlanD.vlanMembersTableMap[vlanId] = make(map[string]dbEntry)
				}
				app.vlanD.vlanMembersTableMap[vlanId][*ifKey] = dbEntry{entry: memberPortEntry, op: opUpdate}
				log.Info("Tagged Port added to cache!")
			}
		}

	}
	return err
}

func (app *IntfApp) translateUpdatePhyIntf(d *db.DB, ifKey *string, inpOp reqType) ([]db.WatchKeys, error) {

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
	app.translateUpdateIntfConfig(ifKey, intf, &curr)

	/* Handling Interface Ethernet updates */
	err = app.translateUpdatePhyIntfEthernet(d, ifKey, intf)
	if err != nil {
		return keys, err
	}

	/* Handling Interface SubInterfaces updates */
	err = app.translateUpdatePhyIntfSubInterfaces(d, ifKey, intf)
	if err != nil {
		return keys, err
	}
	return keys, err
}

func (app *IntfApp) processUpdatePhyIntfConfig(d *db.DB) error {
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

func (app *IntfApp) processUpdatePhyIntfSubInterfaces(d *db.DB) error {
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

func (app *IntfApp) processUpdatePhyIntfVlanAdd(d *db.DB) error {
	var err error
	/* Updating the VLAN member table */

	for vlanStr, ifEntries := range app.vlanD.vlanMembersTableMap {
		var memberPortsListStrB strings.Builder
		var memberPortsList []string

		vlanEntry, err := d.GetEntry(app.vlanD.vlanTs, db.Key{Comp: []string{vlanStr}})
		if !vlanEntry.IsPopulated() {
			errStr := "Failed to retrieve memberPorts info of VLAN : " + vlanStr
			return errors.New(errStr)
		}
		memberPortsExists := false
		memberPortsListStr, ok := vlanEntry.Field["members@"]
		if ok {
			if len(memberPortsListStr) != 0 {
				memberPortsListStrB.WriteString(vlanEntry.Field["members@"])
				memberPortsList = generateMemberPortsSliceFromString(&memberPortsListStr)
				memberPortsExists = true
			}
		}

		for ifName, ifEntry := range ifEntries {
			switch ifEntry.op {
			case opCreate:
				log.Info("Vlan = ", vlanStr)
				log.Info("Interface name = ", ifName)
				if memberPortsExists {
					if checkMemberPortExistsInList(memberPortsList, &ifName) {
						errStr := "Interface: " + ifName + " is already part of VLAN: " + vlanStr
						log.Error(errStr)
						continue
					}
				}
				err = d.CreateEntry(app.vlanD.vlanMemberTs, db.Key{Comp: []string{vlanStr, ifName}}, ifEntry.entry)
				if err != nil {
					errStr := "Creating entry for VLAN member table with vlan : " + vlanStr + " If : " + ifName + " failed"
					return errors.New(errStr)
				}
			case opUpdate:
				if memberPortsExists {
					if checkMemberPortExistsInList(memberPortsList, &ifName) {
						errStr := "Interface: " + ifName + " is already part of VLAN: " + vlanStr
						log.Error(errStr)
						continue
					}
				}
				err = d.SetEntry(app.vlanD.vlanMemberTs, db.Key{Comp: []string{vlanStr, ifName}}, ifEntry.entry)
				if err != nil {
					errStr := "Set entry for VLAN member table with vlan : " + vlanStr + " If : " + ifName + " failed"
					return errors.New(errStr)
				}
			}
			if len(memberPortsList) == 0 && len(ifEntries) == 1 {
				memberPortsListStrB.WriteString(ifName)
			} else {
				memberPortsListStrB.WriteString("," + ifName)
			}
		}
		log.Infof("Member ports = %s", memberPortsListStrB.String())
		vlanEntry.Field["members@"] = memberPortsListStrB.String()

		err = d.SetEntry(app.vlanD.vlanTs, db.Key{Comp: []string{vlanStr}}, vlanEntry)
		if err != nil {
			return errors.New("Updating VLAN table with member ports failed")
		}
	}
	return err
}

func (app *IntfApp) removeVlanMembFromIntfAndFetchVlanList(d *db.DB, ifName *string) ([]string, error) {
	var err error
	var vlanKeys []db.Key
	vlanTable, err := d.GetTable(app.vlanD.vlanMemberTs)
	if err != nil {
		return nil, err
	}

	vlanKeys, err = vlanTable.GetKeys()
	var vlanSlice []string

	for _, vlanKey := range vlanKeys {
		if len(vlanKeys) < 2 {
			continue
		}
		if vlanKey.Get(1) == *ifName {
			entry, err := d.GetEntry(app.vlanD.vlanMemberTs, vlanKey)
			if err != nil {
				log.Errorf("Error found on fetching Vlan member info from App DB for Interface Name : %s", *ifName)
				return vlanSlice, err
			}
			tagInfo, ok := entry.Field["tagging_mode"]
			if ok {
				switch app.mode.mode {
				case ACCESS:
					if tagInfo != "tagged" {
						continue
					}
				case TRUNK:
					if tagInfo != "untagged" {
						continue
					}
				}
				vlanSlice = append(vlanSlice, vlanKey.Get(0))
				d.DeleteEntry(app.vlanD.vlanMemberTs, vlanKey)
			}
		}
	}
	return vlanSlice, err
}

func (app *IntfApp) removeAndUpdateMembersListForVlan(d *db.DB, ifName *string, vlan *string) error {

	vlanEntry, err := d.GetEntry(app.vlanD.vlanTs, db.Key{Comp: []string{*vlan}})
	if err != nil {
		log.Errorf("Get Entry for VLAN table with Vlan:%s failed!", *vlan)
		return err
	}
	memberPortsInfo, ok := vlanEntry.Field["members@"]
	if ok {
		memberPortsList := generateMemberPortsSliceFromString(&memberPortsInfo)
		if memberPortsList == nil {
			return nil
		}
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
			if len(memberPortsList) == 0 {
				log.Info("Deleting the members@")
				delete(vlanEntry.Field, "members@")
			} else {
				memberPortsStr := generateMemberPortsStringFromSlice(memberPortsList)
				log.Infof("Updated Member ports = %s for VLAN: %s", *memberPortsStr, *vlan)
				vlanEntry.Field["members@"] = *memberPortsStr
			}
			d.SetEntry(app.vlanD.vlanTs, db.Key{Comp: []string{*vlan}}, vlanEntry)
		} else {
			return nil
		}
	}
	return nil
}

func (app *IntfApp) updateMembersListForVlanTable(d *db.DB, ifName *string, vlanSlice []string) error {
	var err error

	for _, vlan := range vlanSlice {
		err = app.removeAndUpdateMembersListForVlan(d, ifName, &vlan)
		if err != nil {
			return err
		}
	}
	return err
}

func (app *IntfApp) updateAccessModeConfig(d *db.DB, ifName *string) error {
	var err error

	if len(*ifName) == 0 {
		return errors.New("Empty Interface name received!")
	}

	vlanList, err := app.removeVlanMembFromIntfAndFetchVlanList(d, ifName)
	if err != nil {
		return err
	}

	err = app.updateMembersListForVlanTable(d, ifName, vlanList)
	if err != nil {
		return err
	}
	return err
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
	case MODE_UNSET:
		break
	}
	return err
}

func (app *IntfApp) processUpdatePhyIntf(d *db.DB) error {
	var err error
	err = app.processUpdatePhyIntfConfig(d)
	if err != nil {
		return err
	}

	err = app.processUpdatePhyIntfSubInterfaces(d)
	if err != nil {
		return err
	}

	err = app.processUpdatePhyIntfVlanAdd(d)
	if err != nil {
		return err
	}

	/* Switchport access/trunk mode config without VLAN */
	/* This mode will be set in the translate fn, when request is just for mode without VLAN info. */
	if app.mode.mode != MODE_UNSET {
		err = app.processUpdateInterfaceModeConfig(d, &app.mode.ifName)
		if err != nil {
			return err
		}
	}
	return err
}

/******* DELETE FUNCTIONS ********/

/* TODO: Update the Data Structure to Map, since you could get request for multiple interfaces in JSON request */
func (app *IntfApp) translateDeletePhyIntfEthernetSwitchedVlan(d *db.DB, switchedVlanIntf *ocbinds.OpenconfigInterfaces_Interfaces_Interface_Ethernet_SwitchedVlan, ifName *string) {
	vlanFound := false
	var ifVlanInfo ifVlan
	if switchedVlanIntf.Config != nil {
		if switchedVlanIntf.Config.AccessVlan != nil {
			accessVlan := switchedVlanIntf.Config.AccessVlan
			accessVlanStr := "Vlan" + strconv.Itoa(int(*accessVlan))
			ifVlanInfo.accessVlan = &accessVlanStr
			vlanFound = true
		}
		if switchedVlanIntf.Config.TrunkVlans != nil {
			trunkVlansUnionList := switchedVlanIntf.Config.TrunkVlans
			for _, trunkVlanUnion := range trunkVlansUnionList {
				trunkVlanUnionType := reflect.TypeOf(trunkVlanUnion).Elem()

				switch trunkVlanUnionType {

				case reflect.TypeOf(ocbinds.OpenconfigInterfaces_Interfaces_Interface_Ethernet_SwitchedVlan_Config_TrunkVlans_Union_String{}):
					val := (trunkVlanUnion).(*ocbinds.OpenconfigInterfaces_Interfaces_Interface_Ethernet_SwitchedVlan_Config_TrunkVlans_Union_String)
					ifVlanInfo.trunkVlans = append(app.intfD.ifVlanInfo.trunkVlans, val.String)
				case reflect.TypeOf(ocbinds.OpenconfigInterfaces_Interfaces_Interface_Ethernet_SwitchedVlan_Config_TrunkVlans_Union_Uint16{}):
					val := (trunkVlanUnion).(*ocbinds.OpenconfigInterfaces_Interfaces_Interface_Ethernet_SwitchedVlan_Config_TrunkVlans_Union_Uint16)
					ifVlanInfo.trunkVlans = append(app.intfD.ifVlanInfo.trunkVlans, "Vlan"+strconv.Itoa(int(val.Uint16)))
				}
			}
			vlanFound = true
		}
		if vlanFound {
			ifVlanInfo.ifName = ifName
			app.intfD.ifVlanInfo = &ifVlanInfo
		}
	}
}

func (app *IntfApp) translateDeletePhyIntfEthernet(d *db.DB, intf *ocbinds.OpenconfigInterfaces_Interfaces_Interface, ifName *string) error {
	var err error
	if intf.Ethernet == nil {
		return err
	}
	if intf.Ethernet.SwitchedVlan == nil {
		return err
	}
	switchedVlanIntf := intf.Ethernet.SwitchedVlan
	app.translateDeletePhyIntfEthernetSwitchedVlan(d, switchedVlanIntf, ifName)

	return err
}

func (app *IntfApp) translateDeletePhyIntfSubInterfaces(d *db.DB, intf *ocbinds.OpenconfigInterfaces_Interfaces_Interface, ifName *string) error {
	var err error
	if intf.Subinterfaces == nil {
		return err
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
						return ipValidErr
					}
					err = app.validateIp(d, *ifName, *ipAddr)
					if err != nil {
						errStr := "Invalid IPv4 address " + *ipAddr
						ipValidErr := tlerr.InvalidArgsError{Format: errStr}
						return ipValidErr
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
						return ipValidErr
					}
					err = app.validateIp(d, *ifName, *ipAddr)
					if err != nil {
						errStr := "Invalid IPv6 address:" + *ipAddr
						ipValidErr := tlerr.InvalidArgsError{Format: errStr}
						return ipValidErr
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

func (app *IntfApp) translateDeletePhyIntf(d *db.DB, ifName string) ([]db.WatchKeys, error) {
	var err error
	var keys []db.WatchKeys

	intfObj := app.getAppRootObject()
	intf := intfObj.Interface[ifName]

	err = app.translateDeletePhyIntfSubInterfaces(d, intf, &ifName)
	if err != nil {
		return keys, err
	}

	err = app.translateDeletePhyIntfEthernet(d, intf, &ifName)
	if err != nil {
		return keys, err
	}

	return keys, err
}

func (app *IntfApp) processDeletePhyIntfSubInterfaces(d *db.DB) error {
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

func (app *IntfApp) processDeletePhyIntfVlanRemoval(d *db.DB) error {
	var err error

	if app.intfD.ifVlanInfo == nil {
		return err
	}
	if app.intfD.ifVlanInfo.ifName == nil {
		return err
	}

	ifName := app.intfD.ifVlanInfo.ifName
	accessVlan := app.intfD.ifVlanInfo.accessVlan
	trunkVlans := app.intfD.ifVlanInfo.trunkVlans

	if accessVlan != nil {
		log.Infof("Access VLAN received - %s received for Interface - %s", *accessVlan, *ifName)
		memberPortEntry, err := d.GetEntry(app.vlanD.vlanMemberTs, db.Key{Comp: []string{*accessVlan, *ifName}})
		if err != nil || !memberPortEntry.IsPopulated() {
			errStr := "Access Vlan: " + *accessVlan + " not configured for Interface: " + *ifName
			return errors.New(errStr)
		}
		tagMode, ok := memberPortEntry.Field["tagging_mode"]
		if !ok {
			errStr := "tagging_mode entry is not present for VLAN: " + *accessVlan + " Interface: " + *ifName
			return errors.New(errStr)
		}
		if tagMode != "untagged" {
			errStr := "Member port: " + *ifName + " is not configured as untagged port to VLAN: " + *accessVlan
			return errors.New(errStr)
		}
		err = d.DeleteEntry(app.vlanD.vlanMemberTs, db.Key{Comp: []string{*accessVlan, *ifName}})
		if err != nil {
			return err
		}
		app.removeMemberPortFromVlan(d, accessVlan, ifName)
	}
	if trunkVlans != nil {
		for _, trunkVlan := range trunkVlans {
			log.Infof("Trunk VLAN received - %s for Interface - %s", trunkVlan, *ifName)
			memberPortEntry, err := d.GetEntry(app.vlanD.vlanMemberTs, db.Key{Comp: []string{trunkVlan, *ifName}})
			if err != nil || !memberPortEntry.IsPopulated() {
				errStr := "Trunk Vlan: " + trunkVlan + " not configured for Interface: " + *ifName
				return errors.New(errStr)
			}
			tagMode, ok := memberPortEntry.Field["tagging_mode"]
			if !ok {
				errStr := "tagging_mode entry is not present for VLAN: " + trunkVlan + " Interface: " + *ifName
				return errors.New(errStr)
			}
			if tagMode != "tagged" {
				errStr := "Member port: " + *ifName + " is not configured as tagged port to VLAN: " + trunkVlan
				return errors.New(errStr)
			}
			err = d.DeleteEntry(app.vlanD.vlanMemberTs, db.Key{Comp: []string{trunkVlan, *ifName}})
			app.removeMemberPortFromVlan(d, &trunkVlan, ifName)
		}
	}
	return err
}

func (app *IntfApp) processDeletePhyIntf(d *db.DB) error {
	var err error

	err = app.processDeletePhyIntfSubInterfaces(d)
	if err != nil {
		return err
	}

	err = app.processDeletePhyIntfVlanRemoval(d)
	if err != nil {
		return err
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
