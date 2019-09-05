#!/usr/bin/env python
#
# sensors.py
#
# Diag tool with sensors in SONiC
#

try:
    import sys
    import os
    from diag_util import DiagUtil
except ImportError as e:
    raise ImportError("%s - required module not found" % str(e))

VERSION = '1.0'

def version():
    """Display version info"""
    print "diag_sensors version {0}".format(VERSION)

def run_sensors():
	os.system("sudo sensors >> " + LOG_FILE)

# ==================== Main Logic ====================
if len(sys.argv) != 2:
        print "Usage: <script> <logfile>"
        print len(sys.argv)
        sys.exit(1)

LOG_FILE=sys.argv[1]
stdout_org = sys.stdout
sys.stdout = open(LOG_FILE, "w+")

version()
run_sensors()

sys.stdout = stdout_org

diagUtil=DiagUtil()
diagUtil.check_log_file_err_msg('sensors', LOG_FILE)




