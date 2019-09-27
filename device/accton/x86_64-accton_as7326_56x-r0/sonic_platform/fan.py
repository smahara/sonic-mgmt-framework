#!/usr/bin/env python

#############################################################################
#
# Module contains an implementation of SONiC Platform Base API and
# provides the fan status which are available in the platform
#
#############################################################################

import json
import math
import os.path

try:
    from sonic_platform_base.fan_base import FanBase
except ImportError as e:
    raise ImportError(str(e) + "- required module not found")

class Fan(FanBase):
    """Platform-specific Fan class"""

    FAN_MOD_NAME = 'as7326_56x_fan-i2c-11-66'
    FAN_RPM_MAX = 21500
    BASE_VAL_PATH = '/sys/bus/i2c/devices/11-0066/{0}'
    FAN_DUTY_PATH = '/sys/bus/i2c/devices/11-0066/fan_duty_cycle_percentage'

    def __init__(self, fan_index):
        self.index = fan_index + 1
        FanBase.__init__(self)

    def get_name(self):
        """
        Retrieves the name of the device

        Returns:
            string: The name of the device
        """
        return "{}:fan{}".format(self.FAN_MOD_NAME, self.index)

    def get_status(self):
        """
        Retrieves the operational status of the device

        Returns:
            A boolean value, True if device is operating properly, False if not
        """
        status = 0
        attr = 'fan' + str(self.index) + '_fault'
        node = self.BASE_VAL_PATH.format(attr)
        try:
            with open(node, 'r') as fault:
                status = int(fault.read())
        except IOError as e:
            print "Error: %s"%str(e)
            return False
        return False if (status > 0) else True

    def get_presence(self):
        """
        Retrieves the presence of the device

        Returns:
            bool: True if device is present, False if not
        """
        status = 0
        attr = 'fan' + str(self.index) + '_present'
        node = self.BASE_VAL_PATH.format(attr)
        try:
            with open(node, 'r') as presence_status:
                status = int(presence_status.read())
        except IOError as e:
            print "Error: %s"%str(e)
            return None
        return status == 1

    def get_direction(self):
        """
        Retrieves the direction of fan

        Returns:
            A string, either FAN_DIRECTION_INTAKE or FAN_DIRECTION_EXHAUST
            depending on fan direction
        """
        direction = ""
        attr = 'fan' + str(self.index) + '_direction'
        node = self.BASE_VAL_PATH.format(attr)
        try:
            with open(node, 'r') as fan_dir:
                direction = int(fan_dir.read())
        except IOError as e:
            print "Error: %s"%str(e)
            return self.FAN_DIRECTION_INTAKE
        if direction == 1:
            return self.FAN_DIRECTION_INTAKE

        return self.FAN_DIRECTION_EXHAUST

    def get_speed(self):
        """
        Retrieves the speed of fan as a percentage of full speed

        Returns:
            An integer, the percentage of full fan speed, in the range 0 (off)
                 to 100 (full speed)
        """
        frpm = 0
        attr = 'fan' + str(self.index) + '_front_speed_rpm'
        node = self.BASE_VAL_PATH.format(attr)
        try:
            with open(node, 'r') as front_speed:
                frpm = int(front_speed.read())
        except IOError as e:
            print "Error: %s"%str(e)
            return 0
        return (frpm * 100) / self.FAN_RPM_MAX

    def get_target_speed(self):
        """
        Retrieves the target (expected) speed of the fan

        Returns:
            An integer, the percentage of full fan speed, in the range 0 (off)
                 to 100 (full speed)
        """
        duty = 0
        node = self.FAN_DUTY_PATH
        try:
            with open(node, 'r') as fan_duty:
                duty = int(fan_duty.read())
        except IOError:
            duty = 0
        return duty

    def set_speed(self, speed):
        """
        Sets the fan speed

        Args:
            speed: An integer, the percentage of full fan speed to set fan to,
                   in the range 0 (off) to 100 (full speed)

        Returns:
            A boolean, True if speed is set successfully, False if not
        """
        if speed < 0 or speed > 100:
            return False
        node = self.FAN_DUTY_PATH
        try:
            with open(node, 'w') as fan_duty:
                fan_duty.write(str(speed))
        except IOError:
            return False
        return True
