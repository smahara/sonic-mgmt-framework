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

    def get_name(self):
	device_name="TEMP{}".format(self.thermal_index)
	return (device_name)

    def get_display_name(self):
	try:
            display_name=pddf_obj.data[self.get_name()]['dev_attr']['display_name']
	except Exception as e:
            display_name=self.get_name()

        return (display_name)

    def get_temperature(self):
        output = pddf_obj.get_attr_name_output(self.get_name(), "temp1_input")
        if not output:
            return (0.0) 

        if output['status'].isalpha():
            attr_value = None
        else:
            attr_value = float(output['status'])
        
        if output['mode']=='bmc':
	    return attr_value
        else:
            return (attr_value/float(1000))


    def get_high_threshold(self):
        output = pddf_obj.get_attr_name_output(self.get_name(), "temp1_max")
        if not output:
            return (0.0)

        if output['status'].isalpha():
            attr_value = None
        else:
            attr_value = float(output['status'])

        if output['mode']=='bmc':
	    return attr_value
        else:
            return (attr_value/float(1000))


    def get_low_threshold(self):
        output = pddf_obj.get_attr_name_output(self.get_name(), "temp1_max_hyst")
        if not output:
            return (0.0)

        if output['status'].isalpha():
            attr_value = None
        else:
            attr_value = float(output['status'])
        
        if output['mode']=='bmc':
	    return attr_value
        else:
            return (attr_value/float(1000))


    def set_high_threshold(self, temperature):
        node = pddf_obj.get_path(self.get_name(), "temp1_max")
        if node is None:
            print "ERROR %s does not exist"%node
            return (0.0)
	
	cmd = "echo '%d' > %s"%(temperature * 1000, node)
	os.system(cmd) 

        return (True)


    def set_low_threshold(self, temperature):
        node = pddf_obj.get_path(self.get_name(), "temp1_max_hyst")
        if node is None:
            print "ERROR %s does not exist"%node
            return (0.0)
	cmd = "echo '%d' > %s"%(temperature * 1000, node)
        os.system(cmd)

        return (True)

    def get_temp_label(self):
	if 'bmc' in pddf_obj.data[self.get_name()].keys():
	    return None 
	else:   
            dev= pddf_obj.data[self.get_name()]
            topo_info = dev['i2c']['topo_info']
            label="%s-i2c-%d-%x" % (topo_info['dev_type'], int(topo_info['parent_bus'], 0), int(topo_info['dev_addr'], 0))
	    return (label)


    def dump_sysfs(self):
        return pddf_obj.cli_dump_dsysfs('temp-sensors')


		

#temp=ThermalUtil()
#num_temps = temp.get_num_thermals()
##temp.get_thermal_info()
#temp.show_temp_values()
