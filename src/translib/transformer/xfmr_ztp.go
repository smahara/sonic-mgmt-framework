package transformer

import (
    //"fmt"
    //"bytes"
    //"errors"
    //"strings"
    //"strconv"
    "reflect"
    //"regexp"
    //"net"
    //"translib/tlerr"
    "github.com/openconfig/ygot/ygot"
    //"translib/db"
    log "github.com/golang/glog"
    "translib/ocbinds"
    //"bufio"
    //"os"
    //"github.com/openconfig/ygot/ytypes"
)


func init () {
    XlateFuncBind("DbToYang_ztp_status_xfmr", DbToYang_ztp_status_xfmr)
    XlateFuncBind("DbToYang_ztp_enable_xfmr", DbToYang_ztp_enable_xfmr)
    XlateFuncBind("DbToYang_ztp_disable_xfmr",DbToYang_ztp_disable_xfmr)

}

func getZtpRoot (s *ygot.GoStruct) *ocbinds.OpenconfigZtp_Ztp {
    deviceObj := (*s).(*ocbinds.Device)
    return deviceObj.Ztp
}
/*func getConfigSection(sectionName string, oneCfgSection *ocbinds.OpenconfigZtp_Ztp_ZtpStatus_CONFIG_SECTION_LIST) {

}
*/

func getZtpStatusInfofromDb( statusObj *ocbinds.OpenconfigZtp_Ztp_ZtpStatus) (error) {

    act := new(string)
    *act =  "ZTP Service is not running"
    statusObj.ActivityString =  act
    admin := new(bool)
    *admin =  true
    statusObj.AdminMode =  admin
    jsonver := new(string)
    *jsonver = "1.0"
    statusObj.Jsonversion = jsonver
    rt := new(string)
    *rt = "05m 31s"
    statusObj.Runtime = rt
    serv := new (string)
    *serv =  "Inactive"
    statusObj.Service = serv
    sour := new (string)
    *sour = "dhcp-opt67 (eth0)"
    statusObj.Source = sour
    st := new(string)
    *st = "SUCCESS"
    statusObj.Status = st
    ts := new (string)
    *ts = "2019-09-11 19:12:24 UTC"
    statusObj.Timestamp = ts
    /*section := []string{"Config-db-json","connectivity-check"}
    log.Info("ZTP",section[0],section[1])
    for i := 0; i < 2; i++ {
        oneCfgList, err :=statusObj.NewCONFIG_SECTION_LIST(section[i])
	if err != nil {
                log.Info("Creation of subsectionlist subtree failed!")
                return err
            }
            ygot.BuildEmptyTree(oneCfgList)

    }*/
    return nil;
}


var DbToYang_ztp_status_xfmr SubTreeXfmrDbToYang = func (inParams XfmrParams) (error) {

    ztpObj := getZtpRoot(inParams.ygRoot)
    pathInfo := NewPathInfo(inParams.uri)
    targetUriPath, err := getYangPathFromUri(pathInfo.Path)

    log.Info("TARGET URI PATH ZTP:", targetUriPath)
    log.Info("TableXfmrFunc - Uri ZTP: ", inParams.uri);
    log.Info("type of ZTP-ROOT OBJECT:",reflect.TypeOf(ztpObj))
    statusObj := ztpObj.ZtpStatus
    if  statusObj != nil {
       log.Info("ztp status obj not nil")
    }else  {
        log.Info("ztp status obj is nil")
    }
    //ygot.BuildEmptyTree(statusObj)
    log.Info("type of ZTP-status OBJECT:",reflect.TypeOf(statusObj))
    err =  getZtpStatusInfofromDb(statusObj)
    log.Info("done getztp status info from func() ZTP: ", err);
    return err

}


var DbToYang_ztp_enable_xfmr SubTreeXfmrDbToYang = func (inParams XfmrParams) (error) {

    log.Info("TableXfmrFunc - Uri ZTP: ", inParams.uri);
    pathInfo := NewPathInfo(inParams.uri)

    targetUriPath, err := getYangPathFromUri(pathInfo.Path)
    log.Info("TARGET URI PATH ZTP:", targetUriPath)
    return err;


}
var DbToYang_ztp_disable_xfmr SubTreeXfmrDbToYang = func (inParams XfmrParams) (error) {

    log.Info("TableXfmrFunc - Uri ZTP: ", inParams.uri);
    pathInfo := NewPathInfo(inParams.uri)

    targetUriPath, err := getYangPathFromUri(pathInfo.Path)
    log.Info("TARGET URI PATH ZTP:", targetUriPath)
    return err;


}


