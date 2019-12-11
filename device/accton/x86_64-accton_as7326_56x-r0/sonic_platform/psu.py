#!/usr/bin/env python

#############################################################################
#
# Module contains an implementation of SONiC Platform Base API and
# provides the PSU status which are available in the platform
#
#############################################################################

import json
import math
import os.path

try:
    from sonic_platform_base.psu_base import PsuBase
    from sonic_platform_base.fan_base import FanBase
except ImportError as e:
    raise ImportError(str(e) + "- required module not found")

class PsuFan(FanBase):
    """Platform-specific Fan class"""

    def __init__(self, fan_index):
        self.index = fan_index + 1
        self.psu_path = "/sys/bus/i2c/devices/"
        self.psu_fan_dir = "/psu_fan_dir"
        self.psu_fan_rpm_max = 10000
        self.psu_fan_rpm = "/psu_fan1_speed_rpm"
        self.psu_mapping_diag = {
            2: "13-005b",
            1: "17-0059",
        }
        FanBase.__init__(self)

    def get_direction(self):
        """
        Retrieves the direction of fan

        Returns:
            A string, either FAN_DIRECTION_INTAKE or FAN_DIRECTION_EXHAUST
            depending on fan direction
        """
        node = self.psu_path + self.psu_mapping_diag[self.index] + self.psu_fan_dir
        try:
            with open(node, 'r') as psu_fan_dir:
                dir = psu_fan_dir.read()
        except IOError:
            return self.FAN_DIRECTION_INTAKE

        if dir.startswith('F2B'):
            return self.FAN_DIRECTION_INTAKE

        return self.FAN_DIRECTION_EXHAUST

    def get_speed(self):
        """
        Retrieves the speed of fan as a percentage of full speed

        Returns:
            An integer, the percentage of full fan speed, in the range 0 (off)
                 to 100 (full speed)
        """
        rpm = 0
        node = self.psu_path + self.psu_mapping_diag[self.index] + self.psu_fan_rpm
        try:
            with open(node, 'r') as speed_rpm:
                rpm = int(speed_rpm.read())
        except IOError:
            return 0
        return ((rpm * 100) / self.psu_fan_rpm_max)

    def get_speed_rpm(self):
        """
        Retrieves the speed of fan in revolutions per monute 

        Returns:
            An integer, speed of a fan in RPM
        """
        rpm = 0
        node = self.psu_path + self.psu_mapping_diag[self.index] + self.psu_fan_rpm
        try:
            with open(node, 'r') as speed_rpm:
                rpm = int(speed_rpm.read())
        except IOError:
            return 0
        return (rpm)

class Psu(PsuBase):
    """Platform-specific PSU class"""

    def __init__(self, psu_index):
        PsuBase.__init__(self)
        fan = PsuFan(psu_index)
        self._fan_list.append(fan)
        self.index = psu_index + 1
        self.psu_drv = "ym2651"
        self.psu_path = "/sys/bus/i2c/devices/"
        self.psu_presence = "/psu_present"
        self.psu_oper_status = "/psu_power_good"
        self.psu_model_name = "/psu_model_name"
        self.psu_serial_num = "/psu_serial_num"
        self.psu_mfr_id = "/psu_mfr_id"
        self.psu_v_out = "/psu_v_out"
        self.psu_i_out = "/psu_i_out"
        self.psu_p_out = "/psu_p_out"
        self.psu_mapping_info = {
            2: "13-0053",
            1: "17-0051",
        }
        self.psu_mapping_diag = {
            2: "13-005b",
            1: "17-0059",
        }

    def get_name(self):
        """
        Retrieves the name of the device

        Returns:
            string: The name of the device
        """
        return "{}-i2c-{}".format(self.psu_drv, self.psu_mapping_diag[self.index])

    def get_presence(self):
        """
        Retrieves the presence of the device

        Returns:
            bool: True if device is present, False if not
        """
        status = 0
        node = self.psu_path + self.psu_mapping_info[self.index] + self.psu_presence
        try:
            with open(node, 'r') as presence_status:
                status = int(presence_status.read())
        except IOError:
            return False
        return status == 1

    def get_status(self):
        """
        Retrieves the operational status of the device

        Returns:
            A boolean value, True if device is operating properly, False if not
        """
        status = 0
        node = self.psu_path + self.psu_mapping_info[self.index] + self.psu_oper_status
        try:
            with open(node, 'r') as power_status:
                status = int(power_status.read())
        except IOError:
            return False
        return status == 1

    def get_model(self):
        """
        Retrieves the model number (or part number) of the device

        Returns:
            string: Model/part number of device
        """
        model = ""
        node = self.psu_path + self.psu_mapping_info[self.index] + self.psu_model_name
        try:
            with open(node, 'r') as model_name:
                model = model_name.read()
        except IOError:
            return None
        return model.rstrip()

    def get_mfr_id(self):
        """
        Retrieves the manufacturer's name (or id) of the device

        Returns:
            string: Manufacturer's id of device
        """
        mfr = ""
        node = self.psu_path + self.psu_mapping_diag[self.index] + self.psu_mfr_id
        try:
            with open(node, 'r') as mfr_id:
                mfr = mfr_id.read()
        except IOError:
            return None
        return mfr.rstrip()

    def get_serial(self):
        """
        Retrieves the serial number of the device

        Returns:
            string: Serial number of device
        """
        serial = ""
        node = self.psu_path + self.psu_mapping_diag[self.index] + self.psu_serial_num
        try:
            with open(node, 'r') as serial_num:
                serial = serial_num.read()
        except IOError:
            return None
        return serial.rstrip()[1:]  # pmbus read output's first char needs to be left

    def get_voltage(self):
        """
        Retrieves current PSU voltage output

        Returns:
            A float number, the output voltage in volts, 
            e.g. 12.1 
        """
        vout = 0
        node = self.psu_path + self.psu_mapping_diag[self.index] + self.psu_v_out
        try:
            with open(node, 'r') as v_out:
                vout = int(v_out.read())
        except IOError:
            return 0
        return float(vout)

    def get_current(self):
        """
        Retrieves present electric current supplied by PSU

        Returns:
            A float number, the electric current in amperes, e.g 15.4
        """
        iout = 0
        node = self.psu_path + self.psu_mapping_diag[self.index] + self.psu_i_out
        try:
            with open(node, 'r') as i_out:
                iout = int(i_out.read())
        except IOError:
            return 0
        return float(iout)

    def get_power(self):
        """
        Retrieves current energy supplied by PSU

        Returns:
            A float number, the power in watts, e.g. 302.6
        """
        pout = 0
        node = self.psu_path + self.psu_mapping_diag[self.index] + self.psu_p_out
        try:
            with open(node, 'r') as p_out:
                pout = int(p_out.read())
        except IOError:
            return 0
        return float(pout*1000) #return power value in micro watts

    def get_powergood_status(self):
        """
        Retrieves the powergood status of PSU

        Returns:
            A boolean, True if PSU has stablized its output voltages and passed all
            its internal self-tests, False if not.
        """
        status = 0
        node = self.psu_path + self.psu_mapping_info[self.index] + self.psu_oper_status
        try:
            with open(node, 'r') as powergood_status:
                status = int(powergood_status.read())
        except IOError:
            return False
        return status == 1
