#!/usr/bin/env python

import os.path
import sys, traceback
import json
sys.path.append('/usr/share/sonic/platform/sonic_platform')
import pddfparse
import argparse

try:
    from sonic_platform_base.thermal_base import ThermalBase
except ImportError as e:
    raise ImportError(str(e) + "- required module not found")



class Thermal(ThermalBase):
    def __init__(self, index):
        global pddf_obj
        global plugin_data
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)) + '/../pddf/pd-plugin.json')) as pd:
            plugin_data = json.load(pd)

        pddf_obj = pddfparse.PddfParse()
        self.platform = pddf_obj.get_platform()

        self.thermal_index = index + 1
        self.info=[]

    #def get_name(self):
        #"""
        #Retrieves the name of the device

        #Returns:
            #string: The name of the device
        #"""

    #def get_temperature(self):
        #"""
        #Retrieves current temperature reading from thermal

        #Returns:
            #A float number of current temperature in Celsius up to nearest thousandth
            #of one degree Celsius, e.g. 30.125
        #"""
        #raise NotImplementedError


    #def get_high_threshold(self):
        #"""
        #Retrieves the high threshold temperature of thermal

        #Returns:
            #A float number, the high threshold temperature of thermal in Celsius
            #up to nearest thousandth of one degree Celsius, e.g. 30.125
        #"""
        #raise NotImplementedError

    #def get_high_threshold(self):
        #"""
        #Retrieves the high threshold temperature of thermal

        #Returns:
            #A float number, the high threshold temperature of thermal in Celsius
            #up to nearest thousandth of one degree Celsius, e.g. 30.125
        #"""
        #raise NotImplementedError

    #def get_low_threshold(self):
        #"""
        #Retrieves the low threshold temperature of thermal

        #Returns:
            #A float number, the low threshold temperature of thermal in Celsius
            #up to nearest thousandth of one degree Celsius, e.g. 30.125
        #"""
        #raise NotImplementedError

    #def set_high_threshold(self, temperature):
        #"""
        #Sets the high threshold temperature of thermal

        #Args :
            #temperature: A float number up to nearest thousandth of one degree Celsius,
            #e.g. 30.125

        #Returns:
            #A boolean, True if threshold is set successfully, False if not
        #"""
        #raise NotImplementedError

    #def set_low_threshold(self, temperature):
        #"""
        #Sets the low threshold temperature of thermal

        #Args :
            #temperature: A float number up to nearest thousandth of one degree Celsius,
            #e.g. 30.125

        #Returns:
            #A boolean, True if threshold is set successfully, False if not
        #"""
        #raise NotImplementedError

    def dump_sysfs(self):
        return pddf_obj.cli_dump_dsysfs('temp-sensors')


		

#temp=ThermalUtil()
#num_temps = temp.get_num_thermals()
##temp.get_thermal_info()
#temp.show_temp_values()
