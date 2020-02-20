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
	"fmt"
	"time"
	"testing"
)

func Test_ConfigInterfaces(t *testing.T) {

	fmt.Println("+++++  Start ConfigInterfaces testing  +++++")

	url := "/openconfig-interfaces:interfaces/interface[name=Ethernet0]"

        // configure mtu
	mtuUrl := url + "/config/mtu"
	t.Run("configure mtu", processSetRequest(mtuUrl, configMtu, "PATCH", false))
	time.Sleep(1 * time.Second)

	t.Run("Verify result", processGetRequest(mtuUrl, configMtu, false))

}

/***************************************************************************/
///////////                  JSON Data for Tests              ///////////////
/***************************************************************************/

var configMtu string = "{\"openconfig-interfaces:mtu\":1500}"

