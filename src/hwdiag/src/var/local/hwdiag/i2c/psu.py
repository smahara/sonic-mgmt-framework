#!/usr/bin/env python
#
# psu.py
#
# Diag tool with PSU in SONiC
#

try:
    import sys
    import os
    import subprocess
    import imp
    import syslog
    import traceback
    from tabulate import tabulate
    from diag_util import DiagUtil
except ImportError as e:
    raise ImportError("%s - required module not found" % str(e))

VERSION = '1.0'

SYSLOG_IDENTIFIER = "diag_psu"
PLATFORM_SPECIFIC_MODULE_NAME = "psuutil"
PLATFORM_SPECIFIC_CLASS_NAME = "PsuUtil"
DIAG_UTIL_CLASS_NAME = "diag_util"

PLATFORM_ROOT_PATH = '/usr/share/sonic/device'
PLATFORM_ROOT_PATH_DOCKER = '/usr/share/sonic/platform'
SONIC_CFGGEN_PATH = '/usr/local/bin/sonic-cfggen'
HWSKU_KEY = 'DEVICE_METADATA.localhost.hwsku'
PLATFORM_KEY = 'DEVICE_METADATA.localhost.platform'

# Global platform-specific psuutil class instance
platform_psuutil = None

# ========================== Syslog wrappers ==========================


def log_info(msg, also_print_to_console=False):
    syslog.openlog(SYSLOG_IDENTIFIER)
    syslog.syslog(syslog.LOG_INFO, msg)
    syslog.closelog()

    if also_print_to_console:
        print msg 


def log_warning(msg, also_print_to_console=False):
    syslog.openlog(SYSLOG_IDENTIFIER)
    syslog.syslog(syslog.LOG_WARNING, msg)
    syslog.closelog()

    if also_print_to_console:
        print msg 


def log_error(msg, also_print_to_console=False):
    syslog.openlog(SYSLOG_IDENTIFIER)
    syslog.syslog(syslog.LOG_ERR, msg)
    syslog.closelog()

    if also_print_to_console:
        print msg 


# ==================== Methods for initialization ====================

# Returns platform and HW SKU
def get_platform_and_hwsku():
    try:
        proc = subprocess.Popen([SONIC_CFGGEN_PATH, '-H', '-v', PLATFORM_KEY],
                                stdout=subprocess.PIPE,
                                shell=False,
                                stderr=subprocess.STDOUT)
        stdout = proc.communicate()[0]
        proc.wait()
        platform = stdout.rstrip('\n')

        proc = subprocess.Popen([SONIC_CFGGEN_PATH, '-d', '-v', HWSKU_KEY],
                                stdout=subprocess.PIPE,
                                shell=False,
                                stderr=subprocess.STDOUT)
        stdout = proc.communicate()[0]
        proc.wait()
        hwsku = stdout.rstrip('\n')
    except OSError, e:
        raise OSError("Cannot detect platform")

    return (platform, hwsku)

# Loads platform specific psuutil module from source
def load_platform_psuutil():
    global platform_psuutil

    # Get platform and hwsku
    (platform, hwsku) = get_platform_and_hwsku()

    # Load platform module from source
    platform_path = ''
    if len(platform) != 0:
        platform_path = "/".join([PLATFORM_ROOT_PATH, platform])
    else:
        platform_path = PLATFORM_ROOT_PATH_DOCKER
    hwsku_path = "/".join([platform_path, hwsku])

    try:
        module_file = "/".join([platform_path, "plugins", PLATFORM_SPECIFIC_MODULE_NAME + ".py"])
        module = imp.load_source(PLATFORM_SPECIFIC_MODULE_NAME, module_file)
    except IOError, e:
        log_error("Failed to load platform module '%s': %s" % (PLATFORM_SPECIFIC_MODULE_NAME, str(e)), True)
        return -1

    try:
        platform_psuutil_class = getattr(module, PLATFORM_SPECIFIC_CLASS_NAME)
        platform_psuutil = platform_psuutil_class()
    except AttributeError, e:
        log_error("Failed to instantiate '%s' class: %s" % (PLATFORM_SPECIFIC_CLASS_NAME, str(e)), True)

        return -2

    return 0

# ==================== PSU Diag Tool APIs ====================
def version():
    """Display version info"""
    print "diag_psu version {0}".format(VERSION)


def numpsus():
    """Display number of supported PSUs on device"""
    print "numspsus: " + str(platform_psuutil.get_num_psus())


def status():
    """Display PSU status"""
    supported_psu = range(1, platform_psuutil.get_num_psus() + 1)

    header = ['PSU', 'Status']
    status_table = []

    for psu in supported_psu:
        msg = ""
        psu_name = "PSU {}".format(psu)
        presence = platform_psuutil.get_psu_presence(psu)
        if presence:
            oper_status = platform_psuutil.get_psu_status(psu)
            msg = 'Inserted' if oper_status else "Removed"
        else:
            msg = 'NOT PRESENT'
        status_table.append([psu_name, msg])

    if status_table:
        print tabulate(status_table, header, tablefmt="simple")


# ==================== Main Logic ====================
err = load_platform_psuutil()
if err != 0:
    log_error("Failed to load load_platform_psuutil", True)
    sys.exit(2)

if len(sys.argv) != 2:
	print "Usage: <script> <logfile>"
	print len(sys.argv)
    	sys.exit(1)

LOG_FILE=sys.argv[1]
stdout_org = sys.stdout
sys.stdout = open(LOG_FILE, "w+")

version()
numpsus()
status()

sys.stdout = stdout_org

diagUtil=DiagUtil()
diagUtil.check_log_file_err_msg('psu', LOG_FILE)

