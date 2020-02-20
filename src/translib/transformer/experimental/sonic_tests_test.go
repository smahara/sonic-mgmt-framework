////////////////////////////////////////////////////////////////////////////////
//                                                                            //
//  Copyright 2019 Dell, Inc.                                                 //
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

func Test_SetTABLE(t *testing.T) {

	fmt.Println("+++++  Start sonic-tests/TABLE_A testing  +++++")

	url := "/sonic-tests:sonic-tests/TABLE_A/TABLE_A_LIST[id=14628525]"

        //Add entry
	t.Run("Add entry", processSetRequest(url, addEntryJson, "PATCH", false))
	time.Sleep(1 * time.Second)

        // Verify entry
	t.Run("Verify entry", processGetRequest(url, addEntryJson, false))

	/*
        //Set speed
	speedUrl := url + "/speed"
	t.Run("Set speed", processSetRequest(speedUrl, speedTestJson, "PATCH", false))
	time.Sleep(1 * time.Second)

        // Verify speed
	t.Run("Verify speed", processGetRequest(url, ConfigGetJsonResp, false))

        //Add collector
        url = "/sonic-sflow:sonic-sflow/SFLOW_COLLECTOR/SFLOW_COLLECTOR_LIST[collector_name=col1]"
	t.Run("Add sFlow collector col1", processSetRequest(url, col1Json, "PATCH", false))
	time.Sleep(1 * time.Second)

        // Verify collector configurations
	t.Run("Verify sFlow collector col1", processGetRequest(url, col1Json, false))

        // Set collector ip
        ipUrl := url + "/collector_ip"
	t.Run("Set sFlow collector col1 ip", processSetRequest(ipUrl, colIPJson, "PATCH", false))
	time.Sleep(1 * time.Second)

        // Set collector port
        portUrl := url + "/collector_port"
	t.Run("Set sFlow collector col1 port", processSetRequest(portUrl, colPortJson, "PATCH", false))
	time.Sleep(2 * time.Second)

        // Verify collector configurations
	t.Run("Verify_sFlow_collector", processGetRequest(url, col1ModJson, false))
	*/
}

/***************************************************************************/
///////////                  JSON Data for Tests              ///////////////
/***************************************************************************/

var addEntryJson string = "{\"sonic-tests:TABLE_A_LIST\":[{\"id\":14628525,\"ifname\":\"Ethernet0\",\"index\":14628526,\"indices\":[10,20,14628510,14628220],\"speed\":\"4444\"}]}"
var setSpeedJson string = "{\"sonic-tests:TABLE_A_LIST\": \"2.2.2.2\"}"
/*
var globalAdminJson string = "{\"sonic-sflow:admin_state\": \"up\"}"
var pollingJson string = "{\"sonic-sflow:polling_interval\": 10}"
var agentIdJson string = "{\"sonic-sflow:agent_id\": \"Ethernet0\"}"
var globalConfigGetJsonResp string = "{\"sonic-sflow:SFLOW_LIST\":[{\"admin_state\":\"up\",\"agent_id\":\"Ethernet0\",\"polling_interval\":10,\"sflow_key\":\"global\"}]}"

var col1Json string = "{\"sonic-sflow:SFLOW_COLLECTOR_LIST\":[{\"collector_ip\":\"1.1.1.1\",\"collector_name\":\"col1\",\"collector_port\":4444}]}"
var col1ModJson string = "{\"sonic-sflow:SFLOW_COLLECTOR_LIST\":[{\"collector_ip\":\"2.2.2.2\",\"collector_name\":\"col1\",\"collector_port\":1234}]}"

var colIPJson string = "{\"sonic-sflow:collector_ip\": \"2.2.2.2\"}"
var colPortJson string = "{\"sonic-sflow:collector_port\": 1234}"
*/
