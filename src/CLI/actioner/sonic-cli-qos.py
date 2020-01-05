#!/usr/bin/python
import sys
import time
import json
import ast
import cli_client as cc
from collections import OrderedDict
from scripts.render_cli import show_cli_output
from rpipe_utils import pipestr

def invoke(func, args=[]):
    api = cc.ApiClient()
    if func == 'get_openconfig_qos_qos_interfaces_interface_output_queues_queue_state':
        path = cc.Path('/restconf/data/openconfig-qos:qos/interfaces/interface={interface_id}/output/queues/queue={name}/state', interface_id=args[0], name=args[1] )
        return api.get(path)
    if func == 'get_openconfig_qos_qos_interfaces_interface_output_queues':
        path = cc.Path('/restconf/data/openconfig-qos:qos/interfaces/interface={interface_id}/output/queues', interface_id=args[0])
        return api.get(path)
    if func == 'get_openconfig_qos_ext_qos_interfaces_interface_input_priority_groups':
        path = cc.Path('/restconf/data/openconfig-qos:qos/interfaces/interface={interface_id}/input/openconfig-qos-ext:priority-groups', interface_id=args[0])
        return api.get(path)
    if func == 'get_openconfig_qos_qos_interfaces':
        path = cc.Path('/restconf/data/openconfig-qos:qos/interfaces')
        return api.get(path)
    if func == 'get_list_openconfig_qos_ext_qos_threshold_breaches_breach':
        path = cc.Path('/restconf/data/openconfig-qos:qos/openconfig-qos-ext:threshold-breaches/breach')
        return api.get(path)
    return api.cli_not_implemented(func)


def run(func, args):

    response = invoke(func, args)

    if response.ok():
        if response.content is not None:
            api_response = response.content
            
            #print api_response
            #print sys.argv[2:]
            if 'openconfig-qos:state' in api_response:
                value = response['openconfig-qos:state']
                if value is None:
                    return
                show_cli_output(sys.argv[4], value)
            elif 'openconfig-qos:queues' in api_response:
                    value = response['openconfig-qos:queues']
                    if value is None:
                        return
                    show_cli_output(sys.argv[3], value)
            elif 'openconfig-qos:interfaces' in api_response:
                    value = response['openconfig-qos:interfaces']
                    if value is None:
                        return
                    show_cli_output(sys.argv[2], value)
            elif 'openconfig-qos-ext:priority-groups' in api_response:
                    value = response['openconfig-qos-ext:priority-groups']
                    if value is None:
                        return
                    show_cli_output(sys.argv[3], value)
            elif 'openconfig-qos-ext:breach' in api_response:
                    value = response['openconfig-qos-ext:breach']
                    if value is None:
                        return
                    show_cli_output(sys.argv[2], value)

    else:
        print response.error_message()



if __name__ == '__main__':
    pipestr().write(sys.argv)
    func = sys.argv[1]
    run(func, sys.argv[2:])
