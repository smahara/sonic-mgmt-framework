package transformer

import (
    "strings"
    log "github.com/golang/glog"
)
func init () {
    XlateFuncBind("YangToDb_qos_scheduler_policy_key_xfmr", YangToDb_qos_scheduler_policy_key_xfmr)
    XlateFuncBind("DbToYang_qos_scheduler_policy_key_xfmr", DbToYang_qos_scheduler_policy_key_xfmr)
 
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


