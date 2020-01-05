package transformer

import (
    "errors"
    "strconv"
    "strings"
    "github.com/openconfig/ygot/ygot"
    "translib/db"
    log "github.com/golang/glog"
    "translib/ocbinds"
)

var qCounterTblAttr [] string = []string {"transmit-pkts", "transmit-octets", "dropped-pkts", "dropped-octets", "watermark"}
var pgCounterTblAttr [] string = []string {"headroom-watermark", "headroom-persistent-watermark", "shared-watermark", "shared-persistent-watermark"}


func init () {
    XlateFuncBind("DbToYang_qos_get_one_intf_one_q_counters_xfmr", DbToYang_qos_get_one_intf_one_q_counters_xfmr)
    XlateFuncBind("DbToYang_qos_get_one_intf_all_q_counters_xfmr", DbToYang_qos_get_one_intf_all_q_counters_xfmr)
    XlateFuncBind("DbToYang_qos_get_all_intf_all_counters_xfmr",   DbToYang_qos_get_all_intf_all_counters_xfmr)
    XlateFuncBind("DbToYang_qos_get_one_intf_all_pg_counters_xfmr", DbToYang_qos_get_one_intf_all_pg_counters_xfmr)
    XlateFuncBind("DbToYang_threshold_breach_counter_field_xfmr", DbToYang_threshold_breach_counter_field_xfmr)
}


type PopulateQueueCounters func (inParams XfmrParams, uri string, oid string, counters *ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Output_Queues_Queue_State) (error)

type PopulatePriorityGroupCounters func (inParams XfmrParams, uri string, oid string, counters *ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Input_PriorityGroups_PriorityGroup_State) (error)


type GetQTrafficType = func (queueTypeMap db.Value, oid string, counter *ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Output_Queues_Queue_State) () 

func getQosRoot (s *ygot.GoStruct) *ocbinds.OpenconfigQos_Qos {
    deviceObj := (*s).(*ocbinds.Device)
    return deviceObj.Qos
}

func getQosIntfRoot (s *ygot.GoStruct) *ocbinds.OpenconfigQos_Qos_Interfaces {
    deviceObj := (*s).(*ocbinds.Device)
    return deviceObj.Qos.Interfaces
}

var DbToYang_qos_name_xfmr FieldXfmrDbtoYang = func(inParams XfmrParams) (map[string]interface{}, error) {
    var err error
    res_map := make(map[string]interface{})
    res_map["name"] =  inParams.key
    return res_map, err
}

func doGetAllQueueOidMap(d *db.DB) (db.Value, error) {

    // COUNTERS_QUEUE_NAME_MAP
    dbSpec := &db.TableSpec{Name: "COUNTERS_QUEUE_NAME_MAP"}
    queueOidMap, err := d.GetMapAll(dbSpec)
    if err != nil {
        log.Info("queueOidMap get failed")
    }

    log.Info("queueOidMap: ", queueOidMap)
    return queueOidMap, err
}

func doGetAllQueueTypeMap(d *db.DB) (db.Value, error) {

    // COUNTERS_QUEUE_TYPE_MAP
    queueTs := &db.TableSpec{Name: "COUNTERS_QUEUE_TYPE_MAP"}
    queueTypeMap, err := d.GetMapAll(queueTs)
    if err != nil {
        log.Info("queueTypeMap get failed")
    }

    log.Info("queueTypeMap: ", queueTypeMap)
    return queueTypeMap, err
}

func doGetAllPriorityGroupOidMap(d *db.DB) (db.Value, error) {

    // COUNTERS_PG_NAME_MAP
    dbSpec := &db.TableSpec{Name: "COUNTERS_PG_NAME_MAP"}
    pgOidMap, err := d.GetMapAll(dbSpec)
    if err != nil {
        log.Info("pgOidMap get failed")
    }

    log.Info("pgOidMap: ", pgOidMap)
    return pgOidMap, err
}

