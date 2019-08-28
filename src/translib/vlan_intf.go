package translib

import (
	"errors"
	log "github.com/golang/glog"
	"strings"
	"translib/db"
	"translib/tlerr"
)

/******** CONFIG FUNCTIONS ********/

func (app *IntfApp) translateCommonVlanIntf(d *db.DB, vlanName *string, inpOp reqType) ([]db.WatchKeys, error) {
	var err error
	var keys []db.WatchKeys
	log.Info("TranslateCommonVlanIntf() called for ", *vlanName)
	intfObj := app.getAppRootObject()

	m := make(map[string]string)
	entryVal := db.Value{Field: m}
	entryVal.Field["vlanid"], err = getVlanIdFromVlanName(vlanName)
	if err != nil {
		return keys, err
	}

	vlan := intfObj.Interface[*vlanName]
	curr, _ := d.GetEntry(app.vlanD.vlanTs, db.Key{Comp: []string{*vlanName}})
	if !curr.IsPopulated() {
		log.Info("VLAN-" + *vlanName + " not present in DB, need to create it!!")
		app.ifTableMap[*vlanName] = dbEntry{op: opCreate, entry: entryVal}
		return keys, nil
	}
	app.translateCommonIntfConfig(vlanName, vlan, &curr)
	return keys, err
}

func (app *IntfApp) processUpdateVlanTableMap(d *db.DB) error {
	var err error

	/* Updating the VLAN table */
	for vlanId, vlanEntry := range app.ifTableMap {
		switch vlanEntry.op {
		case opCreate:
			err = d.CreateEntry(app.vlanD.vlanTs, db.Key{Comp: []string{vlanId}}, vlanEntry.entry)
			if err != nil {
				errStr := "Creating VLAN entry for VLAN : " + vlanId + " failed"
				return errors.New(errStr)
			}
		case opUpdate:
			err = d.SetEntry(app.vlanD.vlanTs, db.Key{Comp: []string{vlanId}}, vlanEntry.entry)
			if err != nil {
				errStr := "Updating VLAN entry for VLAN : " + vlanId + " failed"
				return errors.New(errStr)
			}
		}
	}
	return err
}

func (app *IntfApp) processUpdateVlanMemberTableMap(d *db.DB) error {
	var err error
	/* Updating the VLAN member table */

	for vlanStr, ifEntries := range app.vlanD.vlanMemberTableMap {
		var memberPortsListStrB strings.Builder
		var memberPortsList []string

		ifEntryLen := len(ifEntries)
		idx := 1

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
						idx += 1
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
						idx += 1
						continue
					}
				}
				err = d.SetEntry(app.vlanD.vlanMemberTs, db.Key{Comp: []string{vlanStr, ifName}}, ifEntry.entry)
				if err != nil {
					errStr := "Set entry for VLAN member table with vlan : " + vlanStr + " If : " + ifName + " failed"
					return errors.New(errStr)
				}
			}

			if idx != ifEntryLen {
				memberPortsListStrB.WriteString(ifName + ",")
			} else {
				memberPortsListStrB.WriteString(ifName)
			}
			idx = idx + 1
		}
		vlanEntry.Field["members@"] = memberPortsListStrB.String()

		/* Updating VLAN map with updated members */
		err = d.SetEntry(app.vlanD.vlanTs, db.Key{Comp: []string{vlanStr}}, vlanEntry)
		if err != nil {
			return errors.New("Updating VLAN table with member ports failed")
		}
	}
	return err
}

func (app *IntfApp) processCommonVlanIntf(d *db.DB) error {
	var err error
	err = app.processUpdateVlanTableMap(d)
	if err != nil {
		return err
	}

	err = app.processUpdateVlanMemberTableMap(d)
	if err != nil {
		return err
	}
	return err
}

/********* DELETE FUNCTIONS ********/

func (app *IntfApp) translateDeleteVlanIntf(d *db.DB, vlanName string) ([]db.WatchKeys, error) {
	var err error
	var keys []db.WatchKeys
	log.Info("translateDeleteVlanIntf() called")
	curr, err := d.GetEntry(app.vlanD.vlanTs, db.Key{Comp: []string{vlanName}})
	if err != nil {
		errStr := "Invalid Vlan: " + vlanName
		return keys, tlerr.InvalidArgsError{Format: errStr}
	}
	app.ifTableMap[vlanName] = dbEntry{entry: curr, op: opDelete}
	return keys, err
}

func (app *IntfApp) processDeleteVlanIntf(d *db.DB) error {
	var err error
	for vlanKey, dbentry := range app.ifTableMap {
		memberPortsVal, ok := dbentry.entry.Field["members@"]
		if ok {
			memberPorts := generateMemberPortsSliceFromString(&memberPortsVal)
			/* Empty member ports */
			if memberPorts == nil {
				return nil
			}
			log.Info("MemberPorts = ", memberPortsVal)

			for _, memberPort := range memberPorts {
				log.Infof("Member Port:%s part of vlan:%s to be deleted!", memberPort, vlanKey)
				err = d.DeleteEntry(app.vlanD.vlanMemberTs, db.Key{Comp: []string{vlanKey, memberPort}})
				if err != nil {
					return err
				}
			}
		}
		err = d.DeleteEntry(app.vlanD.vlanTs, db.Key{Comp: []string{vlanKey}})
		if err != nil {
			return err
		}
	}
	return err
}
