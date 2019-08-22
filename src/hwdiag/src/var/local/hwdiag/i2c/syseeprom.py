#!/usr/bin/env python

#############################################################################
#
# Dial Tool for eeprom decoding
#
try:
    import exceptions
    import binascii
    import time
    import optparse
    import warnings
    import os
    import subprocess
    import sys
    from array import array
    import imp
    from diag_util  import DiagUtil

    from sonic_device_util import get_machine_info
    from sonic_device_util import get_platform_info

except ImportError, e:
    raise ImportError (str(e) + "- required module not found")

PLATFORM_ROOT = '/usr/share/sonic/device'
CACHE_ROOT = '/var/cache/sonic/decode-syseeprom'
CACHE_FILE = 'syseeprom_cache'

def decode_syseeprom():
#    if not os.geteuid() == 0:
#        raise RuntimeError("must be root to run")

    # Get platform name
    platform = get_platform_info(get_machine_info())

    platform_path = '/'.join([PLATFORM_ROOT, platform])


    #
    # load the target class file and instantiate the object
    #
    try:
        m = imp.load_source('eeprom','/'.join([platform_path, 'plugins', 'eeprom.py']))
    except IOError:
        raise IOError("cannot load module: " + '/'.join([platform_path, 'plugins', 'eeprom.py']))

    class_ = getattr(m, 'board')
    t = class_('board', '','','')

    #
    # execute the command
    #
    run(t)

#-------------------------------------------------------------------------------
#
# Run
#
def run(target):

    if not os.path.exists(CACHE_ROOT):
        try:
            os.makedirs(CACHE_ROOT)
        except:
            pass

    #
    # only the eeprom classes that inherit from eeprom_base
    # support caching. Others will work normally
    #
    try:
        target.set_cache_name(os.path.join(CACHE_ROOT, CACHE_FILE))
    except:
        pass

    e = target.read_eeprom()
    if e is None :
        return 0

    try:
        target.update_cache(e)
    except:
        pass
    target.decode_eeprom(e)
    (is_valid, valid_crc) = target.is_checksum_valid(e)
    if is_valid:
         print '(checksum valid)'
    else:
         print '(*** checksum invalid)'
    return 0


# ==================== Main Logic ====================
if len(sys.argv) != 2:
        print "Usage: <script> <logfile>"
        print len(sys.argv)
        sys.exit(1)

LOG_FILE=sys.argv[1]
stdout_org = sys.stdout

sys.stdout = open(LOG_FILE, "w+") 

decode_syseeprom()

sys.stdout = stdout_org


diagUtil=DiagUtil()
diagUtil.check_log_file_err_msg('syseeprom', LOG_FILE)

