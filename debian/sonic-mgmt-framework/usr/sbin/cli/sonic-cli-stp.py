#:!/usr/bin/python
import sys
import json
import openconfig_spanning_tree_client
from scripts.render_cli import show_cli_output
from openconfig_spanning_tree_client.rest import ApiException


def generate_body(func, args):
    body = None
    keypath = []
    # Get the rules of all ACL table entries.
    if func.__name__ == 'patch_openconfig_spanning_tree_stp_rapid_pvst_vlan_config_hello_time':
       keypath = [ args[0] ]
       body = { "openconfig-spanning-tree:hello-time": int(args[1]) }
    elif func.__name__ == 'patch_openconfig_spanning_tree_stp_rapid_pvst_vlan_config_forwarding_delay':
       keypath = [ args[0] ]
       body = { "openconfig-spanning-tree:forwarding-delay": int(args[1]) }
    elif func.__name__ == 'patch_openconfig_spanning_tree_stp_rapid_pvst_vlan_config_max_age':
       keypath = [ args[0] ]
       body = { "openconfig-spanning-tree:forwarding-delay": int(args[1]) }
    elif func.__name__ == 'patch_openconfig_spanning_tree_stp_rapid_pvst_vlan_config_bridge_priority':
       keypath = [ args[0] ]
       body = { "openconfig-spanning-tree:forwarding-delay": int(args[1]) }
    elif func.__name__ == 'patch_openconfig_spanning_tree_stp_global_config_enabled_protocol':
       keypath = []
       body = { "openconfig-spanning-tree:enabled-protocol": args[1] }
    elif func.__name__ == 'patch_openconfig_spanning_tree_stp_interfaces_interface_config_bpdu_guard':
       keypath = [args[1]]
       if args[2] == "True":
                body = { "openconfig-spanning-tree:bpdu-guard": True }
    elif func.__name__ == 'patch_openconfig_spanning_tree_stp_interfaces_interface_config_guard':
       keypath = [args[1]]
       if args[2] == "True":
           body = { "openconfig-spanning-tree:guard": "ROOT" }
    elif func.__name__ == 'patch_openconfig_spanning_tree_stp_interfaces_interface_config_edge_port':
       keypath = [args[1]]
       if args[2] == "True":
           body = { "openconfig-spanning-tree:edge-port": "DISABLED" }
    else:
       body = {}

    return keypath,body

