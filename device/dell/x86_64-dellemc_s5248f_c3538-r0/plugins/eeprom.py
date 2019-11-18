#!/usr/bin/env python

#############################################################################
# DellEMC S5248f
#
# Platform and model specific eeprom subclass, inherits from the base class,
# and provides the followings:
# - the eeprom format definition
# - specific encoder/decoder if there is special need
#############################################################################

try:
<<<<<<< HEAD
    import os.path
=======
>>>>>>> origin/broadcom_sonic_share
    from sonic_eeprom import eeprom_tlvinfo
except ImportError, e:
    raise ImportError (str(e) + "- required module not found")


class board(eeprom_tlvinfo.TlvInfoDecoder):

    def __init__(self, name, path, cpld_root, ro):
<<<<<<< HEAD
        self.eeprom_path = None
        for b in (0, 1):
            f = '/sys/class/i2c-adapter/i2c-{0}/{0}-0050/eeprom'.format(b)
            if os.path.exists(f):
                self.eeprom_path = f
                break
        if self.eeprom_path is None:
            return

=======
        self.eeprom_path = "/sys/class/i2c-adapter/i2c-0/0-0050/eeprom"
>>>>>>> origin/broadcom_sonic_share
        super(board, self).__init__(self.eeprom_path, 0, '', True)
