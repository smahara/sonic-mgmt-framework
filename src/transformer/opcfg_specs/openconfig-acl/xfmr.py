#!/usr/bin/python

import sys
import opcfg_trans_logger as opcfg_log

acl_xfmr_filenm = sys._getframe().f_code.co_filename # Filename, for logging

# ACL callbacks
def _validate_arg(xpath_dict, func_nm):
    if not isinstance(xpath_dict, dict):
        opcfg_log.log_err_msg(acl_xfmr_filenm + ":%s"%sys._getframe().f_lineno,
                              "Input arg to %s() should be a dictionary"%func_nm)

def xfmr_ip_protocol(xpath_dict):
    return {'IP_PROTOCOL': "dummyval"}

def xfmr_source_port(xpath_dict):
    return {'SRC_IP': "dummyval"}

def xfmr_destination_port(xpath_dict):
    return {'DST_IP': "dummyval"}

def xfmr_tcp_flags(xpath_dict):
    return {'TCP_FLAGS': "dummyval"}

def xfmr_acl_table_key(xpath_dict):
    _validate_arg(xpath_dict, sys._getframe().f_code.co_name)
    #### following is mock code, replace with  actual logic
    for item in xpath_dict:
        opcfg_log.log_dbg_msg(acl_xfmr_filenm + ":%s"%sys._getframe().f_lineno, "item : %s"%item)
    return {'ACL1_IPV4': None}

def xfmr_acl_rule_table_key(xpath_dict):
    return {'ACL1_IPV4|RULE_1': None}
