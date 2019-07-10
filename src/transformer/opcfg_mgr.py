#!/usr/bin/python

import os
import sys
import json
from opcfg_exceptions import OpcfgMgrError 
import opcfg_spec
import opcfg_trans_logger as opcfg_log

opcfg_mgr_filenm = sys._getframe().f_code.co_filename # Filename, for logging

class SpecMgr(object):

    """
    OpcfgMgr Class

    """
    def __init__(self):
        try:
            # Init opcfg object dictionary
            self.opcfg_obj_dict = {}

            # Load open config to redis mapping objects by walking the scripts directory
            dirname = os.path.dirname(__file__)
            # opcfg_log.log_dbg_msg(opcfg_mgr_filenm ":%s"%sys._getframe().f_lineno, "directory name : %s"%dirname)
            basedir = os.path.join(os.sep, dirname, 'opcfg_specs')
        
            # add each sub folder under opcfg_specs per Open Config yang
            syspath = sys.path
            for subdirname, subdirs, files in os.walk(basedir):
                for subdir in subdirs:
                    path = os.path.join(os.sep, basedir, subdir)
                    # opcfg_log.log_dbg_msg(opcfg_mgr_filenm + ":%s"%sys._getframe().f_lineno ":%s"%sys._getframe().f_lineno, "spec sys path : %s"%path)
                    sys.path = [path] + syspath
                    # opcfg_log.log_dbg_msg(opcfg_mgr_filenm + ":%s"%sys._getframe().f_lineno, "sys path after adding spec: %s"%sys.path)
                    fnames=os.listdir(path)
                    for fname in fnames:
                        # opcfg_log.log_dbg_msg(opcfg_mgr_filenm + ":%s"%sys._getframe().f_lineno , "file name: %s"%fname)
                        if fname.endswith('.json'): 
                            fname = os.path.join(os.sep, path, fname)
                            opcfg_log.log_dbg_msg(opcfg_mgr_filenm + ":%s"%sys._getframe().f_lineno, "json file name: %s"%fname)
                            with open(fname, 'r') as f:
                                try:
                                    data = json.load(f)
                                except Exception as e:
                                    opcfg_log.log_err_msg(opcfg_mgr_filenm, "Error loading json file %s, error  : %s"%(fname, e.message))
                                    raise
                                # opcfg_log.log_dbg_msg(opcfg_mgr_filenm + ":%s"%sys._getframe().f_lineno, "spec json %s"%data)
                                spec = opcfg_spec.OpcfgSpec(path,data)
                                # opcfg_log.log_dbg_msg(opcfg_mgr_filenm, "Spec obj dictionary spec name %s"%spec.module_name())
                                self.opcfg_obj_dict[spec.module_name()] = spec
                                # opcfg_log.log_dbg_msg(opcfg_mgr_filenm, "DICTIONARY%s"%self.opcfg_obj_dict)

        except:
            opcfg_log.log_exception_msg(opcfg_mgr_filenm + ":%s"%sys._getframe().f_lineno,
                                        "Failure in instantiating MibMgr class") 
            raise OpcfgMgrError

    def get_opcfg_spec_obj(self, opcfg_module_nm):
        opcfg_log.log_dbg_msg(opcfg_mgr_filenm + ":%s"%sys._getframe().f_lineno, "Module name %s"%opcfg_module_nm)
        result = None
        # opcfg_log.log_dbg_msg(opcfg_mgr_filenm + ":%s"%sys._getframe().f_lineno, "Spec object dictionary %s"%self.opcfg_obj_dict)
        if opcfg_module_nm in self.opcfg_obj_dict:
            result = self.opcfg_obj_dict[opcfg_module_nm]
        return result

    def opcfg_obj_dict(self):
        return self.opcfg_obj_dict
    

           
