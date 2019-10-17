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
import openconfig_interfaces_client
import openconfig_lacp_client
from rpipe_utils import pipestr
from openconfig_interfaces_client.rest import ApiException
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
    if func.__name__ == 'get_openconfig_interfaces_interfaces_interface' or 'get_openconfig_lacp_lacp_interfaces_interface':
	keypath = [args[0]]
    elif func.__name__ == 'get_openconfig_interfaces_interfaces' or 'get_openconfig_lacp_lacp_interfaces':
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

    """
    c = openconfig_interfaces_client.Configuration()
    c.verify_ssl = False
    aa = openconfig_interfaces_client.OpenconfigInterfacesApi(api_client=openconfig_interfaces_client.ApiClient(configuration=c))
    """

    c1 = openconfig_lacp_client.Configuration()
    c1.verify_ssl = False
    aa1 = openconfig_lacp_client.OpenconfigLacpApi(api_client=openconfig_lacp_client.ApiClient(configuration=c1))

    # create a body block

    """
    func = eval(sys.argv[1], globals(), openconfig_interfaces_client.OpenconfigInterfacesApi.__dict__)
    args = sys.argv[2:]
    keypath, body = generate_body(func, args)
    """


    if sys.argv[1] == "get_all_portchannels":
        lacp_func = 'get_openconfig_lacp_lacp_interfaces'
    else :
        lacp_func = 'get_openconfig_lacp_lacp_interfaces_interface'

    func1 = eval(lacp_func, globals(), openconfig_lacp_client.OpenconfigLacpApi.__dict__)

    args = sys.argv[2:]
    keypath1, body1 = generate_body(func1, args)


    try:
        """
        if body is not None:
           api_response = getattr(aa,func.__name__)(*keypath, body=body)
        else :
           api_response = getattr(aa,func.__name__)(*keypath)


        if api_response is None:
            print ("Success")
        else:
            # Get Command Output
            api_response = aa.api_client.sanitize_for_serialization(api_response)
            if 'openconfig-interfaces:interfaces' in api_response:
                value = api_response['openconfig-interfaces:interfaces']
                if 'interface' in value:
                    tup = value['interface']
                    value['interface'] = sorted(tup, key=getId)
        """

        if body1 is not None:
           api_response1 = getattr(aa1,func1.__name__)(*keypath1, body=body1)
        else :
           api_response1 = getattr(aa1,func1.__name__)()

        #print "------------------------------------------------", api_response1
        if sys.argv[1] == "get_all_portchannels":
            show_cli_output(sys.argv[2], api_response1)
        else:
            show_cli_output(sys.argv[3], api_response1)


        """
        if api_response1 is None:
            print ("Success")
        else:
            # Get Command Output
            # Combine responses
            print api_response, api_response1
        """ 

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
