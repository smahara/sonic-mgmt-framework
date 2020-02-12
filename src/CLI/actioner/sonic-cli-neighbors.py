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

import syslog as log
import sys
import cli_client as cc
from rpipe_utils import pipestr
from scripts.render_cli import show_cli_output

import urllib3
urllib3.disable_warnings()

#For interface to VRF mapping
vrfDict = {}
inputDict = {}
egressPortDict = {}

aa = cc.ApiClient()

def get_keypath(func,args):
    keypath = None
    instance = None
    body = None

    rcvdIntfName = inputDict.get('intf')
    if rcvdIntfName == None:
        rcvdIntfName = ""

    rcvdIpAddr = inputDict.get('ip')
    if rcvdIpAddr == None:
        rcvdIpAddr = ""

    rcvdFamily = inputDict.get('family')
    if rcvdFamily == None:
        rcvdFamily = ""

    rcvdForceStatus = inputDict.get('force')
    if rcvdForceStatus == None:
        rcvdForceStatus = ""

    if func == 'get_openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv4_neighbors':
        keypath = cc.Path('/restconf/data/openconfig-interfaces:interfaces/interface={name}/subinterfaces/subinterface={index}/openconfig-if-ip:ipv4/neighbors', name=rcvdIntfName, index="0")
    elif func == 'get_openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv6_neighbors':
        keypath = cc.Path('/restconf/data/openconfig-interfaces:interfaces/interface={name}/subinterfaces/subinterface={index}/openconfig-if-ip:ipv6/neighbors', name=rcvdIntfName, index="0")
    elif func == 'get_openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv4_neighbors_neighbor':
        keypath = cc.Path('/restconf/data/openconfig-interfaces:interfaces/interface={name}/subinterfaces/subinterface={index}/openconfig-if-ip:ipv4/neighbors/neighbor={ip}', name=rcvdIntfName, index="0", ip=rcvdIpAddr)
    elif func == 'get_openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv6_neighbors_neighbor':
        keypath = cc.Path('/restconf/data/openconfig-interfaces:interfaces/interface={name}/subinterfaces/subinterface={index}/openconfig-if-ip:ipv6/neighbors/neighbor={ip}',name=rcvdIntfName, index="0", ip=rcvdIpAddr)
    elif func == 'get_sonic_neigh_sonic_neigh_neigh_table':
        keypath = cc.Path('/restconf/data/sonic-neighbor:sonic-neighbor/NEIGH_TABLE')
    elif func == 'rpc_sonic_clear_neighbors':
        keypath = cc.Path('/restconf/operations/sonic-neighbor:clear-neighbors')
        body = {"sonic-neighbor:input":{"family": rcvdFamily, "force": rcvdForceStatus, "ip": rcvdIpAddr, "ifname": rcvdIntfName}}

    return keypath, body

def get_egress_port(macAddr, vlanName):
    vlanId = vlanName[len("Vlan"):]
    macAddr = macAddr.strip()

    keypath = cc.Path('/restconf/data/openconfig-network-instance:network-instances/network-instance={name}/fdb/mac-table/entries/entry={macaddress},{vlan}', name='default', macaddress=macAddr, vlan=vlanId)

    try:
        response = aa.get(keypath)
        response = response.content

        if 'openconfig-network-instance:entry' in response.keys():
                instance = response['openconfig-network-instance:entry'][0]['interface']['interface-ref']['state']['interface']

        if instance is not None:
                return instance
        return "-"

    except:
        return "-"

def isMgmtVrfEnabled():
    try:
        request = "/restconf/data/openconfig-network-instance:network-instances/network-instance=mgmt/state/enabled/"

        response = aa.get(request)
        response = response.content
        response = response.get('openconfig-network-instance:enabled')
        if response == True:
            return response
        else:
            return False

    except Exception as e:
        print "%Error: Internal error"

    return False

def build_vrf_list():
    global vrfDict
    tIntf = ("/restconf/data/sonic-interface:sonic-interface/INTERFACE/",
             "sonic-interface:INTERFACE",
             "INTERFACE_LIST",
             "portname")

    tVlanIntf = ("/restconf/data/sonic-vlan-interface:sonic-vlan-interface/VLAN_INTERFACE/",
                 "sonic-vlan-interface:VLAN_INTERFACE",
                 "VLAN_INTERFACE_LIST",
                 "vlanName")

    tPortChannelIntf = ("/restconf/data/sonic-portchannel-interface:sonic-portchannel-interface/PORTCHANNEL_INTERFACE/",
                        "sonic-portchannel-interface:PORTCHANNEL_INTERFACE",
                        "PORTCHANNEL_INTERFACE_LIST",
                        "pch_name")


    requests = [tIntf, tVlanIntf, tPortChannelIntf]

    for request in requests:
        keypath = cc.Path(request[0])

        try:
            response = aa.get(keypath)
            response = response.content

            intfsContainer = response.get(request[1])
            if intfsContainer is None:
                continue

            intfsList = intfsContainer.get(request[2])
            if intfsList is None:
                continue

            for intf in intfsList:
                portName = intf.get(request[3])
                vrfName = intf.get('vrf_name')
                if len(portName) > 0:
                    if len(vrfName) > 0:
                        vrfDict[portName] = vrfName
                    else:
                        vrfDict[portName] = ""

        except Exception as e:
            print "%Error: Internal error"

    if isMgmtVrfEnabled():
        vrfDict["eth0"] = "management"