func getIntfQCountersTblKey (d *db.DB, ifQKey string) (string, error) {
    var oid string
    var err error

    queueOidMap, _ := doGetAllQueueOidMap(d);

    if queueOidMap.IsPopulated() {
        _, ok := queueOidMap.Field[ifQKey]
        if !ok {
            err = errors.New("OID info not found from Counters DB for interface queue: " + ifQKey)
        } else {
            oid = queueOidMap.Field[ifQKey]
        }
    } else {
        err = errors.New("Get for OID info from all the interfaces queues from Counters DB failed!")
    }

    return oid, err
}

func getIntfPGCountersTblKey (d *db.DB, ifPGKey string) (string, error) {
    var oid string
    var err error

    priorityGroupOidMap, _ := doGetAllPriorityGroupOidMap(d);

    if priorityGroupOidMap.IsPopulated() {
        _, ok := priorityGroupOidMap.Field[ifPGKey]
        if !ok {
            err = errors.New("OID info not found from Counters DB for interface priorityGroup: " + ifPGKey)
        } else {
            oid = priorityGroupOidMap.Field[ifPGKey]
        }
    } else {
        err = errors.New("Get for OID info from all the interfaces priorityGroups from Counters DB failed!")
    }

    return oid, err
}


func getQosCounters(entry *db.Value, attr string, counter_val **uint64 ) error {

    var ok bool = false
    var val string
    var err error

    val, ok = entry.Field[attr]
    if !ok {
        return errors.New("Attr " + attr + "doesn't exist in the table Map!")
    }

    if len(val) > -1 {
        v, e := strconv.ParseUint(val, 10, 64)
        if err == nil {
            *counter_val = &v
            return nil
        }
        err = e
    }
    return err
}

func getPersistentWatermark(d *db.DB, oid string, stat_key string, counter **uint64)  (error) {
    ts := &db.TableSpec{Name: "PERSISTENT_WATERMARKS"}
    entry, err := d.GetEntry(ts, db.Key{Comp: []string{oid}})
    if err != nil {
        log.Info("getPersistentWatermark: not able to find the oid entry in DB ")
        return err
    }
    
    err = getQosCounters(&entry, stat_key, counter)

    return err
}

func getPeriodicWatermark(d *db.DB, oid string, stat_key string, counter **uint64)  (error) {
    ts := &db.TableSpec{Name: "PERIODIC_WATERMARKS"}
    entry, err := d.GetEntry(ts, db.Key{Comp: []string{oid}})
    if err != nil {
        log.Info("getPeriodicWatermark: not able to find the oid entry in DB ")
        return err
    }
    
    err = getQosCounters(&entry, stat_key, counter)

    return err
}

func getQueueSpecificCounterAttr(targetUriPath string, entry *db.Value, counters *ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Output_Queues_Queue_State) (bool, error) {

    var e error

    switch targetUriPath {
    /* Not supported in SONIC
    case "/openconfig-qos:qos/interfaces/interface/output/queues/queue/state/max-queue-len":
        e = getQosCounters(entry, "SAI_QUEUE_STAT_PACKETS", &counters.MaxQueueLen)
        return true, e

    case "/openconfig-qos:qos/interfaces/interface/output/queues/queue/state/avg-queue-len":
        e = getQosCounters(entry, "SAI_QUEUE_STAT_PACKETS", &counters.AvgQueueLen)
        return true, e
    */

    case "/openconfig-qos:qos/interfaces/interface/output/queues/queue/state/transmit-pkts":
        e = getQosCounters(entry, "SAI_QUEUE_STAT_PACKETS", &counters.TransmitPkts)
        return true, e

    case "/openconfig-qos:qos/interfaces/interface/output/queues/queue/state/transmit-octets":
        e = getQosCounters(entry, "SAI_QUEUE_STAT_BYTES", &counters.TransmitOctets)
        return true, e

    case "/openconfig-qos:qos/interfaces/interface/output/queues/queue/state/dropped-pkts":
        e = getQosCounters(entry, "SAI_QUEUE_STAT_DROPPED_PACKETS", &counters.DroppedPkts)
        return true, e

    case "/openconfig-qos:qos/interfaces/interface/output/queues/queue/state/dropped-octets":
        e = getQosCounters(entry, "SAI_QUEUE_STAT_DROPPED_BYTES", &counters.DroppedOctets)
        return true, e

    case "/openconfig-qos:qos/interfaces/interface/output/queues/queue/state/watermark":
        e = getQosCounters(entry, "SAI_QUEUE_STAT_SHARED_WATERMARK_BYTES", &counters.Watermark)
        return true, e

    default:
        log.Infof(targetUriPath + " - Not an interface state counter attribute or unsupported")
    }
    return false, nil
}

