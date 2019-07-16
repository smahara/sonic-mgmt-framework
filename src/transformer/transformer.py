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
import opcfg_mgr
from . import opcfg_mgr
from . import opcfg_trans_logger as opcfg_log


transformer_filenm = sys._getframe().f_code.co_filename # Filename, for logging


class Transformer(object):

    __instance = None
    @staticmethod
    def getInstance():
        """ Static access method. """
        if Transformer.__instance == None:
            Transformer.__instance = Transformer()
        return Transformer.__instance

    def __init__(self):
        if Transformer.__instance != None:
            raise Exception("singleton class")
        else:
            Transformer.__instance = self
            self.spec_mgr = opcfg_mgr.SpecMgr()


    #@staticmethod
    def translate_to_db(self, path, params):
        """
        """
        opcfg_log.log_dbg_msg(transformer_filenm + ":%s"%sys._getframe().f_lineno, "received path : %s, params : %s"%(path, params))
        module_nm = "openconfig-acl" # this open config yang module name should be extracted from incoming parameters
        spec_obj = self.spec_mgr.get_opcfg_spec_obj(module_nm)
        ########### following is mock code on how to use spec APIs/object  #################
        xpath = "acl/acl-sets/acl-set/name" # this will be extracted from incoming parameters
        tbl_info_dict = spec_obj.get_table_info(xpath)
        opcfg_log.log_dbg_msg(transformer_filenm + ":%s"%sys._getframe().f_lineno, "Table info dict : %s"%tbl_info_dict)
        # iterate thru tbl_info_dict to take necessrary actions
        for kidx in tbl_info_dict.keys():
            if kidx == "table_data":
                 # will fetch dictionary {'table_name':<nm>, 'table_keys':[list_key_xpaths], 'key_xfmr':<xmfr_nm>}
                 tbl_key_info_dict = spec_obj.get_table_key_info(tbl_info_dict['table_data'])
                 print("Table key info dict : %s"%tbl_key_info_dict)
                 xfmr_result = tbl_key_info_dict['key_xfmr']({"acl/acl-sets/acl-set/name":"dummy_val"})
                 print("key transformer result %s"%xfmr_result)
            if kidx == "is_key":
                print("xpath is key")
            if kidx == "field":
                # extract field list
                print("xpath is field") 
            # check for kidx == "xfmr", if yes then callback depending wheteher its field level or object level passing necessary data
        ########################################################################################
        return

    #@staticmethod
    def translate_to_yang(self, path, param):
        pass
    
def translate(path, params):
    """
    """
    print("tranlate() instance :",Transformer.getInstance())
    Transformer.getInstance().translate_to_db(path, params)

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
    xfmrObj = Transformer()
    print("init_transformer() instance ", xfmrObj.getInstance())
    return xfmrObj


if __name__ == '__main__':
    init_transformer()
    path = "test"
    params = {'acl': {
                 'acl-sets':{
                    'acl' :[] 
                 }
              }  
             }
    translate(path, params)

