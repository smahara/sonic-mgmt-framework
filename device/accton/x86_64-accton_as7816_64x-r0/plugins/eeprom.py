#!/usr/bin/env python

try:
    import exceptions
    import binascii
    import time
    import optparse
    import warnings
    import os
    import sys
    from sonic_eeprom import eeprom_base
    from sonic_eeprom import eeprom_tlvinfo
    import subprocess
except ImportError, e:
    raise ImportError (str(e) + "- required module not found")

class board(eeprom_tlvinfo.TlvInfoDecoder):
    _TLV_INFO_MAX_LEN = 256
    def __init__(self, name, path, cpld_root, ro):
        self.eeprom_path = "/sys/bus/i2c/devices/0-0056/eeprom"
        super(board, self).__init__(self.eeprom_path, 0, '', True)


    def read_eeprom_bytes(self, byteCount, offset=0):
        subcmd =  "i2cget -y -f 0 0x56 {0} w"
        byte = []
        for x in range(offset, offset+byteCount, 2):
            cmd = subcmd.format(x)
            wd = os.popen(cmd).read() 
            num = int(wd, 16)
            byte.append(chr(num &255))
            byte.append(chr(num >> 8))
            #str +=  ''.join(hex(num >> 8)[2:])
            str = ''.join(byte)
        if len(str) < byteCount:
            raise RuntimeError("expected to read %d bytes, " \
                %(byteCount) + "but only read %d" %(len(str)))
        return str[:byteCount]