var populateQCounters PopulateQueueCounters = func (inParams XfmrParams, targetUriPath string, oid string, counter *ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Output_Queues_Queue_State) (error) {

    log.Info("PopulateQueueCounters : inParams.curDb : ", inParams.curDb, " D: ", inParams.d, "DB index : ", inParams.dbs[inParams.curDb])

    cntTs := &db.TableSpec{Name: "COUNTERS"}
    entry, dbErr := inParams.dbs[inParams.curDb].GetEntry(cntTs, db.Key{Comp: []string{oid}})
    if dbErr != nil {
        log.Info("PopulateQueueCounters : not able to find the oid entry in DB Counters table")
        return dbErr
    }

    log.Info("targetUriPath is : ", targetUriPath)

    var err error

    switch (targetUriPath) {
    case "/openconfig-qos:qos/interfaces/interface/output/queues/queue/state":
        log.Info("Entering queue-state table")
        for _, attr := range qCounterTblAttr {
            uri := targetUriPath + "/" + attr
            if ok, err := getQueueSpecificCounterAttr(uri, &entry, counter); !ok || err != nil {
                log.Info("Get Counter URI failed :", uri)
                err = errors.New("Get Counter URI failed")
            }
        }
    
        if err == nil {
            // Separately get Persistent watermark from a different table
            err = getPersistentWatermark(inParams.dbs[inParams.curDb], oid, "SAI_QUEUE_STAT_SHARED_WATERMARK_BYTES", &counter.PersistentWatermark)
        }

    // persisten-watermark resides on separate DB table
    case "/openconfig-qos:qos/interfaces/interface/output/queues/queue/state/persistent-watermark":
        err = getPersistentWatermark(inParams.dbs[inParams.curDb], oid, "SAI_QUEUE_STAT_SHARED_WATERMARK_BYTES", &counter.PersistentWatermark)

    default:
        log.Info("Entering default branch")
        _, err = getQueueSpecificCounterAttr(targetUriPath, &entry, counter)
    }

    return err
}


var getQTrafficType GetQTrafficType = func (queueTypeMap db.Value, oid string, counter *ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Output_Queues_Queue_State) () {

    log.Info("GetQTrafficType: ")

    var ac = "AC"
    var mc = "MC"
    var uc = "UC"
    counter.TrafficType =  &ac

    q_type, ok := queueTypeMap.Field[oid]
    if !ok {
        log.Info("Queue oid is not mapped in Queue-Type-Map")
        counter.TrafficType =  &ac
        return
    } else {
        if strings.Compare(q_type, "SAI_QUEUE_TYPE_MULTICAST") == 0 {
            counter.TrafficType =  &mc
        } else {
            if strings.Compare(q_type, "SAI_QUEUE_TYPE_UNICAST") == 0 {
                counter.TrafficType =  &uc
            } else {
                counter.TrafficType =  &ac
            }
        }
    }
}

