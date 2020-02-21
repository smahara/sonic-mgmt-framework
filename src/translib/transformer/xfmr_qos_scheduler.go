package transformer

import (
    "strings"
    "strconv"
    "translib/db"
    log "github.com/golang/glog"
    "translib/ocbinds"
    "github.com/openconfig/ygot/ygot"
)
func init () {
    /*
    XlateFuncBind("YangToDb_qos_scheduler_policy_key_xfmr", YangToDb_qos_scheduler_policy_key_xfmr)
    XlateFuncBind("DbToYang_qos_scheduler_policy_key_xfmr", DbToYang_qos_scheduler_policy_key_xfmr)
    */
    XlateFuncBind("YangToDb_qos_scheduler_priority_xfmr", YangToDb_qos_scheduler_priority_xfmr)
    XlateFuncBind("DbToYang_qos_scheduler_priority_xfmr", DbToYang_qos_scheduler_priority_xfmr)
    XlateFuncBind("YangToDb_qos_scheduler_xfmr", YangToDb_qos_scheduler_xfmr)
    XlateFuncBind("DbToYang_qos_scheduler_xfmr", DbToYang_qos_scheduler_xfmr)
 
}


/*
var YangToDb_qos_scheduler_policy_key_xfmr KeyXfmrYangToDb = func(inParams XfmrParams) (string, error) {
    var entry_key string
    log.Info("YangToDb_qos_scheduler_policy_key_xfmr: ", inParams.ygRoot, inParams.uri)
    pathInfo := NewPathInfo(inParams.uri)

    policy_name := pathInfo.Var("name")
    sequence := pathInfo.Var("sequence")

    log.Info("YangToDb: policy name: ", policy_name, " sequence: ", sequence)

    entry_key = policy_name+"@"+sequence

    log.Info("YangToDb_qos_scheduler_policy_key_xfmr - entry_key : ", entry_key)

    return entry_key, nil 
}

var DbToYang_qos_scheduler_policy_key_xfmr KeyXfmrDbToYang = func(inParams XfmrParams) (map[string]interface{}, error) {
    rmap := make(map[string]interface{})
    entry_key := inParams.key
    log.Info("DbToYang_qos_scheduler_policy_key_xfmr: ", entry_key)

    key := strings.Split(entry_key, "@")

    rmap["sequence"], _ = strconv.Atoi(key[1])

    return rmap, nil 
}
*/




var YangToDb_qos_scheduler_priority_xfmr FieldXfmrYangToDb = func(inParams XfmrParams) (map[string]string, error) {

    qos_scheduler_priority, _ := inParams.param.(ocbinds.E_OpenconfigQos_Qos_SchedulerPolicies_SchedulerPolicy_Schedulers_Scheduler_Config_Priority)

    db_qos_scheduler_type := "WRR"
    if qos_scheduler_priority == ocbinds.OpenconfigQos_Qos_SchedulerPolicies_SchedulerPolicy_Schedulers_Scheduler_Config_Priority_STRICT {
        db_qos_scheduler_type = "PRIORITY"
    }

    log.Info( "YangToDb_qos_scheduler_priority_xfmr: type: ", db_qos_scheduler_type)
    res_map :=  make(map[string]string)
    res_map["type"] = db_qos_scheduler_type 
    return res_map, nil
}

var DbToYang_qos_scheduler_priority_xfmr FieldXfmrDbtoYang = func(inParams XfmrParams) (map[string]interface{}, error) {
    var err error
    rmap := make(map[string]interface{})
    data := (*inParams.dbDataMap)[inParams.curDb]
    db_qos_scheduler_type, ok := data["SCHEDULER"][inParams.key].Field["type"]
    if ok {
        log.Info("DbToYang_qos_scheduler_priority_xfmr: db_qos_scheduler_type: ", db_qos_scheduler_type)
        if db_qos_scheduler_type == "PRIORITY" {
            rmap["priority"] = "STRICT"
        }
    }
    return rmap, err
}




