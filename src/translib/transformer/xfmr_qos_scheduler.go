package transformer

import (
    "strings"
    log "github.com/golang/glog"
    "translib/ocbinds"
)
func init () {
    XlateFuncBind("YangToDb_qos_scheduler_policy_key_xfmr", YangToDb_qos_scheduler_policy_key_xfmr)
    XlateFuncBind("DbToYang_qos_scheduler_policy_key_xfmr", DbToYang_qos_scheduler_policy_key_xfmr)
    XlateFuncBind("YangToDb_qos_scheduler_priority_xfmr", YangToDb_qos_scheduler_priority_xfmr)
    XlateFuncBind("DbToYang_qos_scheduler_priority_xfmr", DbToYang_qos_scheduler_priority_xfmr)
 
}



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

    rmap["name"] = key[0]
    rmap["sequence"] = key[1]

    return rmap, nil 
}

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

