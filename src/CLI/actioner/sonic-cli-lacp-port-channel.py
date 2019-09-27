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
    if func.__name__ == 'get_openconfig_lacp_lacp_interfaces':
        keypath = []
    elif func.__name__ == 'get_openconfig_lacp_lacp_interfaces_interface':
        keypath = [args[1]]
    else:
       body = {}

    return keypath,body



def run(func, args):

    c = openconfig_lacp_client.Configuration()
    c.verify_ssl = False
    aa = openconfig_lacp_client.OpenconfigLacpApi(api_client=openconfig_lacp_client.ApiClient(configuration=c))

    # create a body block
    keypath, body = generate_body(func, args)

    try:
        if func.__name__ == 'get_openconfig_lacp_lacp_state_system_priority':
            template_filename = args[0]
            api_response = {
                            'openconfig-lacp:lacp': {
                                    'state': {
                                               'system-priority': 65535
                                             }
                            }
                           }
        elif func.__name__ == 'get_openconfig_lacp_lacp_interfaces':
            template_filename = args[0]
            api_response = {
                        'openconfig-lacp:lacp': {
                                    'interfaces': {
                                                    'interface': [
                                                                  {'name': "PortChannel1",
                                                                   'state': {
                                                                              'interval': "slow",
                                                                              'lacp-mode': "active",
                                                                              'system-id-mac': "90:b1:1c:f4:a8:7e",
                                                                              'system-priority': 65535
                                                                            },
                                                                    'members': {
                                                                                    'member': [
                                                                                                {
                                                                                                    'name': "Ethernet4",
                                                                                                    'state': {
                                                                                                                    'system-id': "90:b1:1c:f4:a8:7e",
                                                                                                                    'oper-key': 0,
                                                                                                                    'partner-id': "00:00:00:00:00:00",
                                                                                                                    'partner-key': 0,
                                                                                                                    'port-num': 5,
                                                                                                                    'partner-port-num': 0
                                                                                                             }
                                                                                                },
                                                                                                {
                                                                                                    'name': "Ethernet8",
                                                                                                    'state': {
                                                                                                                    'system-id': "90:b1:1c:f4:a8:7e",
                                                                                                                    'oper-key': 0,
                                                                                                                    'partner-id': "00:00:00:00:00:00",
                                                                                                                    'partner-key': 0,
                                                                                                                    'port-num': 5,
                                                                                                                    'partner-port-num': 0
                                                                                                             }
                                                                                                }
                                                                                              ]
                                                                               }
                                                                  },
                                                                  {'name': "PortChannel5",
                                                                   'state': {
                                                                              'interval': "slow",
                                                                              'lacp-mode': "active",
                                                                              'system-id-mac': "90:b1:1c:f4:a8:7e",
                                                                              'system-priority': 65535
                                                                            },
                                                                    'members': {
                                                                                    'member': [
                                                                                                {
                                                                                                    'name': "Ethernet12",
                                                                                                    'state': {
                                                                                                                    'system-id': "90:b1:1c:f4:a8:7e",
                                                                                                                    'oper-key': 0,
                                                                                                                    'partner-id': "00:00:00:00:00:00",
                                                                                                                    'partner-key': 0,
                                                                                                                    'port-num': 5,
                                                                                                                    'partner-port-num': 0
                                                                                                             }
                                                                                                },
                                                                                                {
                                                                                                    'name': "Ethernet16",
                                                                                                    'state': {
                                                                                                                    'system-id': "90:b1:1c:f4:a8:7e",
                                                                                                                    'oper-key': 0,
                                                                                                                    'partner-id': "00:00:00:00:00:00",
                                                                                                                    'partner-key': 0,
                                                                                                                    'port-num': 5,
                                                                                                                    'partner-port-num': 0
                                                                                                             }
                                                                                                }
                                                                                              ]
                                                                               }
                                                                  }

                                                                 ]
                                                  }
                                   },


                        'openconfig-interfaces:interfaces': {
                                                    'interface': [ {
                                                                        "name": "PortChannel1",
                                                                        "state": {
                                                                            "admin-status" : "up",
                                                                            "oper-status" : "down"
                                                                        }
                                                                    },
                                                                    {
                                                                        "name": "PortChannel5",
                                                                        "state": {
                                                                            "admin-status" : "up",
                                                                            "oper-status" : "down"
                                                                        }
                                                                    }
                                                                 ]

                                                }
           }
        elif func.__name__ == 'get_openconfig_lacp_lacp_interfaces_interface':
                template_filename = args[1]
                api_response = {
                            'openconfig-lacp:lacp': {
                                    'interfaces': {
                                                    'interface': [
                                                                  {'name': "PortChannel1",
                                                                   'state': {
                                                                              'interval': "slow",
                                                                              'lacp-mode': "active",
                                                                              'system-id-mac': "90:b1:1c:f4:a8:7e",
                                                                              'system-priority': 65535
                                                                            },
                                                                    'members': {
                                                                                    'member': [
                                                                                                {
                                                                                                    'name': "Ethernet4",
                                                                                                    'state': {
                                                                                                                    'system-id': "90:b1:1c:f4:a8:7e",
                                                                                                                    'oper-key': 0,
                                                                                                                    'partner-id': "00:00:00:00:00:00",
                                                                                                                    'partner-key': 0,
                                                                                                                    'port-num': 5,
                                                                                                                    'partner-port-num': 0
                                                                                                             }
                                                                                                },
                                                                                                {
                                                                                                    'name': "Ethernet8",
                                                                                                    'state': {
                                                                                                                    'system-id': "90:b1:1c:f4:a8:7e",
                                                                                                                    'oper-key': 0,
                                                                                                                    'partner-id': "00:00:00:00:00:00",
                                                                                                                    'partner-key': 0,
                                                                                                                    'port-num': 5,
                                                                                                                    'partner-port-num': 0
                                                                                                             }
                                                                                                }
                                                                                              ]
                                                                               }
                                                                  }

                                                                 ]
                                                  }
                                   },

                                'openconfig-interfaces:interfaces': {
                                                    'interface': [ {
                                                                        "name": "PortChannel1",
                                                                        "state": {
                                                                            "admin-status" : "up",
                                                                            "oper-status" : "down"
                                                                        }
                                                                    }
                                                                 ]

                                                }
           }



        show_cli_output(template_filename, api_response)
    except ApiException as e:
        print("Exception when calling OpenconfigLacpApi->%s : %s\n" %(func.__name__, e))


if __name__ == '__main__':

    pipestr().write(sys.argv)
    func = eval(sys.argv[1], globals(), openconfig_lacp_client.OpenconfigLacpApi.__dict__)

    run(func, sys.argv[2:])