func getIntfsBySPName(sp_name string) ([]string) {
    var s []string

    log.Info("sp_name ", sp_name)

    d, err := db.NewDB(getDBOptions(db.ConfigDB))
    if err != nil {
        log.Infof("getIntfsBySPName, unable to get configDB, error %v", err)
        return s
    }


    // QUEUE
    dbSpec := &db.TableSpec{Name: "QUEUE"}

    keys, _ := d.GetKeys(dbSpec)
    for _, key := range keys {
        log.Info("key: ", key)
        qCfg, _ := d.GetEntry(dbSpec, key)
        log.Info("qCfg: ", qCfg)
        sp, ok := qCfg.Field["scheduler"] 
        if !ok {
            continue
        }
        log.Info("sp: ", sp)

        str := strings.Split(sp, "@")
        //log.Info("str: ", str)

        if str[0] == sp_name {
            //log.Info("found matching scheduler profile: ", sp_name)
            intf_name := key.Get(0)

            log.Info("intf_name added to the referenece list: ", intf_name)

            s = append(s, intf_name)  
        }
    }

    return s
}



var YangToDb_qos_scheduler_xfmr SubTreeXfmrYangToDb = func(inParams XfmrParams) (map[string]map[string]db.Value, error) {

    var err error
    res_map := make(map[string]map[string]db.Value)

    log.Info("YangToDb_qos_scheduler_xfmr: ", inParams.ygRoot, inParams.uri)
    log.Info("inParams: ", inParams)

    pathInfo := NewPathInfo(inParams.uri)
    sp_name := pathInfo.Var("name")
    seq := pathInfo.Var("sequence")

    log.Info("YangToDb: policy name: ", sp_name, " sequence: ", seq)

    /* parse the inParams */
    qosObj := getQosRoot(inParams.ygRoot)
    if qosObj == nil {
        return res_map, err
    }

    spObj, ok := qosObj.SchedulerPolicies.SchedulerPolicy[sp_name]
    if !ok {
        return res_map, err
    }
    
    seq_val, _ := strconv.ParseUint(seq, 10, 32)
    schedObj, ok := spObj.Schedulers.Scheduler[uint32(seq_val)]
    if !ok {
        return res_map, err
    }

    /* update "scheduler" table */
    sched_entry := make(map[string]db.Value)
    sched_key := sp_name+"@"+seq
    sched_entry[sched_key] = db.Value{Field: make(map[string]string)}

    if ((inParams.oper == CREATE) ||
        (inParams.oper == REPLACE) ||
        (inParams.oper == UPDATE)) {
        if schedObj.TwoRateThreeColor != nil && schedObj.TwoRateThreeColor.Config != nil {
            if schedObj.TwoRateThreeColor.Config.Bc != nil  {
                sched_entry[sched_key].Field["bc"] = strconv.Itoa((int)(*schedObj.TwoRateThreeColor.Config.Bc))
            }

            if schedObj.TwoRateThreeColor.Config.Be != nil  {
                sched_entry[sched_key].Field["be"] = strconv.Itoa((int)(*schedObj.TwoRateThreeColor.Config.Be))
            }

            if schedObj.TwoRateThreeColor.Config.Cir != nil  {
                sched_entry[sched_key].Field["cir"] = strconv.Itoa((int)(*schedObj.TwoRateThreeColor.Config.Cir))
            }

            if schedObj.TwoRateThreeColor.Config.Pir != nil  {
                sched_entry[sched_key].Field["pir"] = strconv.Itoa((int)(*schedObj.TwoRateThreeColor.Config.Pir))
            }
        }

        if schedObj.Config != nil  {
            if schedObj.Config.Priority == ocbinds.OpenconfigQos_Qos_SchedulerPolicies_SchedulerPolicy_Schedulers_Scheduler_Config_Priority_STRICT {
                sched_entry[sched_key].Field["type"] = "PRIORITY"
            }

            if schedObj.Config.Weight != nil  {
                sched_entry[sched_key].Field["weight"] = strconv.Itoa((int)(*schedObj.Config.Weight))
            }
        }
    }

    if (inParams.oper == DELETE) {
        if schedObj.Config != nil  {
            if schedObj.Config.Priority == ocbinds.OpenconfigQos_Qos_SchedulerPolicies_SchedulerPolicy_Schedulers_Scheduler_Config_Priority_UNSET {
                //log.Info("field Type is set for attribute deletion")
                sched_entry[sched_key].Field["type"] = "PRIORITY"
            }
        }
    }

    log.Info("YangToDb_qos_scheduler_xfmr - entry_key : ", sched_key)
    res_map["SCHEDULER"] = sched_entry

    /* update "Queue" table for newly created scheduler if the scheduler profile is used by intfs*/
    queueTblMap := make(map[string]db.Value)

    if inParams.oper == CREATE  || inParams.oper == UPDATE {
        // read intfs refering to the scheduler profile 
        intfs := getIntfsBySPName(sp_name)

        // Use "if_name:seq" to form DB key for QUEUE, write "if_name@seq" as its scheduler profile
        for _, if_name := range intfs {
            queueKey := if_name + "|" + seq
            db_sp_name := sp_name + "@" + seq
            log.Infof("YangToDb_qos_scheduler_xfmr --> key: %v, db_sp_name: %v", queueKey, db_sp_name)

            _, ok := queueTblMap[queueKey]
            if !ok {
                queueTblMap[queueKey] = db.Value{Field: make(map[string]string)}
            }
            queueTblMap[queueKey].Field["scheduler"] = db_sp_name
        }

        res_map["QUEUE"] = queueTblMap
    }

    return res_map, err

}

