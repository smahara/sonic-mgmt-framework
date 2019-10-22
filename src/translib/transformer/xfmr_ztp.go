package transformer

import (
    //"fmt"
    //"bytes"
    //"errors"
    //"strings"
    //"strconv"
    //"reflect"
    //"regexp"
    //"net"
    //"translib/tlerr"
    //"github.com/openconfig/ygot/ygot"
    //"translib/db"
    log "github.com/golang/glog"
    //"translib/ocbinds"
    //"bufio"
    //"os"
    //"github.com/openconfig/ygot/ytypes"
)


func init () {
    XlateFuncBind("DbToYang_ztp_status_xfmr", DbToYang_ztp_status_xfmr)
    XlateFuncBind("DbToYang_ztp_enable_xfmr", DbToYang_ztp_enable_xfmr)
    XlateFuncBind("DbToYang_ztp_disable_xfmr",DbToYang_ztp_disable_xfmr)

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

var DbToYang_ztp_status_xfmr SubTreeXfmrDbToYang = func (inParams XfmrParams) (error) {

    log.Info("TableXfmrFunc - Uri ZTP: ", inParams.uri);
    pathInfo := NewPathInfo(inParams.uri)

    targetUriPath, err := getYangPathFromUri(pathInfo.Path)
    log.Info("TARGET URI PATH ZTP:", targetUriPath)
    return err;
}