func getPriorityGroupSpecificCounterAttr(targetUriPath string, d *db.DB, oid string, counter *ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Input_PriorityGroups_PriorityGroup_State) (bool, error) {

    var e error

    switch targetUriPath {
    case "/openconfig-qos:qos/interfaces/interface/input/openconfig-qos-ext:priority-groups/priority-group/state/headroom-watermark":
        e = getPeriodicWatermark(d, oid, "SAI_INGRESS_PRIORITY_GROUP_STAT_XOFF_ROOM_WATERMARK_BYTES", &counter.HeadroomWatermark)
        return true, e

    case "/openconfig-qos:qos/interfaces/interface/input/openconfig-qos-ext:priority-groups/priority-group/state/headroom-persistent-watermark":
        e = getPersistentWatermark(d, oid, "SAI_INGRESS_PRIORITY_GROUP_STAT_XOFF_ROOM_WATERMARK_BYTES", &counter.HeadroomPersistentWatermark)
        return true, e

    case "/openconfig-qos:qos/interfaces/interface/input/openconfig-qos-ext:priority-groups/priority-group/state/shared-watermark":
        e = getPeriodicWatermark(d, oid, "SAI_INGRESS_PRIORITY_GROUP_STAT_SHARED_WATERMARK_BYTES", &counter.SharedWatermark)
        return true, e

    case "/openconfig-qos:qos/interfaces/interface/input/openconfig-qos-ext:priority-groups/priority-group/state/shared-persistent-watermark":
        e = getPersistentWatermark(d, oid, "SAI_INGRESS_PRIORITY_GROUP_STAT_SHARED_WATERMARK_BYTES", &counter.SharedPersistentWatermark)
        return true, e

    default:
        log.Infof(targetUriPath + " - Not an interface PG counter attribute or unsupported")
    }
    return false, nil
}

var populatePriorityGroupCounters PopulatePriorityGroupCounters = func (inParams XfmrParams, targetUriPath string, oid string, counter *ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Input_PriorityGroups_PriorityGroup_State) (error) {

    log.Info("PopulatePriorityGroupCounters : inParams.curDb : ", inParams.curDb, " D: ", inParams.d, "DB index : ", inParams.dbs[inParams.curDb])

    log.Info("targetUriPath is : ", targetUriPath)

    var err error
    switch (targetUriPath) {
    case "/openconfig-qos:qos/interfaces/interface/input/openconfig-qos-ext:priority-groups/priority-group/state":
        log.Info("Entering priority-group-state table")
        for _, attr := range pgCounterTblAttr {
            uri := targetUriPath + "/" + attr
            if ok, err := getPriorityGroupSpecificCounterAttr(uri, inParams.dbs[inParams.curDb], oid, counter); !ok || err != nil {
                log.Info("Get Counter URI failed :", uri)
                err = errors.New("Get Counter URI failed")
            }
        }
    
    default:
        log.Info("Entering default branch")
        _, err = getPriorityGroupSpecificCounterAttr(targetUriPath, inParams.dbs[inParams.curDb], oid, counter)
    }

    return err
}



var DbToYang_qos_get_one_intf_one_q_counters_xfmr SubTreeXfmrDbToYang = func(inParams XfmrParams) error {
    var err error

    qosIntfsObj := getQosIntfRoot(inParams.ygRoot)
    pathInfo := NewPathInfo(inParams.uri)
    intfName := pathInfo.Var("interface-id")
    queueName := pathInfo.Var("name")

    targetUriPath, err := getYangPathFromUri(inParams.uri)
    log.Info("targetUriPath is ", targetUriPath)

    if  targetUriPath != "/openconfig-qos:qos/interfaces/interface/output/queues/queue/state" {
        log.Info("%s is redundant", targetUriPath)
        return err
    }

    var state_counters * ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Output_Queues_Queue_State

    if qosIntfsObj != nil && qosIntfsObj.Interface != nil && len(qosIntfsObj.Interface) > 0 {
        var queuesObj *ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Output_Queues
        queuesObj = qosIntfsObj.Interface[intfName].Output.Queues

        var queueObj *ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Output_Queues_Queue
        if queuesObj != nil {
            queueObj = queuesObj.Queue[queueName]
        }
        state_counters = queueObj.State
    }

    if state_counters == nil  {
        log.Info("DbToYang_qos_get_one_intf_one_q_counters_xfmr - state_counters is nil")
        return err
    }

    state_counters.Name = &queueName

    oid, err := getIntfQCountersTblKey(inParams.dbs[inParams.curDb], intfName+":"+queueName)
    if err != nil {
        log.Info(err)
        return err 
    }
    
    queueTypeMap, _ := doGetAllQueueTypeMap(inParams.dbs[inParams.curDb]);

    getQTrafficType(queueTypeMap, oid, state_counters)

    err = populateQCounters(inParams, targetUriPath, oid, state_counters)

    log.Info("DbToYang_qos_get_one_intf_one_q_counters_xfmr - finished ")

    return err
}

