#!/usr/bin/env python


# Sample pddf_fanutil file 
# All the supported FAN SysFS aattributes are
#- fan<idx>_present
#- fan<idx>_direction
#- fan<idx>_input
#- fan<idx>_pwm
#- fan<idx>_fault
# where idx is in the range [1-6]
#


import os.path
import sys, traceback, time
sys.path.append('/usr/share/sonic/platform/sonic_platform')
import pddfparse
import json

try:
    from sonic_platform_base.fan_base import FanBase
except ImportError as e:
    raise ImportError(str(e) + "- required module not found")


class Fan(FanBase):
    """PDDF generic Fan class"""
    color_map = {
         "STATUS_LED_COLOR_GREEN" : "on",
         "STATUS_LED_COLOR_RED" : "faulty",
         "STATUS_LED_COLOR_OFF" : "off"
    }


    def __init__(self, tray_idx, fan_idx=0, is_psu_fan=False, psu_index=0):
        # idx is 0-based 
        global pddf_obj
        global plugin_data
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)) + '/../pddf/pd-plugin.json')) as pd:
            plugin_data = json.load(pd)

        pddf_obj = pddfparse.PddfParse()
        self.platform = pddf_obj.get_platform()
        if tray_idx<0 or tray_idx>=self.platform['num_fantrays']:
            print "Invalid fantray index %d\n"%tray_idx
            return
        
        if fan_idx<0 or fan_idx>=self.platform['num_fans_pertray']:
            print "Invalid fan index (within a tray) %d\n"%fan_idx
            return

        self.fantray_index = tray_idx+1
        self.fan_index = fan_idx+1
        self.is_psu_fan = is_psu_fan
        if self.is_psu_fan:
            self.fans_psu_index = psu_index

        #self.is_rear = is_rear #TODO: Should this be included in __init__ arguments



    def get_name(self):
        """
        Retrieves the fan name
        Returns: String containing fan-name
        """
        if self.is_psu_fan:
            return "PSU_FAN{}".format(self.fan_index)
        else:
            if 'name' in plugin_data['FAN']:
                return plugin_data['FAN']['name'][str(self.fantray_index)]
            else:
                return "FAN{}_{}".format(self.fantray_index, self.fan_index)

    def get_presence(self):
        if self.is_psu_fan:
            return True
        else:
            idx = (self.fantray_index-1)*self.platform['num_fans_pertray'] + self.fan_index
            attr_name = "fan" + str(idx) + "_present"
            sysfs_path = pddf_obj.get_path("FAN-CTRL", attr_name)
            if sysfs_path is None:
                return False
            try:
                with open(sysfs_path, 'r') as f:
                    presence = int(f.read())
            except IOError:
                return False
            
            status = (True if presence==1 else False)
            return status

    #def get_model(self):
        #"""
        #Retrieves the model number (or part number) of the device

        #Returns:
            #string: Model/part number of device
        #"""
        #raise NotImplementedError

    #def get_serial(self):
        #"""
        #Retrieves the serial number of the device

        #Returns:
            #string: Serial number of device
        #"""
        #raise NotImplementedError

    def get_status(self):
        speed = self.get_speed()
        #rear_speed = self.get_speed_rear()
        status = True if (speed != 0) else False
        return status

    def get_direction(self):
        """
        Retrieves the direction of fan

        Returns:
            A string, either FAN_DIRECTION_INTAKE or FAN_DIRECTION_EXHAUST
            depending on fan direction
        """
        if self.is_psu_fan:
            attr = "psu_fan_dir"
            device = "PSU{}".format(self.fans_psu_index)
            path = pddf_obj.get_path(device, "psu_fan_dir")
            if path is None:
                return None
            try:
                with open(path, 'r') as f:
                    val = f.read()
            except IOError:
                return None

            val = val.rstrip()
            vmap = plugin_data['PSU']['psu_fan_dir']['valmap']
            if val in vmap:
                direction = vmap[val]
            else:
                direction = val

        else:
            idx = (self.fantray_index-1)*self.platform['num_fans_pertray'] + self.fan_index
            attr = "fan" + str(self.fan_index) + "_direction"
            path = pddf_obj.get_path("FAN-CTRL", attr)
        
            if path is None:
                return None
            try:
                with open(path, 'r') as f:
                    val = f.read()
            except IOError:
                return None

            val = val.rstrip()
            vmap = plugin_data['FAN']['direction']['valmap']
            if val.rstrip('\n') in vmap:
                direction = vmap[val.rstrip('\n')]
            else:
                direction = val

        return direction

    def get_speed(self):
        """
        Retrieves the speed of fan as a percentage of full speed

        Returns:
            An integer, the percentage of full fan speed, in the range 0 (off)
                 to 100 (full speed)
        """
        if self.is_psu_fan:
            attr = "psu_fan{}_speed_rpm".format(self.fan_index)
            device = "PSU{}".format(self.fans_psu_index)
            path = pddf_obj.get_path(device, attr)
            if path is None:
                return 0
            try:
                with open(path, 'r') as f:
                    speed = int(f.read())
            except IOError:
                return 0
            
            max_speed = int(plugin_data['PSU']['PSU_FAN_MAX_SPEED'])
            speed_percentage = (speed*100)/max_speed
            return speed_percentage
        else:
            idx = (self.fantray_index-1)*self.platform['num_fans_pertray'] + self.fan_index
            attr = "fan" + str(idx) + "_pwm"
            path = pddf_obj.get_path("FAN-CTRL", attr)

            if path is None:
                return 0
            try:
                with open(path, 'r') as f:
                    fpwm = int(f.read())
            except IOError:
                return 0

            pwm_to_dc = eval(plugin_data['FAN']['pwm_to_duty_cycle'])
            speed_percentage = pwm_to_dc(fpwm)
            #print "Speed: %d%%\n"%(speed_percentage)

            return speed_percentage

    def get_speed_rpm(self):
        """
        Retrieves the speed of fan in RPM

        Returns:
            An integer, Speed of fan in RPM
        """
        if self.is_psu_fan:
            attr = "psu_fan{}_speed_rpm".format(self.fan_index)
            device = "PSU{}".format(self.fans_psu_index)
            path = pddf_obj.get_path(device, attr)
            if path is None:
                return 0
            try:
                with open(path, 'r') as f:
                    speed = int(f.read())
            except IOError:
                return 0
            
            rpm_speed = speed
            return rpm_speed
        else:
            idx = (self.fantray_index-1)*self.platform['num_fans_pertray'] + self.fan_index
            attr = "fan" + str(idx) + "_input"
            path = pddf_obj.get_path("FAN-CTRL", attr)

            if path is None:
                return 0
            try:
                with open(path, 'r') as f:
                    rpm_speed = int(f.read())
            except IOError:
                return 0


            return rpm_speed

    #def get_target_speed(self):
        #"""
        #Retrieves the target (expected) speed of the fan

        #Returns:
            #An integer, the percentage of full fan speed, in the range 0 (off)
                 #to 100 (full speed)
        #"""
        #raise NotImplementedError

    #def get_speed_tolerance(self):
        #"""
        #Retrieves the speed tolerance of the fan

        #Returns:
            #An integer, the percentage of variance from target speed which is
                 #considered tolerable
        #"""
        #raise NotImplementedError

    def set_speed(self, speed):
        """
        Sets the fan speed

        Args:
            speed: An integer, the percentage of full fan speed to set fan to,
                   in the range 0 (off) to 100 (full speed)

        Returns:
            A boolean, True if speed is set successfully, False if not
        """
        if self.is_psu_fan:
            print "Setting PSU fan speed is not allowed"
            return False
        else:
            if speed<0 or speed>100:
                print "Error: Invalid speed %d. Please provide a valid speed percentage"%speed
                return False

            duty_cycle_to_pwm = eval(plugin_data['FAN']['duty_cycle_to_pwm'])
            pwm = duty_cycle_to_pwm(speed)
            #print "New Speed: %d%% - PWM value to be set is %d\n"%(speed,pwm)

            status = 0
            idx = (self.fantray_index-1)*self.platform['num_fans_pertray'] + self.fan_index
            attr = "fan" + str(idx) + "_pwm"
            node = pddf_obj.get_path("FAN-CTRL", attr)
            if node is None:
                return False
            try:
                with open(node, 'w') as f:
                    f.write(str(pwm))
            except IOError:
                return False

            #print "Done changing the speed of all the fans ... Reading the speed to crossscheck\n"
            return True

    def set_status_led(self, color):
        index = str(self.fantray_index-1)
        color_state="SOLID"
        led_device_name = "FANTRAY{}".format(self.fantray_index) + "_LED"
        if(not pddf_obj.is_led_device_configured(led_device_name, index)):
                print "ERROR: Set " + led_device_name + " : is not supported in the platform"
                return (False)

        if (not color in self.color_map.keys()):
                return ("ERROR: Invalid color")

        pddf_obj.create_attr('device_name', led_device_name,  pddf_obj.get_led_path())
        pddf_obj.create_attr('index', index, pddf_obj.get_led_path())
        pddf_obj.create_attr('color', self.color_map[color], pddf_obj.get_led_cur_state_path())
        pddf_obj.create_attr('color_state', color_state, pddf_obj.get_led_cur_state_path())
        pddf_obj.create_attr('dev_ops', 'set_status',  pddf_obj.get_led_path())
        return (True)


    def get_status_led(self, color):
        index = str(self.fantray_index-1)
        led_device_name = "FANTRAY{}".format(self.fantray_index) + "_LED"
        if(not pddf_obj.is_led_device_configured(led_device_name, index)):
                print "ERROR: Read " + led_device_name  + " : is not supported in the platform"
                return (False)

        pddf_obj.create_attr('device_name', led_device_name,  pddf_obj.get_led_path())
        pddf_obj.create_attr('index', index, pddf_obj.get_led_path())
        pddf_obj.create_attr('dev_ops', 'get_status',  pddf_obj.get_led_path())
        color=pddf_obj.get_led_color()
        return (True)


    def dump_sysfs(self):
        return pddf_obj.cli_dump_dsysfs('fan')