def run(args):
    api_response_vlan = {
      "openconfig-spanning-tree:stp": {
        "rapid-pvst": {
          "vlan": [
           {
              "vlan-id": 20,
              "config": {
                "vlan-id": 20,
                "hello-time": 2,
                "max-age": 20,
                "forwarding-delay": 15,
                "hold-count": 3,
                "bridge-priority": 2
              },
              "state": {
                "vlan-id": 20,
                "hello-time": 3,
                "max-age": 30,
                "forwarding-delay": 8,
                "hold-count": 2,
                "bridge-priority": 0,
                "bridge-address": "00aabbaabbaa0016",
                "designated-root-priority": 0,
                "designated-root-address": "3344334433440016",
                "root-port": 0,
                "root-cost": 4,
                "hold-time": 0,
                "topology-changes": 0,
                "last-topology-change": 0
              },
              "interfaces": {
                "interface": [
                  {
                    "name": "PortChannel12",
                    "config": {
                      "name": "PortChannel12",
                      "cost": 2000,
                      "port-priority": 128
                    },
                    "state": {
                      "name": "PortChannel12",
                      "cost": 2000,
                      "port-priority": 0,
                      "port-num": 0,
                      "role": "DESIGNATED",
                      "port-state": "FORWARDING",
                      "designated-root-priority": 0,
                      "designated-root-address": "99aabbccddee0016",
                      "designated-cost": 15,
                      "designated-bridge-priority": 0,
                      "designated-bridge-address": "99aabbccddee0016",
                      "designated-port-priority": 12,
                      "designated-port-num": 0,
                      "forward-transisitions": 0,
                      "counters": {
                        "bpdu-sent": 12,
                        "bpdu-received": 130
                      }
                    }
                  },
                  {
                    "name": "Ethernet32",
                    "config": {
                      "name": "Ethernet32",
                      "cost": 20000,
                      "port-priority": 128
                    },
                    "state": {
                      "name": "Ethernet32",
                      "cost": 0,
                      "port-priority": 0,
                      "port-num": 0,
                      "role": "ALTERNATE",
                      "port-state": "BLOCKING",
                      "designated-root-priority": 0,
                      "designated-root-address": "99aabbccddee0016",
                      "designated-cost": 17,
                      "designated-bridge-priority": 0,
                      "designated-bridge-address": "99aabbccddee0016",
                      "designated-port-priority": 32,
                      "designated-port-num": 0,
                      "forward-transisitions": 0,
                      "counters": {
                        "bpdu-sent": 13,
                        "bpdu-received":31
                      }
                    }
                  }
                ]
              }
            }
          ]
        }
      }
    }
    api_response_all = {
      "openconfig-spanning-tree:stp": {
        "rapid-pvst": {
          "vlan": [
            {
              "vlan-id": 10,
              "config": {
                "vlan-id": 10,
                "hello-time": 2,
                "max-age": 20,
                "forwarding-delay": 15,
                "hold-count": 3,
                "bridge-priority": 2
              },
              "state": {
                "vlan-id": 10,
                "hello-time": 2,
                "max-age": 20,
                "forwarding-delay": 15,
                "hold-count": 3,
                "bridge-priority": 0,
                "bridge-address": "112211221122000a",
                "designated-root-priority": 0,
                "designated-root-address": "112211221122000a",
                "root-port": 0,
                "root-cost": 0,
                "hold-time": 0,
                "topology-changes": 0,
                "last-topology-change": 0
              },
              "interfaces": {
                "interface": [
                  {
                    "name": "Ethernet4",
                    "config": {
                      "name": "Ethernet4",
                      "cost": 20000,
                      "port-priority": 128
                    },
                    "state": {
                      "name": "Ethernet4",
                      "cost": 0,
                      "port-priority": 0,
                      "port-num": 0,
                      "role": "DISABLED",
                      "port-state": "DISABLED",
                      "designated-root-priority": 0,
                      "designated-root-address": "001122334455000a",
                      "designated-cost": 11,
                      "designated-bridge-priority": 0,
                      "designated-bridge-address": "001122334455000a",
                      "designated-port-priority": 4,
                      "designated-port-num": 0,
                      "forward-transisitions": 0,
                      "counters": {
                        "bpdu-sent": 11,
                        "bpdu-received": 120
                      }
                    }
                  },
                  {
                    "name": "Ethernet12",
                    "config": {
                      "name": "Ethernet12",
                      "cost": 20000,
                      "port-priority": 128
                    },
                    "state": {
                      "name": "Ethernet12",
                      "cost": 0,
                      "port-priority": 0,
                      "port-num": 0,
                      "role": "ROOT",
                      "port-state": "FORWARDING",
                      "designated-root-priority": 0,
                      "designated-root-address": "001122334455000a",
                      "designated-cost": 12,
                      "designated-bridge-priority": 0,
                      "designated-bridge-address": "001122334455000a",
                      "designated-port-priority": 12,
                      "designated-port-num": 0,
                      "forward-transisitions": 0,
                      "counters": {
                        "bpdu-sent": 41,
                        "bpdu-received":14
                      }
                    }
                  }
                ]
              }
            },
            {
              "vlan-id": 20,
              "config": {
                "vlan-id": 20,
                "hello-time": 2,
                "max-age": 20,
                "forwarding-delay": 15,
                "hold-count": 3,
                "bridge-priority": 2
              },
              "state": {
                "vlan-id": 20,
                "hello-time": 3,
                "max-age": 30,
                "forwarding-delay": 8,
                "hold-count": 2,
                "bridge-priority": 0,
                "bridge-address": "00aabbaabbaa0016",
                "designated-root-priority": 0,
                "designated-root-address": "3344334433440016",
                "root-port": 0,
                "root-cost": 4,
                "hold-time": 0,
                "topology-changes": 0,
                "last-topology-change": 0
              },
              "interfaces": {
                "interface": [
                  {
                    "name": "PortChannel12",
                    "config": {
                      "name": "PortChannel12",
                      "cost": 2000,
                      "port-priority": 128
                    },
                    "state": {
                      "name": "PortChannel12",
                      "cost": 2000,
                      "port-priority": 0,
                      "port-num": 0,
                      "role": "DESIGNATED",
                      "port-state": "FORWARDING",
                      "designated-root-priority": 0,
                      "designated-root-address": "99aabbccddee0016",
                      "designated-cost": 15,
                      "designated-bridge-priority": 0,
                      "designated-bridge-address": "99aabbccddee0016",
                      "designated-port-priority": 12,
                      "designated-port-num": 0,
                      "forward-transisitions": 0,
                      "counters": {
                        "bpdu-sent": 12,
                        "bpdu-received": 130
                      }
                    }
                  },
                  {
                    "name": "Ethernet32",
                    "config": {
                      "name": "Ethernet32",
                      "cost": 20000,
                      "port-priority": 128
                    },
                    "state": {
                      "name": "Ethernet32",
                      "cost": 0,
                      "port-priority": 0,
                      "port-num": 0,
                      "role": "ALTERNATE",
                      "port-state": "BLOCKING",
                      "designated-root-priority": 0,
                      "designated-root-address": "99aabbccddee0016",
                      "designated-cost": 17,
                      "designated-bridge-priority": 0,
                      "designated-bridge-address": "99aabbccddee0016",
                      "designated-port-priority": 32,
                      "designated-port-num": 0,
                      "forward-transisitions": 0,
                      "counters": {
                        "bpdu-sent": 13,
                        "bpdu-received":31
                      }
                    }
                  }
                ]
              }
            }
          ]
        }
      }
    }

    print ("Success")
    c = openconfig_spanning_tree_client.Configuration()
    c.verify_ssl = False
    aa = openconfig_spanning_tree_client.OpenconfigSpanningTreeApi(api_client=openconfig_spanning_tree_client.ApiClient(configuration=c))

    # create a body block
    keypath, body = generate_body(func, args)

    try:
        if body is not None:
           api_response = getattr(aa,func.__name__)(*keypath, body=body)
        else :
           api_response = getattr(aa,func.__name__)(*keypath)

        if api_response is None:
            print ("Success")
        else:
            print ("Success")
    except ApiException as e:
        print("Exception when calling OpenconfigSpanningTreeApi->%s : %s\n" %(func.__name__, e))
        return
    if (len(sys.argv) < 3):
        if api_response_all is None:
           print (" No data")
           return
        show_cli_output(sys.argv[1], api_response_all)
    else:
        if api_response_vlan is None:
           print (" No data or VLAN")
           return
        show_cli_output(sys.argv[1], api_response_vlan)
    return

if __name__ == '__main__':

    func = eval(sys.argv[1], globals(), openconfig_spanning_tree_client.OpenconfigSpanningTreeApi.__dict__)
    print sys.argv
    run(sys.argv[1:])
