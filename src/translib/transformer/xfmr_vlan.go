package transformer

import (
        log "github.com/golang/glog"
        "strings"
        "strconv"
)

func init() {
    XlateFuncBind("YangToDb_vlan_tbl_key_xfmr", YangToDb_vlan_tbl_key_xfmr)
    XlateFuncBind("DbToYang_vlan_tbl_key_xfmr", DbToYang_vlan_tbl_key_xfmr)
}


/* YangToDB key transformer for top level network instance */
var YangToDb_vlan_tbl_key_xfmr KeyXfmrYangToDb = func(inParams XfmrParams) (string, error) {
    var vlanTbl_key  string
    var err error

    log.Info("YangToDb_vlan_table_key_xfmr: ")

    pathInfo := NewPathInfo(inParams.uri)
	ntwk_inst, _ := pathInfo.Vars["name"]

    if vlan_id, ok := pathInfo.Vars["vlan-id"]; ok {
		vlanTbl_key = "Vlan" + vlan_id;

// if network instance is vlan, return nil for other vlans.
    	if strings.HasPrefix(ntwk_inst, "Vlan") &&
    		vlanTbl_key != ntwk_inst {
    		log.Infof("vlan_tbl_key_xfmr: vlanTbl_key %s, ntwk_inst %s ", vlanTbl_key, ntwk_inst)
    		return "", err
    	}
	}

    log.Info("YangToDb_vlan_tbl_key_xfmr: key ", vlanTbl_key)
    return vlanTbl_key, err
}

/* DbToYang key transformer for top level network instance */
var DbToYang_vlan_tbl_key_xfmr KeyXfmrDbToYang = func(inParams XfmrParams) (map[string]interface{}, error) {
    res_map := make(map[string]interface{})
    var err error
    var vlanid float64

    tbl_key := inParams.key
 
    if strings.HasPrefix(tbl_key, "Vlan") {
    	tbl_key = strings.TrimPrefix(tbl_key, "Vlan")
    	if vlanid, err  = strconv.ParseFloat(tbl_key, 64); err == nil {
   	    	res_map["vlan-id"] = vlanid
   	    }
    }
   	log.Infof("DbToYang_vlan_tbl_key_xfmr: %s, %f", inParams.key, vlanid)

    return  res_map, err
}