var DbToYang_qos_scheduler_xfmr SubTreeXfmrDbToYang = func(inParams XfmrParams) error {

    pathInfo := NewPathInfo(inParams.uri)

    sp_name := pathInfo.Var("name")

    log.Info("inParams: ", inParams)

    qosObj := getQosRoot(inParams.ygRoot)

    if qosObj == nil {
        ygot.BuildEmptyTree(qosObj)
    }

    spObj, ok := qosObj.SchedulerPolicies.SchedulerPolicy[sp_name]
    if !ok {
        spObj, _ = qosObj.SchedulerPolicies.NewSchedulerPolicy(sp_name)
        ygot.BuildEmptyTree(spObj)
        spObj.Name = &sp_name

        if spObj.Schedulers == nil {
            ygot.BuildEmptyTree(spObj.Schedulers)
        }
    }


    // Scheduler
    dbSpec := &db.TableSpec{Name: "SCHEDULER"}

    keys, _ := inParams.dbs[db.ConfigDB].GetKeys(dbSpec)
    log.Info("keys: ", keys)
    for  _, key := range keys {
        log.Info("current key: ", key)
        if len(key.Comp) < 1 {
            continue
        }

        s := strings.Split(key.Comp[0], "@")

        if strings.Compare(sp_name, s[0]) == 0 {
            log.Info("found matching scheduler policy in scheduler: ", s)

            var seq uint32
            tmp, _ := strconv.ParseUint(s[1], 10, 32)
            seq = (uint32) (tmp)

            schedObj, _ := spObj.Schedulers.NewScheduler(seq)
            ygot.BuildEmptyTree(schedObj)

            schedCfg, _ := inParams.dbs[db.ConfigDB].GetEntry(dbSpec, key) 
            log.Info("current entry: ", schedCfg)

            var tmp_u32 uint32
            var tmp_u8  uint8
            if val, exist := schedCfg.Field["bc"]; exist {
                tmp,_ = strconv.ParseUint(val, 10, 32)
                tmp_u32 = uint32(tmp)
                schedObj.TwoRateThreeColor.Config.Bc = &tmp_u32
            }

            if val, exist := schedCfg.Field["be"]; exist {
                tmp,_ = strconv.ParseUint(val, 10, 32)
                tmp_u32 = uint32(tmp)
                schedObj.TwoRateThreeColor.Config.Be = &tmp_u32
            }

            if val, exist := schedCfg.Field["cir"]; exist {
                tmp,_ = strconv.ParseUint(val, 10, 32)
                schedObj.TwoRateThreeColor.Config.Cir = &tmp
            }

            if val, exist := schedCfg.Field["pir"]; exist {
                tmp,_ = strconv.ParseUint(val, 10, 32)
                schedObj.TwoRateThreeColor.Config.Pir = &tmp
            }

            if val, exist := schedCfg.Field["type"]; exist {
                if val == "PRIORITY" {
                    schedObj.Config.Priority = ocbinds.OpenconfigQos_Qos_SchedulerPolicies_SchedulerPolicy_Schedulers_Scheduler_Config_Priority_STRICT
                }
            }

            if val, exist := schedCfg.Field["weight"]; exist {
                tmp,_ = strconv.ParseUint(val, 10, 32)
                tmp_u8 = uint8(tmp)
                schedObj.Config.Weight = &tmp_u8
            }

        }
    }


    log.Info("Done fetching scheduler policy: ", sp_name)
    return nil
}