var DbToYang_qos_get_one_intf_all_q_counters_xfmr SubTreeXfmrDbToYang = func(inParams XfmrParams) error {
    var err error

    log.Info("DbToYang_qos_get_one_intf_all_q_counters_xfmr - started ")


    qosIntfsObj := getQosIntfRoot(inParams.ygRoot)
    pathInfo := NewPathInfo(inParams.uri)
    intfName := pathInfo.Var("interface-id")

    targetUriPath, err := getYangPathFromUri(inParams.uri)
    if  targetUriPath != "/openconfig-qos:qos/interfaces/interface/output/queues" {
        log.Info("unexpected uri path: ", targetUriPath)
        return err
    }
    targetUriPath = targetUriPath + "/queue/state"
    //log.Info("targetUriPath is ", targetUriPath)


    var queuesObj *ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Output_Queues
    if qosIntfsObj != nil && qosIntfsObj.Interface != nil && len(qosIntfsObj.Interface) > 0 {
        queuesObj = qosIntfsObj.Interface[intfName].Output.Queues
    }

    queueOidMap, _ := doGetAllQueueOidMap(inParams.dbs[inParams.curDb]);

    queueOidMapFields := queueOidMap.Field

    queueTypeMap, _ := doGetAllQueueTypeMap(inParams.dbs[inParams.curDb]);

    for keyString, oid := range queueOidMapFields {
        s := strings.Split(keyString, ":")
       
        ifName := s[0]
        queueName := s[1]
        
        if ifName == "" {
            continue
        }
        if queueName == "" {
            continue
        }

        if strings.Compare(ifName, intfName) != 0  {
            continue
        }

        if queuesObj == nil {
            ygot.BuildEmptyTree(queuesObj)
        }

        queueObj, _ := queuesObj.NewQueue(queueName)
        ygot.BuildEmptyTree(queueObj)

        queueObj.Name = &queueName
        if queueObj.State == nil {
            ygot.BuildEmptyTree(queueObj.State)
        }

        var state_counters * ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Output_Queues_Queue_State
        state_counters = queueObj.State

        if state_counters == nil  {
            log.Info("DbToYang_qos_get_one_intf_all_q_counters_xfmr - state_counters is nil")
	        return err
        }

        state_counters.Name = &queueName

        getQTrafficType(queueTypeMap, oid, state_counters)

        err = populateQCounters(inParams, targetUriPath, oid, state_counters)

    }

    log.Info("DbToYang_qos_get_one_intf_all_q_counters_xfmr - finished ")

    return err
}

