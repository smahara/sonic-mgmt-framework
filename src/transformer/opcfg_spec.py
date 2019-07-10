#!/usr/bin/python

import os
import imp
import sys
import json
import collections
import pdb
import opcfg_trans_logger as opcfg_log

opcfg_spec_filenm = sys._getframe().f_code.co_filename # Filename, for logging


class OpcfgSpec(object):
    '''
    Abstract base class for opcfg specs
    '''

    def __init__(self, path, spec):
        '''
        Constructor
        '''
        # yang name/prefix 
        self._module_nm = spec['MODULE-NAME']
        self._prefix_nm = spec['PREFIX-NAME']
        xfmr_flnm = os.path.join(os.sep, path, "xfmr.py")
        py_mdlnm = imp.load_source('xfmr', xfmr_flnm)
        self._py_mdlnm = imp.load_source('xfmr', xfmr_flnm)

        # 'xpath-val': {yng_redis_mappings} } xpath to redis table info mapping
        self._yng_redis_map = {}
        self._rds_tbl_data = {} # {<table_nm>:{table_nm:<tblnm>, tbl_kys:[list of key xpaths], ky_xfmr:<key_transformer>}
        '''
        parse the spec to create the self.yng_redis_map
        '''
        self._transform_spec = spec['TRANSFORM-SPEC']['YOBJECTS']
        for yobject in self._transform_spec:
            self._process_yobject(yobject)
                
    def module_name(self):
        return self._module_nm

    def prefix_name(self):
        return self._prefix_nm

    def _process_table_info(self, yng_rds_map_ky, table_name, parent_table_orddict, yobject_key_inht = None): 
        # proc table name
        tblnm = table_name
        opcfg_log.log_dbg_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno, "Table name : %s"%tblnm)
        self._rds_tbl_data[tblnm] = { 'table_name' : tblnm,
                                      'table_keys' : [],
                                      'key_xfmr'   : ""
                                     }

        if table_name is not None:
            if parent_table_orddict is None:
                # maintain an ordered(order in which inserted) set/dict of parent tables
                parent_table_orddict = collections.OrderedDict()
            opcfg_log.log_dbg_msg(opcfg_spec_filenm+ ":%s"%sys._getframe().f_lineno, "Immediate parent table name : %s"%table_name)
            parent_table_orddict[table_name] = None 

        # from now on for rest of the children this is the new table
        table_name = tblnm
        self._yng_redis_map[yng_rds_map_ky]['table_data'] = tblnm

        # process parent table keys data based on KEYINHERITANCE json spec notation, include this under table if condition
        if parent_table_orddict is None:
            key_inht = 0
        else:
            key_inht =  len(parent_table_orddict.keys()) # this is default
        if yobject_key_inht is not None:
            key_inht = yobject_key_inht
            if key_inht > 0:
                opcfg_log.log_err_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno,
                                      "Key inheritance cannot be more than parent table dictionary length") 
                raise OpcfgkeyInheritError
            elif key_inht == 0:
                opcfg_log.log_dbg_msg(opcfg_spec_filenm, "No inheritance from any parent table") 
            elif ((len(parent_table_orddict.keys()) + (key_inht)) < 0):
                opcfg_log.log_err_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno,
                                      "Key inheritance is upto levels more than parent table dictionary length") 
                raise OpcfgkeyInheritError
            else:
                ky_idx = key_inht
                sum_keys = []
                key_list = parent_table_orddict.keys()
                while ky_idx <= 0:
                    sum_keys = self._rds_tbl_data[key_list[ky_idx]]['table_keys'] + sum_keys  
                    ky_idx = ky_idx + 1
                sum_keys = sum_keys = self._rds_tbl_data[table_name]['table_keys'] = sum_keys
                self._rds_tbl_data[table_name]['table_keys'] = sum_keys
                opcfg_log.log_dbg_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno,
                                      "Current table keys + parent table keys %s"%sum_keys) 

        opcfg_log.log_dbg_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno,
                              "Returning Table name : %s, parent_table_orddict : %s"%(table_name, parent_table_orddict))
        return table_name, parent_table_orddict

    def _process_key_info(self, tbl_key_dict, xpath_pfx, table_name):
        # process keys
	opcfg_log.log_dbg_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno, "Table key dictionary from yobject : %s"%tbl_key_dict)
	key_xpath_list = []
	for yleafy in tbl_key_dict['YLEAFY']:
	    key_xpath = xpath_pfx + "/" + yleafy
	    key_xpath_list.append(key_xpath)
	    # update the xpath in _rds_tbl_data
	    self._rds_tbl_data[table_name]['table_keys'].append(key_xpath)
	    # update the xpath in _yng_redis_map
	    self._yng_redis_map[key_xpath] = {}
	    self._yng_redis_map[key_xpath]['table_data'] = table_name
	    # update the key flag in _yng_redis_map
	    self._yng_redis_map[key_xpath]['is_key'] = True
	# update the transformer info
	if 'TRANSFORMER' in tbl_key_dict:
            xfmr_nm = tbl_key_dict['TRANSFORMER']
            try:
	        self._rds_tbl_data[table_name]['key_xfmr'] = getattr(self._py_mdlnm, xfmr_nm)
            except AttributeError:
                opcfg_log.log_dbg_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno, "Key transformer %s not found in xfmr.py"%xfmr_nm)
	opcfg_log.log_dbg_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno,
                              "Table(%s) key info : %s"%(table_name, self._rds_tbl_data[table_name]))
        return

    def _process_field_info(self, tbl_fields, xpath_pfx, table_name):
        # process fields
	opcfg_log.log_dbg_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno, "fields from spec : %s"%tbl_fields)
	for field in tbl_fields:
	    # @todo  enhance to handle multiple xpath to one redis field case later
	    field_xpath = xpath_pfx + "/" + field['YLEAFY'][0]

	    # update the xpath in _yng_redis_map and corresponding table data
	    self._yng_redis_map[field_xpath] = {}
	    self._yng_redis_map[field_xpath]['table_data'] = table_name

	    # update the redis field(s) name in _yng_redis_map 
	    if "FIELD-NAME" in field.keys():
		rds_field_name_list = field['FIELD-NAME']
	    else:
		# @todo  enhance to handle multiple xpath to one redis field case later
		rds_field_name_list = field['YLEAFY'][0]
            opcfg_log.log_dbg_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno, "redis field names: %s"%rds_field_name_list)
	    self._yng_redis_map[field_xpath]['field'] = rds_field_name_list 
	   
	    # update the transformer info
	    if "TRANSFORMER" in field:
                xfmr_nm = field['TRANSFORMER']
                try:
		    self._yng_redis_map[field_xpath]['xfmr'] = getattr(self._py_mdlnm, xfmr_nm) 
                except AttributeError:
                    opcfg_log.log_dbg_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno, "field transformer %s not found in xfmr.py"%xfmr_nm)
        return 

    def get_table_info(self, xpath):
        opcfg_log.log_dbg_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno, "received xpath : %s"%xpath)
        opcfg_log.log_dbg_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno, "yang to redis map : %s"%self._yng_redis_map)
        try:
            result = self._yng_redis_map[xpath]    
        except KeyError:
            opcfg_log.log_err_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno, "xpath doesn't exist in the map")
            result = {}
        opcfg_log.log_dbg_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno, "returning : %s"%result)
        return result

    def get_table_key_info(self, table_nm):
        opcfg_log.log_dbg_msg(opcfg_spec_filenm+ ":%s"%sys._getframe().f_lineno, "received table name : %s"%table_nm)
        # opcfg_log.log_dbg_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno, "redis table info dictionary : %s"%self._rds_tbl_data)
        try:
            result = self._rds_tbl_data[table_nm]    
        except KeyError:
            opcfg_log.log_err_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno, "table name doesn't exist in table key info dictionary")
            result = {}
        opcfg_log.log_dbg_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno, "returning : %s"%result)
        return result

    def _process_yobject(self, yobject, xpath_pfx=None, table_name=None, parent_table_orddict=None):
        # parse the spec to create dictionary of xpaths as keys and corresponding redis mapping as value dictionary
        # proc xpath
        opcfg_log.log_dbg_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno, "\n\n ********************************")
        #opcfg_log.log_dbg_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno, "xpath prefix : %s"%xpath_pfx)
        #opcfg_log.log_dbg_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno, "yobject : %s"%yobject)
        if xpath_pfx is None:
            yng_rds_map_ky = yobject['YOBJECT']
        else:
            yng_rds_map_ky = xpath_pfx + "/" + yobject['YOBJECT']
        #opcfg_log.log_dbg_msg(opcfg_spec_filenm, "yang-redis map key/XPATH : %s"%yng_rds_map_ky)
        xpath_pfx = yng_rds_map_ky

        self._yng_redis_map[yng_rds_map_ky] = {}
        
        # check if object level transformer
        if ((len(yobject.keys()) == 2) and ("TRANSFORMER" in yobject.keys())):
            #opcfg_log.log_dbg_msg(opcfg_spec_filenm, "Object level transformer found")
            # add transformer to _yng_redis_map
            xfmr_nm = yobject['TRANSFORMER']
            try:
                self._yng_redis_map[yng_rds_map_ky]['xfmr'] = getattr(self._py_mdlnm, xfmr_nm)
            except AttributeError:
                opcfg_log.log_dbg_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno, "Object level transformer %s not found in xfmr.py"%xfmr_nm)

        # proc table name
        if "TABLE-NAME" in yobject.keys():
           tblnm = yobject['TABLE-NAME']
           if "KEY-INHERITANCE" in yobject.keys():
               yobject_key_inht = yobject['KEY-INHERITANCE']
           else:
               yobject_key_inht = None
           table_name, parent_table_orddict = self._process_table_info(yng_rds_map_ky, tblnm, parent_table_orddict, yobject_key_inht)
               
        # process keys
        if "KEY" in yobject.keys():
            tbl_key_dict = yobject['KEY']
            self._process_key_info(tbl_key_dict, xpath_pfx, table_name)

        # process fields
        if "FIELDS" in yobject.keys():
            tbl_fields = yobject['FIELDS']
            self._process_field_info(tbl_fields, xpath_pfx, table_name)
                   

        # proc child objects
        if "YCHILDOBJECTS" in yobject.keys():
            for yobject in yobject['YCHILDOBJECTS']:
                """
                opcfg_log.log_dbg_msg(opcfg_spec_filenm,
                                  "Calling" +
                                  "_process_yobject(%s, %s, %s, %s)"%(yobject, yng_rds_map_ky, table_name, parent_table_orddict)) 
                """
                self._process_yobject(yobject, yng_rds_map_ky, table_name, parent_table_orddict)

        # return happens with all child obects processed     
        opcfg_log.log_dbg_msg(opcfg_spec_filenm + ":%s"%sys._getframe().f_lineno, "Returning for xpath %s"%yng_rds_map_ky)
        return

