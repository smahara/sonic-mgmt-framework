#!/usr/bin/python
#
# Copyright (c) 2019 Dell EMC Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# THIS CODE IS PROVIDED ON AN *AS IS* BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT
# LIMITATION ANY IMPLIED WARRANTIES OR CONDITIONS OF TITLE, FITNESS
# FOR A PARTICULAR PURPOSE, MERCHANTABLITY OR NON-INFRINGEMENT.
#
# See the Apache Version 2.0 License for specific language governing
# permissions and limitations under the License.
#

import os
import sys
import traceback
import pdb
import time

class Transformer(object):
    def __init__(self):
        '''
        Constructor
        '''

    @staticmethod
    def translate_to_db(path, params):
        """
        """
        print (path, params)
        return

    @staticmethod
    def translate_to_yang(self, oid):
        pass
    
def translate(path, params):
    """
    """
    Transformer().translate_to_db(path, params)

    result = {  
        "ACL_TABLE": {
	"MyACL1_ACL_IPV4": {
		"type": "L3", 
		"policy_desc": "Description for MyACL1",
		"stage": "INGRESS", 
		"ports@": "Ethernet0" 
		}, 
	"MyACL2_ACL_IPV4": {
		"type": "L3", 
		"policy_desc": "Description for MyACL2", 
		"stage": "INGRESS", 
		"ports@": "Ethernet4"
		}
        },
        "ACL_RULE": {
        "MyACL1_ACL_IPV4|RULE_1": {
		"PRIORITY": "65534", 
		"IP_PROTOCOL": "6", 
		"DSCP": "1", 
		"SRC_IP": "11.1.1.1/32", 
		"DST_IP": "21.1.1.1/32", 
		"L4_SRC_PORT": "101", 
		"L4_DST_PORT": "201", 
		"PACKET_ACTION": "FORWARD" 
		}, 
        "MyACL1_ACL_IPV4|RULE_2": {
		"PRIORITY": "65533", 
		"IP_PROTOCOL": "6", 
		"DSCP": "2", 
		"SRC_IP": "11.1.1.2/32", 
		"DST_IP": "21.1.1.2/32", 
		"L4_SRC_PORT": "102", 
		"L4_DST_PORT": "202", 
		"PACKET_ACTION": "DROP" 
		}, 
        "MyACL1_ACL_IPV4|RULE_3": {
		"PRIORITY": "65532", 
		"IP_PROTOCOL": "6", 
		"DSCP": "3", 
		"SRC_IP": "11.1.1.3/32", 
		"DST_IP": "21.1.1.3/32", 
		"L4_SRC_PORT": "103", 
		"L4_DST_PORT": "203", 
		"PACKET_ACTION": "FORWARD" 
		}, 
        "MyACL1_ACL_IPV4|RULE_4": {
		"PRIORITY": "65531", 
		"IP_PROTOCOL": "6", 
		"DSCP": "4", 
		"SRC_IP": "11.1.1.4/32", 
		"DST_IP": "21.1.1.4/32", 
		"L4_SRC_PORT": "104", 
		"L4_DST_PORT": "204", 
		"PACKET_ACTION": "DROP" 
		}, 
        "MyACL1_ACL_IPV4|RULE_5": {
		"PRIORITY": "65530", 
		"IP_PROTOCOL": "6", 
		"DSCP": "5", 
		"SRC_IP": "11.1.1.5/32", 
		"DST_IP": "21.1.1.5/32", 
		"L4_SRC_PORT": "105", 
		"L4_DST_PORT": "205", 
		"PACKET_ACTION": "FORWARD"
		}, 
        "MyACL2_ACL_IPV4|RULE_1": {
		"PRIORITY": "65534", 
		"IP_PROTOCOL": "6", 
		"DSCP": "1", 
		"SRC_IP": "12.1.1.1/32", 
		"DST_IP": "22.1.1.1/32", 
		"L4_SRC_PORT": "101", 
		"L4_DST_PORT": "201", 
		"PACKET_ACTION": "FORWARD" 
		}, 
        "MyACL2_ACL_IPV4|RULE_2": {
		"PRIORITY": "65533", 
		"IP_PROTOCOL": "6", 
		"DSCP": "2", 
		"SRC_IP": "12.1.1.2/32", 
		"DST_IP": "22.1.1.2/32", 
		"L4_SRC_PORT": "102", 
		"L4_DST_PORT": "202", 
		"PACKET_ACTION": "FORWARD" 
	        },
        "MyACL2_ACL_IPV4|RULE_3": {
		"PRIORITY": "65532", 
		"IP_PROTOCOL": "6", 
		"DSCP": "3", 
		"SRC_IP": "12.1.1.3/32", 
		"DST_IP": "22.1.1.3/32", 
		"L4_SRC_PORT": "103", 
		"L4_DST_PORT": "203", 
		"PACKET_ACTION": "FORWARD" 
	        },
        "MyACL2_ACL_IPV4|RULE_4": {
		"PRIORITY": "65531", 
		"IP_PROTOCOL": "6", 
		"DSCP": "4", 
		"SRC_IP": "12.1.1.4/32", 
		"DST_IP": "22.1.1.4/32", 
		"L4_SRC_PORT": "104", 
		"L4_DST_PORT": "204", 
		"PACKET_ACTION": "FORWARD" 
	        },
        "MyACL2_ACL_IPV4|RULE_5": {
		"PRIORITY": "65530", 
		"IP_PROTOCOL": "6", 
		"DSCP": "5", 
		"SRC_IP": "12.1.1.5/32", 
		"DST_IP": "22.1.1.5/32", 
		"L4_SRC_PORT": "105", 
		"L4_DST_PORT": "205", 
		"PACKET_ACTION": "FORWARD" 
	        }
        }
    }

    return result

def init_transformer():
    """
    """
    Transformer().translate_to_db("/x/y/z", "test")

if __name__ == '__main__':
    init_transformer()