var DbToYang_qos_get_all_intf_all_counters_xfmr SubTreeXfmrDbToYang = func(inParams XfmrParams) error {
    var err error

    log.Info("DbToYang_qos_get_all_intf_all_counters_xfmr - started ")


    qosIntfsObj := getQosIntfRoot(inParams.ygRoot)
    //pathInfo := NewPathInfo(inParams.uri)

    targetUriPath, err := getYangPathFromUri(inParams.uri)
    if  targetUriPath != "/openconfig-qos:qos/interfaces" {
        log.Info("unexpected uri path: ", targetUriPath)
        return err
    }

    // For faster processing, the result is not sorted here. 

    // Queue Counters
    qTargetUriPath := targetUriPath + "/interface/output/queues/queue/state"
    // log.Info("targetUriPath for Queue is ", qTargetUriPath)

    queueOidMap, _ := doGetAllQueueOidMap(inParams.dbs[inParams.curDb]);

    queueOidMapFields := queueOidMap.Field

    queueTypeMap, _ := doGetAllQueueTypeMap(inParams.dbs[inParams.curDb]);

    for keyString, oid := range queueOidMapFields {
        s := strings.Split(keyString, ":")
       
        intfName := s[0]
        queueName := s[1]
        
        if intfName == "" {
            continue
        }
        if queueName == "" {
            continue
        }

        // log.Info("Get intf queue info of ", intfName, ":", queueName)

        if qosIntfsObj == nil {
            ygot.BuildEmptyTree(qosIntfsObj)
        }

        intfObj, ok := qosIntfsObj.Interface[intfName]
        if !ok {
            intfObj, _ = qosIntfsObj.NewInterface(intfName)
            ygot.BuildEmptyTree(intfObj)
            intfObj.InterfaceId = &intfName

            if intfObj.Output == nil {
                ygot.BuildEmptyTree(intfObj.Output)
            }
        }

        queuesObj := intfObj.Output.Queues
        if queuesObj == nil {
            ygot.BuildEmptyTree(queuesObj)
        }

        queueObj, _ := queuesObj.NewQueue(queueName)
        ygot.BuildEmptyTree(queueObj)

        queueObj.Name = &queueName
        if queueObj.State == nil {
            ygot.BuildEmptyTree(queueObj.State)
        }

        var state_counters * ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Output_Queues_Queue_State
        state_counters = queueObj.State

        if state_counters == nil  {
            log.Info("DbToYang_qos_get_all_intf_all_counters_xfmr - state_counters is nil")
	        return err
        }

        state_counters.Name = &queueName

        getQTrafficType(queueTypeMap, oid, state_counters)

        err = populateQCounters(inParams, qTargetUriPath, oid, state_counters)

    }


    // Priority Group counters
    pgTargetUriPath := targetUriPath + "/interface/input/openconfig-qos-ext:priority-groups/priority-group/state"
    // log.Info("targetUriPath for PG is ", pgTargetUriPath)

    priorityGroupOidMap, _ := doGetAllPriorityGroupOidMap(inParams.dbs[inParams.curDb]);

    priorityGroupOidMapFields := priorityGroupOidMap.Field

    for keyString, oid := range priorityGroupOidMapFields {
        s := strings.Split(keyString, ":")
       
        intfName := s[0]
        priorityGroupName := s[1]
        
        if intfName == "" {
            continue
        }
        if priorityGroupName == "" {
            continue
        }

        // log.Info("Get intf queue info of ", intfName, ":", priorityGroupName)

        if qosIntfsObj == nil {
            ygot.BuildEmptyTree(qosIntfsObj)
        }

        intfObj, ok := qosIntfsObj.Interface[intfName]
        if !ok {
            intfObj, _ = qosIntfsObj.NewInterface(intfName)
            ygot.BuildEmptyTree(intfObj)
            intfObj.InterfaceId = &intfName

            if intfObj.Input == nil {
                ygot.BuildEmptyTree(intfObj.Input)
            }
        }

        priorityGroupsObj := intfObj.Input.PriorityGroups
        if priorityGroupsObj == nil {
            ygot.BuildEmptyTree(priorityGroupsObj)
        }

        priorityGroupObj, _ := priorityGroupsObj.NewPriorityGroup(priorityGroupName)
        ygot.BuildEmptyTree(priorityGroupObj)

        priorityGroupObj.Name = &priorityGroupName
        if priorityGroupObj.State == nil {
            ygot.BuildEmptyTree(priorityGroupObj.State)
        }

        var pg_state * ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Input_PriorityGroups_PriorityGroup_State
        pg_state = priorityGroupObj.State

        if pg_state == nil  {
            log.Info("DbToYang_qos_get_all_intf_all_counters_xfmr - pg_state is nil")
	        return err
        }

        pg_state.Name = &priorityGroupName

        err = populatePriorityGroupCounters(inParams, pgTargetUriPath, oid, pg_state)

    }

    log.Info("DbToYang_qos_get_all_intf_all_counters_xfmr - finished ")

    return err
}