def process_nbrs_intf(response):
    nbr_list = []
    rcvdIntfName = inputDict.get('intf')

    nbrsContainer = response.get('openconfig-if-ip:neighbors')
    if nbrsContainer is None:
        return

    nbrsList = nbrsContainer.get('neighbor')
    if nbrsList is None:
        return

    for nbr in nbrsList:
        ext_intf_name = "-"

        state = nbr.get('state')
        if state is None:
           log.syslog(log.LOG_INFO, "sonic-cli-neighbor.py: 'state' not available")
           continue

        ipAddr = state.get('ip')
        if ipAddr is None:
            log.syslog(log.LOG_INFO, "sonic-cli-neighbor.py: 'ip' not available")
            continue

        macAddr = state.get('link-layer-address')
        if macAddr is None:
            log.syslog(log.LOG_INFO, "sonic-cli-neighbor.py: 'link-layer-address' not available")
            continue

        if ifName.startswith('Vlan'):
            tmpKey = macAddr + "-" + ifName
            ext_intf_name = egressPortDict.get(tmpKey)
            if ext_intf_name is None:
                ext_intf_name = get_egress_port(macAddr, ifName)
                egressPortDict[tmpKey] = ext_intf_name

        nbr_table_entry = {'ipAddr':ipAddr,
                            'macAddr':macAddr,
                            'intfName':rcvdIntfName,
                            'extIntfName':ext_intf_name
                          }
        nbr_list.append(nbr_table_entry)

    return nbr_list

def process_sonic_nbrs(response):
    nbr_list = []
    rcvdVrfName = inputDict.get('vrf')
    rcvdIpAddr = inputDict.get('ip')
    rcvdMacAddr = inputDict.get('mac')
    rcvdFamily = inputDict.get('family')

    nbrContainer = response.get('sonic-neighbor:NEIGH_TABLE')
    if nbrContainer is None:
        return

    nbrs = nbrContainer.get('NEIGH_TABLE_LIST')
    if nbrs is None:
        return

    for nbr in nbrs:
        vrfName = ""
        ext_intf_name = "-"

        family = nbr.get('family')
        if family is None:
            return []

        if family != rcvdFamily:
            continue

        ifName = nbr.get('ifname')
        if ifName is None:
            return []

        ipAddr = nbr.get('ip')
        if ipAddr is None:
            return []

        macAddr = nbr.get('neigh')
        if macAddr is None:
            return []

        vrfName = vrfDict.get(ifName)

        if ifName.startswith('Vlan'):
            tmpKey = macAddr + "-" + ifName
            ext_intf_name = egressPortDict.get(tmpKey)
            if ext_intf_name is None:
                ext_intf_name = get_egress_port(macAddr, ifName)
                egressPortDict[tmpKey] = ext_intf_name

        nbr_table_entry = {'ipAddr':ipAddr,
                           'macAddr':macAddr,
                           'intfName':ifName,
                           'extIntfName':ext_intf_name
                        }
        if (rcvdVrfName == vrfName):
            if (rcvdMacAddr == macAddr):
                nbr_list.append(nbr_table_entry)
            elif (rcvdIpAddr == ipAddr):
                nbr_list.append(nbr_table_entry)
            elif (rcvdIpAddr is None and rcvdMacAddr is None):
                nbr_list.append(nbr_table_entry)

    return nbr_list

def process_args(args):
  global inputDict

  for arg in args:
        tmp = arg.split(":", 1)
        if tmp[1] == "":
                tmp[1] = None
        inputDict[tmp[0]] = tmp[1]

def run(func, args):
    process_args(args)

    # create a body block
    keypath, body = get_keypath(func, args)
    nbr_list = []
    try:
        if (func == 'rpc_sonic_clear_neighbors'):
            api_response = aa.post(keypath, body)
        else:
            api_response = aa.get(keypath)
    except:
        # system/network error
        print "%Error: Unable to connect to the server"

    try:
        if api_response.ok():
            response = api_response.content
        else:
            return

        if response is None:
            return

        build_vrf_list()
        if 'openconfig-if-ip:neighbors' in response.keys():
            nbr_list = process_nbrs_intf(response)
        elif 'sonic-neighbor:NEIGH_TABLE' in response.keys():
            nbr_list = process_sonic_nbrs(response)
        elif 'sonic-neighbor:output' in response.keys():
            status = response['sonic-neighbor:output']
            status = status['response']
            if (status != "Success"):
                print status
            return
        else:
            return
        if (inputDict.get('summary') == "summary"):
            show_cli_output(inputDict.get('script'), len(nbr_list))
        else:
            show_cli_output(inputDict.get('script'), nbr_list)
        return
    except Exception as e:
        print "%Error: Internal error"

if __name__ == '__main__':
    pipestr().write(sys.argv)
    run(sys.argv[1], sys.argv[2:])
