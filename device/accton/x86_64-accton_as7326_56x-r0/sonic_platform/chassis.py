#!/usr/bin/env python

#############################################################################
#
# Module contains an implementation of SONiC Platform Base API and
# provides the Chassis information which are available in the platform
#
#############################################################################

import sys
import re
import os
import subprocess
import json

try:
    from sonic_platform_base.chassis_base import ChassisBase
    from sonic_platform.thermal import Thermal
    from sonic_platform.fan import Fan
    from sonic_platform.psu import Psu
    from sonic_platform.sfp import Sfp
except ImportError as e:
    raise ImportError(str(e) + "- required module not found")

NUM_THERMAL = 6
NUM_FAN = 12
NUM_PSU = 2
NUM_SFP = 82
CONFIG_DB_PATH = "/etc/sonic/config_db.json"

class Chassis(ChassisBase):
    """Platform-specific Chassis class"""

    def __init__(self):
        ChassisBase.__init__(self)
        for index in range(0, NUM_THERMAL):
            thermal = Thermal(index)
            self._thermal_list.append(thermal)
        for index in range(0, NUM_FAN):
            fan = Fan(index)
            self._fan_list.append(fan)
        for index in range(0, NUM_PSU):
            psu = Psu(index)
            self._psu_list.append(psu)
        for index in range(0, NUM_SFP):
            sfp = Sfp(index)
            self._sfp_list.append(sfp)

    def __read_config_db(self):
        try:
            with open(CONFIG_DB_PATH, 'r') as fd:
                data = json.load(fd)
                return data
        except IOError:
            raise IOError("Unable to open config_db file !")

    def get_base_mac(self):
        """
        Retrieves the base MAC address for the chassis
        Returns:
            A string containing the MAC address in the format
            'XX:XX:XX:XX:XX:XX'
        """
        try:
            self.config_data = self.__read_config_db()
            base_mac = self.config_data["DEVICE_METADATA"]["localhost"]["mac"]
            return str(base_mac)
        except KeyError:
            raise KeyError("Base MAC not found")

