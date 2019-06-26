#!/usr/bin/env python
#
# Sample pddf_psuutil file 
#
# All the supported PSU SysFS aattributes are 
#- psu_present
#- psu_model_name
#- psu_power_good
#- psu_mfr_id
#- psu_serial_num
#- psu_fan_dir
#- psu_v_out
#- psu_i_out
#- psu_p_out
#- psu_fan1_speed_rpm
#

import os.path
import sys, traceback
sys.path.append('/usr/share/sonic/platform/plugins')
import pddfparse
import json

try:
    from sonic_psu.psu_base import PsuBase
except ImportError as e:
    raise ImportError (str(e) + "- required module not found")

dirname=os.path.dirname(os.path.realpath(__file__))

with open(dirname+'/../pddf/pd-plugin.json') as pd:
    plugin_data = json.load(pd)


class PsuUtil(PsuBase):
    """Platform-specific PSUutil class"""

    def __init__(self):
        PsuBase.__init__(self)
        self.platform = pddfparse.get_platform()

    def get_num_psus(self):
        return int(self.platform['num_psus'])

    def get_psu_status(self, index):
        if index is None:
            return False

        status = 0
        device = "PSU" + "%d"%index
        node = pddfparse.get_path(device,"psu_power_good")
        try:
            with open(node, 'r') as f:
                status = f.read()
        except IOError:
            return False
        #print "Status %s"%status
        vmap = plugin_data['PSU']['psu_power_good']['valmap']

        if status.rstrip('\n') in vmap:
            return vmap[status.rstrip('\n')]
        else:
            return False

    def get_psu_presence(self, index):
        if index is None:
            return False

        status = 0
        device = "PSU" + "%d"%index
        node = pddfparse.get_path(device,"psu_present")
        try:
            with open(node, 'r') as f:
                status = f.read()
        except IOError:
            return False
        #print "Status %s"%status
        vmap = plugin_data['PSU']['psu_present']['valmap']

        if status.rstrip('\n') in vmap:
            return vmap[status.rstrip('\n')]
        else:
            return False

    def get_psu_info(self):
	total = self.get_num_psus();
        if total is None:
            return False
        print("Total number of PSUs: %d"%total)
        info_string = ""
        index = 0

	for index in range(total):
            device = "PSU"+"%d"%(index+1)
            node = pddfparse.get_path(device, "psu_power_good")
	    node_model_name = pddfparse.get_path(device, "psu_model_name")
	    node_fan_dir = pddfparse.get_path(device, "psu_fan_dir")
	    node_mfr_id = pddfparse.get_path(device, "psu_mfr_id")
	    node_serial_num = pddfparse.get_path(device, "psu_serial_num")
	    try:
		with open(node, 'r') as power_status:
		    status = int(power_status.read())
	    except IOError:
		return False

            if status == 0:
                info_string = info_string + "\n\nPSU" + str(index+1) + ": Power Not Ok\n"

	    if status == 1:
                with open(node_model_name, 'r') as model_name:
                    psu_model_name = model_name.read()
                with open(node_mfr_id, 'r') as mfr_id:
                    psu_mfr_id = mfr_id.read()
                with open(node_serial_num, 'r') as serial_num:
                    psu_serial_num = serial_num.read()
                with open(node_fan_dir, 'r') as fan_dir:
                    psu_fan_dir = fan_dir.read()
                
                psu_fan_dir = psu_fan_dir.rstrip('\n')
                vmap = plugin_data['PSU']['psu_fan_dir']['valmap']

                if psu_fan_dir in vmap:
                    psu_fan_dir_real = vmap[psu_fan_dir]
                else:
                    psu_fan_dir_real = psu_fan_dir

                info_string = info_string + "\n\nPSU" + str(index+1) + ": Power OK\n"
                info_string = info_string + "Manufacture Id:  " + psu_mfr_id
                info_string = info_string + "Model: " + psu_model_name
                info_string = info_string + "Serial Number: " + psu_serial_num
                info_string = info_string + "Fan Direction: " + psu_fan_dir_real + "\n"

        print(info_string)
        return 1


if __name__== "__main__":
    obj=PsuUtil()
    #print(obj.get_psu_status(1))
    #print(obj.get_psu_status(2))
    #print(obj.get_psu_presence(1))
    #print(obj.get_psu_presence(2))
    #obj.get_psu_info()
    #print "END\n"
