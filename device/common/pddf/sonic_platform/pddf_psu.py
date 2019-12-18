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


try:
    import os.path
    import sys, traceback
    sys.path.append('/usr/share/sonic/platform/sonic_platform')
    import pddfparse
    import json
    from sonic_platform_base.psu_base import PsuBase
    from sonic_platform.fan import Fan
except ImportError as e:
    raise ImportError (str(e) + "- required module not found")


class PddfPsu(PsuBase):
    """PDDF generic PSU class"""

    color_map = {
         "STATUS_LED_COLOR_GREEN" : "on",
         "STATUS_LED_COLOR_RED" : "faulty",
         "STATUS_LED_COLOR_OFF" : "off"
    }


    def __init__(self, index):
        PsuBase.__init__(self)
        global pddf_obj
        global plugin_data
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)) + '/../../../platform/pddf/pd-plugin.json')) as pd:
            plugin_data = json.load(pd)

        pddf_obj = pddfparse.PddfParse()
        self.platform = pddf_obj.get_platform()
        self.psu_index = index + 1
        
        self._fan_list = []     # _fan_list under PsuBase class is a global variable, hence we need to use _fan_list per class instatiation
        self.num_psu_fans = int(pddf_obj.get_num_psu_fans('PSU{}'.format(index+1)))
        for psu_fan_idx in range(self.num_psu_fans):
            psu_fan = Fan(0, psu_fan_idx, True, self.psu_index)
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
            return plugin_data['PSU']['name'][str(self.psu_index)]
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
        output = pddf_obj.get_attr_name_output(device, "psu_present")
	if not output:
	    return False

        mode = output['mode']
	status = output['status']

        vmap = plugin_data['PSU']['psu_present'][mode]['valmap']

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
        output = pddf_obj.get_attr_name_output(device, "psu_model_name")
        if not output:
            return None 

        model = output['status']

        return model.rstrip('\n')

    def get_serial(self):
        """
        Retrieves the serial number of the device

        Returns:
            string: Serial number of device
        """
        device = "PSU{}".format(self.psu_index)
        output = pddf_obj.get_attr_name_output(device, "psu_serial_num")
        if not output:
            return None 

        serial = output['status']

        return serial.rstrip('\n')

    def get_status(self):
        """
        Retrieves the operational status of the device

        Returns:
            A boolean value, True if device is operating properly, False if not
        """
        device = "PSU{}".format(self.psu_index)

        output = pddf_obj.get_attr_name_output(device, "psu_power_good")
        if not output:
            return False

        mode = output['mode']
        status = output ['status']

        vmap = plugin_data['PSU']['psu_power_good'][mode]['valmap']

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
        output = pddf_obj.get_attr_name_output(device, "psu_mfr_id")
        if not output:
            return None 

	mfr = output['status']

        return mfr.rstrip('\n')

    def get_voltage(self):
        """
        Retrieves current PSU voltage output

        Returns:
            A float number, the output voltage in volts,
            e.g. 12.1
        """
        device = "PSU{}".format(self.psu_index)        
        output = pddf_obj.get_attr_name_output(device, "psu_v_out")
        if not output:
            return 0.0
		
        v_out = output['status']

        return float(v_out)

    def get_current(self):
        """
        Retrieves present electric current supplied by PSU

        Returns:
            A float number, electric current in amperes,
            e.g. 15.4
        """
        device = "PSU{}".format(self.psu_index)
        output = pddf_obj.get_attr_name_output(device, "psu_i_out")
        if not output:
            return 0.0

        i_out = output['status']

        # current in mA
        return float(i_out)

    def get_power(self):
        """
        Retrieves current energy supplied by PSU

        Returns:
            A float number, the power in watts,
            e.g. 302.6
        """
        device = "PSU{}".format(self.psu_index)
        output = pddf_obj.get_attr_name_output(device, "psu_p_out")
        if not output:
            return 0.0

        p_out = output['status']

        # power is returned in micro watts
        return float(p_out)

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

        if (not led_device_name in pddf_obj.data.keys()):
                print "ERROR: " + led_device_name + " is not configured"
                return (False)

        if (not color in self.color_map.keys()):
                print "ERROR: Invalid color"
                return (False)


        if(not pddf_obj.is_led_device_configured(led_device_name, self.color_map[color])):
                print "ERROR :" + led_device_name + ' ' + color + " :  is not supported in the platform"
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

        if (not led_device_name in pddf_obj.data.keys()):
                print "ERROR: " + led_device_name + " is not configured"
                return (False)

        pddf_obj.create_attr('device_name', led_device_name,  pddf_obj.get_led_path())
        pddf_obj.create_attr('index', index, pddf_obj.get_led_path())
        pddf_obj.create_attr('dev_ops', 'get_status',  pddf_obj.get_led_path())
        color=pddf_obj.get_led_color()
        return (True)

    def dump_sysfs(self):
        return pddf_obj.cli_dump_dsysfs('psu')
