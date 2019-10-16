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
sys.path.append('/usr/share/sonic/platform/sonic_platform')
import pddfparse
import json

try:
    from sonic_platform_base.psu_base import PsuBase
    from sonic_platform.fan import Fan
except ImportError as e:
    raise ImportError (str(e) + "- required module not found")


class Psu(PsuBase):
    """PDDF generic PSU util class"""

    color_map = {
         "STATUS_LED_COLOR_GREEN" : "on",
         "STATUS_LED_COLOR_RED" : "faulty",
         "STATUS_LED_COLOR_OFF" : "off"
    }


    def __init__(self, index):
        PsuBase.__init__(self)
        global pddf_obj
        global plugin_data
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)) + '/../pddf/pd-plugin.json')) as pd:
            plugin_data = json.load(pd)

        pddf_obj = pddfparse.PddfParse()
        self.platform = pddf_obj.get_platform()
        self.psu_index = index + 1
        
        self._fan_list = []     # _fan_list under PsuBase class is a global variable, hence we need to use _fan_list per class instatiation
        self.num_psu_fans = int(pddf_obj.get_num_psu_fans('PSU{}'.format(index+1)))
        for psu_fan_idx in range(self.num_psu_fans):
            psu_fan = Fan(psu_fan_idx, True, self.psu_index)
            self._fan_list.append(psu_fan)

    def get_num_fans(self):
        """
        Retrieves the number of fan modules available on this PSU

        Returns:
            An integer, the number of fan modules available on this PSU
        """
        return len(self._fan_list)

    def get_name(self):
        """
        Retrieves the name of the device

        Returns:
            string: The name of the device
        """
        if 'name' in plugin_data['PSU']:
            for fname in plugin_data['PSU']['name']:
                return fname[str(self.psu_index)]
        else:
            return "PSU{}".format(self.psu_index)

    def get_presence(self):
        """
        Retrieves the presence of the device

        Returns:
            bool: True if device is present, False if not
        """
        status = 0
        device = "PSU{}".format(self.psu_index)
        node = pddf_obj.get_path(device, "psu_present")
        if node is None:
            return False
        try:
            with open(node, 'r') as f:
                status = f.read()
        except IOError:
            return False
        vmap = plugin_data['PSU']['psu_present']['valmap']

        if status.rstrip('\n') in vmap:
            return vmap[status.rstrip('\n')]
        else:
            return False

    def get_model(self):
        """
        Retrieves the model number (or part number) of the device

        Returns:
            string: Model/part number of device
        """
        device = "PSU{}".format(self.psu_index)
        node = pddf_obj.get_path(device, "psu_model_name")
        if node is None:
            return None
        try:
            with open(node, 'r') as f:
                model = f.read()
        except IOError:
            return None

        return model.rstrip('\n')

    def get_serial(self):
        """
        Retrieves the serial number of the device

        Returns:
            string: Serial number of device
        """
        device = "PSU{}".format(self.psu_index)
        node = pddf_obj.get_path(device, "psu_serial_num")
        if node is None:
            return None
        try:
            with open(node, 'r') as f:
                serial = f.read()
        except IOError:
            return None

        return serial.rstrip('\n')

    def get_status(self):
        """
        Retrieves the operational status of the device

        Returns:
            A boolean value, True if device is operating properly, False if not
        """
        device = "PSU{}".format(self.psu_index)
        node = pddf_obj.get_path(device,"psu_power_good")
        if node is None:
            return False
        try:
            with open(node, 'r') as f:
                status = f.read()
        except IOError:
            return False
        vmap = plugin_data['PSU']['psu_power_good']['valmap']

        if status.rstrip('\n') in vmap:
            return vmap[status.rstrip('\n')]
        else:
            return False

    def get_mfr_id(self):
        """
        Retrieves the manufacturer id of the device

        Returns:
            string: Manufacturer Id of device
        """
        device = "PSU{}".format(self.psu_index)
        node = pddf_obj.get_path(device, "psu_mfr_id")
        if node is None:
            return None
        try:
            with open(node, 'r') as f:
                mfr = f.read()
        except IOError:
            return None

        return mfr.rstrip('\n')

    def get_voltage(self):
        """
        Retrieves current PSU voltage output

        Returns:
            A float number, the output voltage in volts,
            e.g. 12.1
        """
        device = "PSU{}".format(self.psu_index)        
        node = pddf_obj.get_path(device, "psu_v_out")
        if node is None:
            return 0.0
        try:
            with open(node, 'r') as f:
                v_out = int(f.read())
        except IOError:
            return 0.0

        return float(v_out)/1000

    def get_current(self):
        """
        Retrieves present electric current supplied by PSU

        Returns:
            A float number, electric current in amperes,
            e.g. 15.4
        """
        device = "PSU{}".format(self.psu_index)
        node = pddf_obj.get_path(device, "psu_i_out")
        if node is None:
            return 0.0
        try:
            with open(node, 'r') as f:
                i_out = int(f.read())
        except IOError:
            return 0.0

        return float(i_out)/1000

    def get_power(self):
        """
        Retrieves current energy supplied by PSU

        Returns:
            A float number, the power in watts,
            e.g. 302.6
        """
        device = "PSU{}".format(self.psu_index)
        node = pddf_obj.get_path(device, "psu_p_out")
        if node is None:
            return 0.0
        try:
            with open(node, 'r') as f:
                p_out = int(f.read())
        except IOError:
            return 0.0

        # power is returned in micro watts
        return float(p_out)/1000000

    def get_powergood_status(self):
        """
        Retrieves the powergood status of PSU

        Returns:
            A boolean, True if PSU has stablized its output voltages and
            passed all its internal self-tests, False if not.
        """
        return self.get_status()

    def set_status_led(self, color):
        index = str(self.psu_index-1)
        color_state="SOLID"
        led_device_name = "PSU{}".format(self.psu_index) + "_LED"
        if(not pddf_obj.is_led_device_configured(led_device_name, index)):
		print "Set " + led_device_name + " : is not supported in the platform"
                return (False)

        pddf_obj.create_attr('device_name', led_device_name,  pddf_obj.get_led_path())
        pddf_obj.create_attr('index', index, pddf_obj.get_led_path())
        pddf_obj.create_attr('color', self.color_map[color], pddf_obj.get_led_cur_state_path())
        pddf_obj.create_attr('color_state', color_state, pddf_obj.get_led_cur_state_path())
        pddf_obj.create_attr('dev_ops', 'set_status',  pddf_obj.get_led_path())
        return (True)


    def get_status_led(self, color):
        index = str(self.psu_index-1)
        led_device_name = "PSU{}".format(self.psu_index) + "_LED"
        if(not pddf_obj.is_led_device_configured(led_device_name, index)):
		print "Set " + led_device_name + " : is not supported in the platform"
                return (False)

        pddf_obj.create_attr('device_name', led_device_name,  pddf_obj.get_led_path())
        pddf_obj.create_attr('index', index, pddf_obj.get_led_path())
        pddf_obj.create_attr('dev_ops', 'get_status',  pddf_obj.get_led_path())
        color=pddf_obj.get_led_color()
        return (True)

    def dump_sysfs(self):
        return pddf_obj.cli_dump_dsysfs('psu')