var DbToYang_qos_get_one_intf_all_pg_counters_xfmr SubTreeXfmrDbToYang = func(inParams XfmrParams) error {
    var err error

    log.Info("DbToYang_qos_get_one_intf_all_pg_counters_xfmr - started ")


    qosIntfsObj := getQosIntfRoot(inParams.ygRoot)
    pathInfo := NewPathInfo(inParams.uri)
    intfName := pathInfo.Var("interface-id")

    targetUriPath, err := getYangPathFromUri(inParams.uri)
    if  targetUriPath != "/openconfig-qos:qos/interfaces/interface/input/openconfig-qos-ext:priority-groups" {
        log.Info("unexpected uri path: ", targetUriPath)
        return err
    }
    targetUriPath = targetUriPath + "/priority-group/state"
    //log.Info("targetUriPath is ", targetUriPath)


    var priorityGroupsObj *ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Input_PriorityGroups
    if qosIntfsObj != nil && qosIntfsObj.Interface != nil && len(qosIntfsObj.Interface) > 0 {
        priorityGroupsObj = qosIntfsObj.Interface[intfName].Input.PriorityGroups
    }

    priorityGroupMap, _ := doGetAllPriorityGroupOidMap(inParams.dbs[inParams.curDb]);

    priorityGroupMapFields := priorityGroupMap.Field

    for keyString, oid := range priorityGroupMapFields {
        s := strings.Split(keyString, ":")
       
        ifName := s[0]
        priorityGroupName := s[1]
        
        if ifName == "" {
            continue
        }
        if priorityGroupName == "" {
            continue
        }

        if strings.Compare(ifName, intfName) != 0  {
            continue
        }

        if priorityGroupsObj == nil {
            ygot.BuildEmptyTree(priorityGroupsObj)
        }

        priorityGroupObj, _ := priorityGroupsObj.NewPriorityGroup(priorityGroupName)
        ygot.BuildEmptyTree(priorityGroupObj)

        priorityGroupObj.Name = &priorityGroupName
        if priorityGroupObj.State == nil {
            ygot.BuildEmptyTree(priorityGroupObj.State)
        }

        var state_counters * ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Input_PriorityGroups_PriorityGroup_State
        state_counters = priorityGroupObj.State

        if state_counters == nil  {
            log.Info("DbToYang_qos_get_one_intf_all_pg_counters_xfmr - state_counters is nil")
	        return err
        }

        state_counters.Name = &priorityGroupName

        err = populatePriorityGroupCounters(inParams, targetUriPath, oid, state_counters)

    }

    log.Info("DbToYang_qos_get_one_intf_all_pg_counters_xfmr - finished ")

    return err
}


var THRESHOLD_BREACH_COUNTER_MAP = map[string]string{
    "SAI_INGRESS_PRIORITY_GROUP_STAT_SHARED_WATERMARK_BYTES"    : "counter",
    "SAI_INGRESS_PRIORITY_GROUP_STAT_XOFF_ROOM_WATERMARK_BYTES" : "counter",
    "SAI_QUEUE_STAT_SHARED_WATERMARK_BYTES"                     : "counter",
}


var DbToYang_threshold_breach_counter_field_xfmr FieldXfmrDbtoYang = func(inParams XfmrParams) (map[string]interface{}, error) {
	result := make(map[string]interface{})
	data := (*inParams.dbDataMap)[inParams.curDb]
	log.Info("DbToYang_threshold_breach_counter_field_xfmr", data, inParams.ygRoot)

    for watermark_str, _ := range  THRESHOLD_BREACH_COUNTER_MAP {
        // try each one of the strings
        val, found := data["THRESHOLD_BREACH_TABLE"][inParams.key].Field[watermark_str] 
        if  found == true {
	        result["counter"] = val
            break
        }
    }

	return result, nil 
}
