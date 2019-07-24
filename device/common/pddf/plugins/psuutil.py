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

pddf_obj = pddfparse.PddfParse()

class PsuUtil(PsuBase):
    """PDDF generic PSU util class"""

    def __init__(self):
        PsuBase.__init__(self)
        self.platform = pddf_obj.get_platform()

    def get_num_psus(self):
        return int(self.platform['num_psus'])

    def get_psu_status(self, index):
        if index is None:
            return False

        status = 0
        device = "PSU" + "%d"%index
        node = pddf_obj.get_path(device,"psu_power_good")
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
        node = pddf_obj.get_path(device,"psu_present")
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

    def get_mfr_info(self, idx):
        if idx is None:
            return None

        if idx<1 or idx>self.platform['num_psus']:
            print "Invalid index %d\n"%idx
            return None

        info_string = ""
        device = "PSU"+"%d"%(idx)
        node = pddf_obj.get_path(device, "psu_power_good")
        node_model_name = pddf_obj.get_path(device, "psu_model_name")
        node_fan_dir = pddf_obj.get_path(device, "psu_fan_dir")
        node_mfr_id = pddf_obj.get_path(device, "psu_mfr_id")
        node_serial_num = pddf_obj.get_path(device, "psu_serial_num")
        try:
            with open(node, 'r') as power_status:
                status = int(power_status.read())
        except IOError:
            return None

        if status == 0:
            info_string = info_string + "\n\nPSU" + str(idx) + ": Power Not Ok\n"
        elif status == 1:
            try:
                with open(node_model_name, 'r') as model_name:
                    psu_model_name = model_name.read()
                with open(node_mfr_id, 'r') as mfr_id:
                    psu_mfr_id = mfr_id.read()
                with open(node_serial_num, 'r') as serial_num:
                    psu_serial_num = serial_num.read()
                with open(node_fan_dir, 'r') as fan_dir:
                    psu_fan_dir = fan_dir.read()
            except IOError:
                return None
                
            psu_fan_dir = psu_fan_dir.rstrip('\n')
            vmap = plugin_data['PSU']['psu_fan_dir']['valmap']

            if psu_fan_dir in vmap:
                psu_fan_dir_real = vmap[psu_fan_dir]
            else:
                psu_fan_dir_real = psu_fan_dir

            info_string = info_string + "\n\nPSU" + str(idx) + ": Power OK\n"
            info_string = info_string + "Manufacture Id:  " + psu_mfr_id
            info_string = info_string + "Model: " + psu_model_name
            info_string = info_string + "Serial Number: " + psu_serial_num
            info_string = info_string + "Fan Direction: " + psu_fan_dir_real + "\n"


        return info_string

    def get_output_voltage(self, idx):
        if idx is None:
            return 0

        if idx<1 or idx>self.platform['num_psus']:
            print "Invalid index %d\n"%idx
            return 0

        device = "PSU"+"%d"%(idx)
        node = pddf_obj.get_path(device, "psu_v_out")
        try:
            with open(node, 'r') as f:
                v_out = int(f.read())
        except IOError:
            return 0

        return v_out

    def get_output_current(self, idx):
        if idx is None:
            return 0

        if idx<1 or idx>self.platform['num_psus']:
            print "Invalid index %d\n"%idx
            return 0

        device = "PSU"+"%d"%(idx)
        node = pddf_obj.get_path(device, "psu_i_out")
        try:
            with open(node, 'r') as f:
                i_out = int(f.read())
        except IOError:
            return 0

        return i_out

    def get_output_power(self, idx):
        if idx is None:
            return 0

        if idx<1 or idx>self.platform['num_psus']:
            print "Invalid index %d\n"%idx
            return 0

        device = "PSU"+"%d"%(idx)
        node = pddf_obj.get_path(device, "psu_p_out")
        try:
            with open(node, 'r') as f:
                p_out = int(f.read())
        except IOError:
            return 0

        return p_out

    def get_fan_rpm(self, idx, fan_idx):
        if idx is None or fan_idx is None:
            return 0

        if idx<1 or idx>self.platform['num_psus']:
            print "Invalid index %d\n"%idx
            return 0


        device = "PSU"+"%d"%(idx)
        num_fans = pddf_obj.get_num_psu_fans(device)

        if fan_idx<1 or fan_idx>num_fans:
            print "Invalid PSU-fan index %d\n"%fan_idx
            return 0

        node = pddf_obj.get_path(device, "psu_fan"+str(fan_idx)+"_speed_rpm")
        try:
            with open(node, 'r') as f:
                fan_rpm = int(f.read())
        except IOError:
            return 0

        return fan_rpm


    def dump_sysfs(self):
        return pddf_obj.cli_dump_dsysfs('psu')

#if __name__== "__main__":
    #obj=PsuUtil()
    #print(obj.get_psu_status(1))
    #print(obj.get_psu_status(2))
    #print(obj.get_psu_presence(1))
    #print(obj.get_psu_presence(2))
    #print "END\n"
