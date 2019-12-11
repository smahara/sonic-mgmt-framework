#!/usr/bin/env python

try:
    import os
    import sys
    from pddf_eeprom import PddfEeprom
except ImportError, e:
    raise ImportError(str(e) + "- required module not found")


class Eeprom(PddfEeprom):
    # Display vendor extension for Quanta platforms
    _TLV_DISPLAY_VENDOR_EXT = True

    def __init__(self):
        PddfEeprom.__init__(self)

    # Provide the functions/variables below for which implementation is to be overwritten
