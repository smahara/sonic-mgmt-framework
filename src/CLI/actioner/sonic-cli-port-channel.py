#!/usr/bin/python
###########################################################################
#
# Copyright 2019 Dell, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
###########################################################################

import sys
import time
import json
import ast
import openconfig_lacp_client
import sonic_portchannel_client
from sonic_portchannel_client.api.sonic_portchannel_api import SonicPortchannelApi  
from sonic_portchannel_client.rest import ApiException
import sonic_port_client
from rpipe_utils import pipestr
from openconfig_lacp_client.rest import ApiException
from scripts.render_cli import show_cli_output

import urllib3
urllib3.disable_warnings()


plugins = dict()

def register(func):
    """Register sdk client method as a plug-in"""
    plugins[func.__name__] = func
    return func


def call_method(name, args):
    method = plugins[name]
    return method(args)

def generate_body(func, args):
    body = None
    keypath = []
    if func.__name__ == 'get_sonic_portchannel_sonic_portchannel_lag_table_lag_table_list' or 'get_openconfig_lacp_lacp_interfaces_interface':
	keypath = [args[0]]
    elif func.__name__ == 'get_sonic_portchannel_sonic_portchannel_lag_table' or 'get_openconfig_lacp_lacp_interfaces':
        keypath = []
    else:
       body = {}

    return keypath,body

def getId(item):
    prfx = "Ethernet"
    state_dict = item['state']
    ifName = state_dict['name']

    if ifName.startswith(prfx):
        ifId = int(ifName[len(prfx):])
        return ifId
    return ifName

def run():

    c = sonic_portchannel_client.Configuration()
    c2 = sonic_port_client.Configuration()
    c.verify_ssl = False
    c2.verify_ssl = False
    aa = sonic_portchannel_client.SonicPortchannelApi(api_client=sonic_portchannel_client.ApiClient(configuration=c))
    aa2 = sonic_port_client.SonicPortApi(api_client=sonic_port_client.ApiClient(configuration=c2))

    c1 = openconfig_lacp_client.Configuration()
    c1.verify_ssl = False
    aa1 = openconfig_lacp_client.OpenconfigLacpApi(api_client=openconfig_lacp_client.ApiClient(configuration=c1))

    # create a body block
    if sys.argv[1] == "get_all_portchannels":
        lacp_func = 'get_openconfig_lacp_lacp_interfaces'
        portchannel_func = 'get_sonic_portchannel_sonic_portchannel_lag_table' 
    else :
        lacp_func = 'get_openconfig_lacp_lacp_interfaces_interface'
        portchannel_func = 'get_sonic_portchannel_sonic_portchannel_lag_table_lag_table_list'

    func = eval(portchannel_func, globals(), sonic_portchannel_client.SonicPortchannelApi.__dict__)
    func1 = eval(lacp_func, globals(), openconfig_lacp_client.OpenconfigLacpApi.__dict__)
    args = sys.argv[2:]

    keypath, body = generate_body(func, args)
    keypath1, body1 = generate_body(func1, args)


    try:
        if body is not None:
           api_response = getattr(aa,func.__name__)(*keypath, body=body)
        else :
           api_response = getattr(aa,func.__name__)()


        if api_response is None:
            print ("Failure in getting portchannel data")
        else:
            # Get Command Output
            api_response = aa.api_client.sanitize_for_serialization(api_response)
            print "-----------------------", api_response

        if body1 is not None:
           api_response1 = getattr(aa1,func1.__name__)(*keypath1, body=body1)
        else :
           #api_response1 = getattr(aa1,func1.__name__)(*keypath1)
            api_response1 = getattr(aa1,func1.__name__)()

        if api_response1 is None:
            print ("Failure in getting LACP data")
        else:
            # Get Command Output
            api_response1 = aa1.api_client.sanitize_for_serialization(api_response1)
            #print "------------------------------------------------", api_response1

        # Combine Outputs
        response = {"portchannel": api_response, "lacp": api_response1}
        #print response

        if sys.argv[1] == "get_all_portchannels":
            show_cli_output(sys.argv[2], response)
        else:
            show_cli_output(sys.argv[3], response)


    except ApiException as e:
        #print("Exception when calling OpenconfigInterfacesApi->%s : %s\n" %(func.__name__, e))
        if e.body != "":
            body = json.loads(e.body)
            if "ietf-restconf:errors" in body:
                 err = body["ietf-restconf:errors"]
                 if "error" in err:
                     errList = err["error"]

                     errDict = {}
                     for dict in errList:
                         for k, v in dict.iteritems():
                              errDict[k] = v

                     if "error-message" in errDict:
                         print "%Error: " + errDict["error-message"]
                         return
                     print "%Error: Transaction Failure"
                     return
            print "%Error: Transaction Failure"
        else:
            print "Failed"


if __name__ == '__main__':

    pipestr().write(sys.argv)
    run()
