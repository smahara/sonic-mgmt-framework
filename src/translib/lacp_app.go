//////////////////////////////////////////////////////////////////////////
//
// Copyright 2019 Dell, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
//////////////////////////////////////////////////////////////////////////

package translib

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

type LacpApp struct {
	path   *PathInfo
	ygotRoot   *ygot.GoStruct
	ygotTarget *interface{}
}


func init() {

	err := register("/openconfig-lacp:lacp",
		&appInfo{appType: reflect.TypeOf(LacpApp{}),
			ygotRootType:  reflect.TypeOf(ocbinds.OpenconfigLacp_Lacp{}),
			isNative:      false })

	if err != nil {
		log.Fatal("Register LACP app module with App Interface failed with error=", err)
	}

	err = addModel(&ModelData{Name: "openconfig-lacp",
		Org: "OpenConfig working group",
		Ver: "1.0.2"})
	if err != nil {
		log.Fatal("Adding model data to app interface failed with error=", err)
	}
}

func (app *LacpApp) initialize(data appData) {
	log.Info("initialize:lacp:path =", data.path)
	pathInfo := NewPathInfo(data.path)
	*app = LacpApp{path: pathInfo, ygotRoot: data.ygotRoot, ygotTarget: data.ygotTarget}

}

func (app *LacpApp) getAppRootObject() *ocbinds.OpenconfigLacp_Lacp {
	deviceObj := (*app.ygotRoot).(*ocbinds.Device)
	return deviceObj.Lacp
}

func (app *LacpApp) translateCreate(d *db.DB) ([]db.WatchKeys, error)  {
    var err error
    var keys []db.WatchKeys
    log.Info("translateCreate:lacp:path =", app.path)

    err = errors.New("Not implemented")
    return keys, err
}

func (app *LacpApp) translateUpdate(d *db.DB) ([]db.WatchKeys, error)  {
    var err error
    var keys []db.WatchKeys
    log.Info("translateUpdate:lacp:path =", app.path)

    err = errors.New("Not implemented")
    return keys, err
}

func (app *LacpApp) translateReplace(d *db.DB) ([]db.WatchKeys, error)  {
    var err error
    var keys []db.WatchKeys
    log.Info("translateReplace:lacp:path =", app.path)

    err = errors.New("Not implemented")
    return keys, err
}

func (app *LacpApp) translateDelete(d *db.DB) ([]db.WatchKeys, error)  {
    var err error
    var keys []db.WatchKeys
    log.Info("translateDelete:lacp:path =", app.path)

    err = errors.New("Not implemented")
    return keys, err
}

func (app *LacpApp) translateGet(dbs [db.MaxDB]*db.DB) error {
	var err error
	log.Info("translateGet:lacp:path =", app.path.Template)
	return err
}


func (app *LacpApp) translateSubscribe(dbs [db.MaxDB]*db.DB, path string) (*notificationOpts, *notificationInfo, error) {
    notSupported := tlerr.NotSupportedError{Format: "Subscribe not supported", Path: path}
    return nil, nil, notSupported
}

func (app *LacpApp) processCreate(d *db.DB) (SetResponse, error)  {
    var err error

    err = errors.New("Not implemented")
    var resp SetResponse

    return resp, err
}

func (app *LacpApp) processUpdate(d *db.DB) (SetResponse, error)  {
    var err error

    err = errors.New("Not implemented")
    var resp SetResponse

    return resp, err
}

func (app *LacpApp) processReplace(d *db.DB) (SetResponse, error)  {
    var err error
    var resp SetResponse
    err = errors.New("Not implemented")

    return resp, err
}

func (app *LacpApp) processDelete(d *db.DB) (SetResponse, error)  {
    var err error
    err = errors.New("Not implemented")
    var resp SetResponse

    return resp, err
}


func (app *LacpApp) processGet(dbs [db.MaxDB]*db.DB) (GetResponse, error)  {
    var err error
    var payload []byte
    pathInfo := app.path

    log.Infof("Received GET for path %s; template: %s vars=%v", pathInfo.Path, pathInfo.Template, pathInfo.Vars)

    lacpIntfObj := app.getAppRootObject()
    targetUriPath, err := getYangPathFromUri(app.path.Path)
    log.Info("LACP processGet")
    log.Info("targetUriPath: ", targetUriPath)

    if targetUriPath == "/openconfig-lacp:lacp/interfaces" {
        log.Info("Requesting LACP information for all portchannels")
    } else if targetUriPath == "/openconfig-lacp:lacp/interfaces/interface" {
        log.Info("Requesting LACP information for portchannel")
        /* Request for a specific portchannel */
        if lacpIntfObj.Interfaces.Interface != nil && len(lacpIntfObj.Interfaces.Interface) > 0 {
            /* PortChannel name is the key */
            for ifKey, _ := range lacpIntfObj.Interfaces.Interface {
                log.Info("PortChannel Name = ", ifKey)

                cmd := exec.Command("docker", "exec", "teamd", "teamdctl", ifKey, "state", "dump")
                out, err := cmd.CombinedOutput()
                if err != nil {
		    log.Fatalf("cmd.Run() failed with %s\n", err)
	        }
	        log.Info("PortChannel state dump :  ", string(out))
            }
       }

    } else  if targetUriPath == "/openconfig-lacp:lacp/state/system-priority" {
        log.Info("GET for global LACP system priority")
    }

    return GetResponse{Payload:payload}, err

}

