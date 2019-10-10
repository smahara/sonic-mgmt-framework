package transformer

import (
	"reflect"
        "errors"
        "translib/db"
	"translib/ocbinds"
	"translib/tlerr"
        "os/exec"

	log "github.com/golang/glog"
	"github.com/openconfig/ygot/ygot"
)

func init () {
    XlateFuncBind("DbToYang_lacp_get_specific_xfmr", DbToYang_lacp_get_specific_xfmr)
}

func getLacpRoot (s *ygot.GoStruct) *ocbinds.OpenconfigLacp_Lacp {
    deviceObj := (*s).(*ocbinds.Device)
    return deviceObj.Lacp
}


var DbToYang_lacp_get_specific_xfmr  SubTreeXfmrDbToYang = func(inParams XfmrParams) error {

    lacpIntfObj := getLacpRoot(inParams.ygRoot)
    pathInfo := NewPathInfo(inParams.uri)
    ifKey := pathInfo.Var("name")

    targetUriPath, err := getYangPathFromUri(pathInfo.Path)

    log.Infof("Received GET for path %s; template: %s vars=%v", pathInfo.Path, pathInfo.Template, pathInfo.Vars)

    if targetUriPath == "/openconfig-lacp:lacp/interfaces" {
        log.Info("Requesting LACP information for all portchannels")
    } else if targetUriPath == "/openconfig-lacp:lacp/interfaces/interface" {
        log.Info("Requesting LACP information for portchannel")
        /* Request for a specific portchannel */
        if lacpIntfObj.Interfaces.Interface != nil && len(lacpIntfObj.Interfaces.Interface) > 0 {
            /* PortChannel name is the key */
            log.Info("PortChannel Name = ", ifKey)

            cmd := exec.Command("docker", "exec", "teamd", "teamdctl", ifKey, "state", "dump")
            out, err := cmd.CombinedOutput()
            if err != nil {
	        log.Fatalf("cmd.Run() failed with %s\n", err)
	    }
	    log.Info("PortChannel state dump :  ", string(out))
       }

    }

    return err

}
