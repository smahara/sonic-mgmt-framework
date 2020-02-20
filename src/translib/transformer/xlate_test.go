////////////////////////////////////////////////////////////////////////////////
//                                                                            //
//  Copyright 2020 Dell, Inc.                                                 //
//                                                                            //
//  Licensed under the Apache License, Version 2.0 (the "License");           //
//  you may not use this file except in compliance with the License.          //
//  You may obtain a copy of the License at                                   //
//                                                                            //
//  http://www.apache.org/licenses/LICENSE-2.0                                //
//                                                                            //
//  Unless required by applicable law or agreed to in writing, software       //
//  distributed under the License is distributed on an "AS IS" BASIS,         //
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  //
//  See the License for the specific language governing permissions and       //
//  limitations under the License.                                            //
//                                                                            //
////////////////////////////////////////////////////////////////////////////////

package transformer_test

import (
	//"fmt"
	//"io/ioutil"
	//"os"
        //"os/exec"
	//"encoding/json"
	"github.com/openconfig/ygot/ygot"
	//"github.com/openconfig/ygot/ytypes"
	"reflect"
	"translib/db"
	"translib/ocbinds"
	. "translib/transformer"
	"github.com/kylelemons/godebug/pretty"

	"sync"
	"testing"
)

func Test_XlateUriToKeySpec(t *testing.T) {
	tests := []struct {
                name     string
		uri	 string
		//requestUri string
		//ygRoot   ygot.GoStruct
		rootType reflect.Type
		t	*interface{}
                txCache interface{}
                want     *[]KeySpec
		wantErr  error
        }{{
                name: "SONiC path",
                uri: "/openconfig-interfaces:interfaces/interface[name=Ethernet0]",
                //requestUri: "/openconfig-interfaces:interfaces/interface[name=Ethernet0]",
                //ygRoot:  ocbinds.Device{},
		rootType: reflect.TypeOf(ocbinds.Device{}),
		t: nil,
		txCache: new(sync.Map),
		want: &[]KeySpec{{
                        //KeySpec.dbNum:  db.ConfigDB,
                        DbNum:  db.ConfigDB,
                        Ts:	db.TableSpec{Name: "VXLAN_TUNNEL", CompCt: 0,},
                        Key:	db.Key{},
                        Child:	[]KeySpec{},
                        IgnoreParentKey: false,},
                },
		wantErr: nil,
	}}

	for _, tt := range tests {
		var deviceObj ocbinds.Device = ocbinds.Device{}
		rootIntf := reflect.ValueOf(&deviceObj).Interface()
		ygotObj := rootIntf.(ygot.GoStruct)

		got, _ := XlateUriToKeySpec(tt.uri, tt.uri, &ygotObj, tt.t, tt.txCache)
		if diff := pretty.Compare(got, tt.want); diff != "" {
                        t.Errorf("%s: XlateUriToKeySpec(%v): did not get expected set of keyspec, diff(-got,+want):\n%s", tt.name, tt.uri, diff)
                }
	}
}

func Test_GetAndXlateFromDB(t *testing.T) {
		/*
	tests := []struct {
                name     string
		uri	 string
		rootType reflect.Type
                want     []byte
		wantErr  error
        }{{
                name: "Get interface eth0",
                uri: "/openconfig-interfaces:interfaces/interface[name=Ethernet0]",
                rootType:  reflect.TypeOf(ocbinds.OpenconfigInterfaces_Interfaces{}),
		want: nil,
		wantErr: nil,
	}}

	dbs, _ := getAllDbs(true)
	for _, tt := range tests {
		var deviceObj ocbinds.Device = ocbinds.Device{}
		path, err := ygot.StringToPath(tt.uri, ygot.StructuredPath, ygot.StringSlicePath)
		if err != nil {
                        t.Errorf("%s: \n%s", tt.name, tt.uri)
		}
		ygNode, _, errYg := ytypes.GetOrCreateNode(ygSchema.RootSchema(), &deviceObj, path)
		if errYg != nil {
                        t.Errorf("%s: \n%s", tt.name, tt.uri)
		}

		rootIntf := reflect.ValueOf(&ygNode).Interface()
		ygotObj := rootIntf.(ygot.GoStruct)

		txCache := new(sync.Map)
		got, _, _ := GetAndXlateFromDB(tt.uri, &ygotObj, dbs, txCache)
		if diff := pretty.Compare(got, tt.want); diff != "" {
                        t.Errorf("%s: XlateUriToKeySpec(%v): did not get expected set of keyspec, diff(-got,+want):\n%s", tt.name, tt.uri, diff)
                }
	}
		*/
}
