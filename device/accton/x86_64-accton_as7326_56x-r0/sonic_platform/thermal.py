#!/usr/bin/env python

#############################################################################
#
# Module contains an implementation of SONiC Platform Base API and
# provides the thermal status which are available in the platform
#
#############################################################################

import json
import math
import os.path

try:
    from sonic_platform_base.thermal_base import ThermalBase
except ImportError as e:
    raise ImportError(str(e) + "- required module not found")

class Thermal(ThermalBase):
    """Platform-specific Thermal class"""

    temp_node_map = {
        1: "/sys/class/hwmon/hwmon0",
        2: "/sys/class/hwmon/hwmon1",
        3: "/sys/class/hwmon/hwmon3",
        4: "/sys/class/hwmon/hwmon4",
        5: "/sys/class/hwmon/hwmon5",
        6: "/sys/class/hwmon/hwmon6"
    }

    temp_name_map = {
        1: "pch_haswell-virtual-0",
        2: "coretemp-isa-0000",
        3: "lm75-i2c-15-0048",
        4: "lm75-i2c-15-004a",
        5: "lm75-i2c-15-0049",
        6: "lm75-i2c-15-004b"
    }

    def __init__(self, temp_index):
        self.index = temp_index + 1
        ThermalBase.__init__(self)

    def get_name(self):
        """
        Retrieves the name of the device

        Returns:
            string: The name of the device
        """
        return self.temp_name_map[self.index]

    def get_status(self):
        """
        Retrieves the operational status of the device

        Returns:
            A boolean value, True if device is operating properly, False if not
        """
        if self.get_temperature() == -255:
            return False
        return True

    def get_presence(self):
        """
        Retrieves the presence of the device

        Returns:
            bool: True if device is present, False if not
        """
        if os.path.exists(self.temp_node_map[self.index] + "/temp1_input"):
            return True
        return False

    def get_temperature(self):
        """
        Retrieves current temperature reading from thermal

        Returns:
            A float number of current temperature in Celsius up to nearest thousandth
            of one degree Celsius, e.g. 30.125 
        """
        temp = 0
        node = self.temp_node_map[self.index] + "/temp1_input"
        try:
            with open(node, 'r') as fp:
                temp = float(fp.read()) / 1000
        except IOError:
            temp = -255
        return temp
