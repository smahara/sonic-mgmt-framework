#!/usr/bin/env python

import os.path
import sys, traceback
sys.path.append('/usr/share/sonic/platform/sonic_platform')
import pddfparse
import json

try:
    import time
    from ctypes import create_string_buffer
    from sonic_platform_base.chassis_base import ChassisBase
    from sonic_platform_base.sfp_base import SfpBase
    from sonic_platform_base.sonic_sfp.sff8436 import sff8436InterfaceId
    from sonic_platform_base.sonic_sfp.sff8436 import sff8436Dom
except ImportError, e:
    raise ImportError (str(e) + "- required module not found")

class Sfp(SfpBase):
    """
    Platform generic PDDF Sfp class
    """

    _port_to_eeprom_mapping = {}
    _port_start = 0
    _port_end = 0
    _port_to_type_mapping = {}
    _qsfp_ports = []
    _sfp_ports = []

    def __init__(self, index):
        SfpUtilBase.__init__(self)
        global pddf_obj
        global plugin_data
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)) + '/../pddf/pd-plugin.json')) as pd:
            plugin_data = json.load(pd)

        pddf_obj = pddfparse.PddfParse()
        self.platform = pddf_obj.get_platform()
        
        self.sfp_index = index

    def get_transceiver_change_event(self):
        """
        TODO: This function need to be implemented
        when decide to support monitoring SFP(Xcvrd)
        on this platform.
        """
        raise NotImplementedError


    def dump_sysfs(self):
        return pddf_obj.cli_dump_dsysfs('xcvr')

