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

func Test_SetRouteMap(t *testing.T) {

	fmt.Println("+++++  Start route-map testing  +++++")

	url := "/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition[name=trial]/statements/statement[name=420]/actions/config/policy-result"

        // add policy result
	t.Run("Add policy result", processSetRequest(url, addPolicyResult, "PATCH", false))
	time.Sleep(1 * time.Second)

        // Verify entry
	t.Run("Verify policy result", processGetRequest(url, addPolicyResult, false))

	url = "/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition[name=trial]/statements/statement[name=420]/actions/openconfig-bgp-policy:bgp-actions/config/set-local-pref"

        // add local preference
	t.Run("add local preference", processSetRequest(url, addLocalPreference, "PATCH", false))
	time.Sleep(1 * time.Second)

        // Verify entry
	t.Run("Verify local preference", processGetRequest(url, addLocalPreference, false))
}

/***************************************************************************/
///////////                  JSON Data for Tests              ///////////////
/***************************************************************************/

var addPolicyResult string = "{\"openconfig-routing-policy:policy-result\":\"ACCEPT_ROUTE\"}"
var addLocalPreference string = "{\"openconfig-bgp-policy:set-local-pref\":1100000}"

