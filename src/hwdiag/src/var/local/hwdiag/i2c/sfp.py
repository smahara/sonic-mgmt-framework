#!/usr/bin/env python
#
# sfp.py
#
# Diag SFP Tool for interacting with SFP transceivers within SONiC
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

SYSLOG_IDENTIFIER = "diag_sfp"

PLATFORM_SPECIFIC_MODULE_NAME = "sfputil"
PLATFORM_SPECIFIC_CLASS_NAME = "SfpUtil"

PLATFORM_ROOT_PATH = '/usr/share/sonic/device'
SONIC_CFGGEN_PATH = '/usr/local/bin/sonic-cfggen'
HWSKU_KEY = 'DEVICE_METADATA.localhost.hwsku'
PLATFORM_KEY = 'DEVICE_METADATA.localhost.platform'

# Global platform-specific sfputil class instance
platform_sfputil = None


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


# ========================== Methods for printing ==========================


# Convert arraw of raw bytes into pretty-printed string
def raw_bytes_to_string_pretty(raw_bytes):
    hexstr = ""

    for i in range(0, len(raw_bytes)):
        if i > 0 and (i % 8) == 0:
            hexstr += " "

        if i > 0 and (i % 16) == 0:
            hexstr += "\n"

        hexstr += raw_bytes[i]
        hexstr += " "

    return hexstr


# Recursively convert dictionary into pretty-printed string
def dict_to_string_pretty(in_dict, indent=0):
    if len(in_dict) == 0:
        return ""

    key = sorted(in_dict)[0]
    val = in_dict[key]

    if isinstance(val, dict):
        output = "%s%s:\n" % ('\t' * indent, key) + dict_to_string_pretty(val, indent + 1)
    else:
        output = "%s%s: %s\n" % ('\t' * indent, key, val)

    return output + dict_to_string_pretty({i:in_dict[i] for i in in_dict if i != key}, indent)


# Recursively convert dictionary into comma-separated string of 'key:value'
def dict_to_string_comma_separated(in_dict, key_blacklist, elemprefix, first=True):
    if len(in_dict) == 0:
        return ""

    output = ""
    key = sorted(in_dict)[0]
    val = in_dict[key]

    if key in key_blacklist:
        return ""

    if not first:
        output += ","
    else:
        first = False

    if isinstance(val, dict):
        output += dict_to_string_comma_separated(val, key_blacklist, key + '.', True)
    else:
        elemname = elemprefix + key
        output += elemname + ':' + str(val)

    return output + dict_to_string_comma_separated(
        {i:in_dict[i] for i in in_dict if i != key},
        key_blacklist, elemprefix, first)


# =============== Getting and printing SFP data ===============


def get_sfp_eeprom_status_string(port, port_sfp_eeprom_status):
    if port_sfp_eeprom_status:
        return "%s: SFP EEPROM detected" % port
    else:
        return "%s: SFP EEPROM not detected" % port


# Returns,
#   port_num if physical
#   logical_port:port_num if logical port and is a ganged port
#   logical_port if logical and not ganged
#
def get_physical_port_name(logical_port, physical_port, ganged):
    port_name = None

    if logical_port == physical_port:
        return logical_port
    elif ganged:
        return logical_port + ":%d (ganged)" % physical_port
    else:
        return logical_port


def logical_port_name_to_physical_port_list(port_name):
    if port_name.startswith("Ethernet"):
        if platform_sfputil.is_logical_port(port_name):
            return platform_sfputil.get_logical_to_physical(port_name)
        else:
            print ("ERROR: Invalid port '%s'\n" % port_name)
            return None
    else:
        return [int(port_name)]


def print_all_valid_port_values():
    print("Valid values for port: %s\n" % str(platform_sfputil.logical))


# Returns multi-line string of pretty SFP port EEPROM data
def port_eeprom_data_string_pretty(logical_port_name, dump_dom):
    result = ""
    ganged = False
    i = 1

    physical_port_list = logical_port_name_to_physical_port_list(logical_port_name)
    if physical_port_list is None:
        print ("ERROR: No physical ports found for logical port '%s'\n" % logical_port_name)
        return ""

    if len(physical_port_list) > 1:
        ganged = True

    for physical_port in physical_port_list:
        port_name = get_physical_port_name(logical_port_name, i, ganged)
        if not platform_sfputil.get_presence(physical_port):
            eeprom_dict = None
        else:
            eeprom_dict = platform_sfputil.get_eeprom_dict(physical_port)

        if eeprom_dict is not None:
            eeprom_iface_dict = eeprom_dict.get('interface')
            iface_data_dict = eeprom_iface_dict.get('data')
            result += get_sfp_eeprom_status_string(port_name, True)
            result += "\n"
            result += dict_to_string_pretty(iface_data_dict, 1)

            if dump_dom:
                eeprom_dom_dict = eeprom_dict.get('dom')
                if eeprom_dom_dict is not None:
                    dom_data_dict = eeprom_dom_dict.get('data')
                    if dom_data_dict is not None:
                        result += dict_to_string_pretty(dom_data_dict, 1)
        else:
            result += get_sfp_eeprom_status_string(port_name, False)
            result += "\n"

        result += "\n"
        i += 1

        return result


# Returns single-line string of pretty SFP port EEPROM data
# Nested dictionary items are prefixed using dot-notation
def port_eeprom_data_string_pretty_oneline(logical_port_name,
                                           ifdata_blacklist,
                                           domdata_blacklist,
                                           dump_dom):
    result = ""
    ganged = False
    i = 1

    physical_port_list = logical_port_name_to_physical_port_list(logical_port_name)
    if physical_port_list is None:
        print ("ERROR: No physical ports found for logical port '%s'\n" % logical_port_name)
        return ""

    if len(physical_port_list) > 1:
        ganged = True

    for physical_port in physical_port_list:
        if not platform_sfputil.get_presence(physical_port):
            eeprom_dict = None
        else:
            eeprom_dict = platform_sfputil.get_eeprom_dict(physical_port)

        # Only print detected sfp ports for oneline
        if eeprom_dict is not None:
            eeprom_iface_dict = eeprom_dict.get('interface')
            iface_data_dict = eeprom_iface_dict.get('data')
            result += "port:%s," % get_physical_port_name(logical_port_name, i, ganged)
            result += dict_to_string_comma_separated(iface_data_dict, ifdata_blacklist, "")

            if dump_dom:
                eeprom_dom_dict = eeprom_dict.get('dom')
                if eeprom_dom_dict is not None:
                    dom_data_dict = eeprom_dom_dict.get('data')
                    if dom_data_dict is not None:
                        result += dict_to_string_comma_separated(
                            dom_data_dict, domdata_blacklist, "")

        result += "\n"
        i += 1

    return result


def port_eeprom_data_raw_string_pretty(logical_port_name):
    result = ""
    ganged = False
    i = 1

    physical_port_list = logical_port_name_to_physical_port_list(logical_port_name)
    if physical_port_list is None:
        print ("ERROR: No physical ports found for logical port '%s'\n" % logical_port_name)
        return ""

    if len(physical_port_list) > 1:
        ganged = True

    for physical_port in physical_port_list:
        port_name = get_physical_port_name(logical_port_name, i, ganged)
        if not platform_sfputil.get_presence(physical_port):
            eeprom_raw = None
        else:
            eeprom_raw = platform_sfputil.get_eeprom_raw(physical_port)

        if eeprom_raw is None:
            result += get_sfp_eeprom_status_string(port_name, False)
            result += "\n"
        else:
            result += get_sfp_eeprom_status_string(port_name, True)
            result += "\n"
            result += raw_bytes_to_string_pretty(eeprom_raw)

        result += "\n"
        i += 1

    return result


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


# Returns path to port config file
def get_path_to_port_config_file():
    # Get platform and hwsku
    (platform, hwsku) = get_platform_and_hwsku()

    # Load platform module from source
    platform_path = "/".join([PLATFORM_ROOT_PATH, platform])
    hwsku_path = "/".join([platform_path, hwsku])

    # First check for the presence of the new 'port_config.ini' file
    port_config_file_path = "/".join([hwsku_path, "port_config.ini"])
    if not os.path.isfile(port_config_file_path):
        # port_config.ini doesn't exist. Try loading the legacy 'portmap.ini' file
        port_config_file_path = "/".join([hwsku_path, "portmap.ini"])

    return port_config_file_path


# Loads platform specific sfputil module from source
def load_platform_sfputil():
    global platform_sfputil

    # Get platform and hwsku
    (platform, hwsku) = get_platform_and_hwsku()

    # Load platform module from source
    platform_path = "/".join([PLATFORM_ROOT_PATH, platform])
    hwsku_path = "/".join([platform_path, hwsku])

    try:
        module_file = "/".join([platform_path, "plugins", PLATFORM_SPECIFIC_MODULE_NAME + ".py"])
        module = imp.load_source(PLATFORM_SPECIFIC_MODULE_NAME, module_file)
    except IOError, e:
        log_error("ERROR to load platform module '%s': %s" % (PLATFORM_SPECIFIC_MODULE_NAME, str(e)), True)
        return -1

    try:
        platform_sfputil_class = getattr(module, PLATFORM_SPECIFIC_CLASS_NAME)
        platform_sfputil = platform_sfputil_class()
    except AttributeError, e:
        log_error("ERROR to instantiate '%s' class: %s" % (PLATFORM_SPECIFIC_CLASS_NAME, str(e)), True)
        return -2

    return 0


# ==================== CLI commands and groups ====================


# This is our main entrypoint - the main 'sfputil' command
def init():
    """sfputil - Command line utility for managing SFP transceivers"""

    # Load platform-specific sfputil class
    err = load_platform_sfputil()
    if err != 0:
	return

    # Load port info
    try:
        port_config_file_path = get_path_to_port_config_file()
        platform_sfputil.read_porttab_mappings(port_config_file_path)
    except Exception, e:
        log_error("ERROR reading port info (%s)" % str(e), True)
	return 


# 'eeprom' subcommand
def eeprom():
    print("Display EEPROM data of SFP transceiver(s)\n")
    logical_port_list = []
    output = ""

    # Create a list containing the logical port names of all ports we're interested in
    logical_port_list = platform_sfputil.logical

    for logical_port_name in logical_port_list:
         output += port_eeprom_data_string_pretty(logical_port_name, True)

    print output


# 'presence' subcommand
def presence():
    print ("Display presence of SFP transceiver(s)\n")
    table_header = ["Port", "Presence"]
    logical_port_list = []
    output_table = []

    # Create a list containing the logical port names of all ports we're interested in
    logical_port_list = platform_sfputil.logical

    for logical_port_name in logical_port_list:
        ganged = False
        i = 1

        physical_port_list = logical_port_name_to_physical_port_list(logical_port_name)
        if physical_port_list is None:
            print("ERROR: No physical ports found for logical port '%s'\n" % logical_port_name)
            return

        if len(physical_port_list) > 1:
            ganged = True

        for physical_port in physical_port_list:
            port_name = get_physical_port_name(logical_port_name, i, ganged)

            try:
                presence = platform_sfputil.get_presence(physical_port)
            except NotImplementedError:
                print ("This functionality is currently not implemented for this platform\n")
		return

            if presence:
                output_table.append([port_name, "Present"])
            else:
                output_table.append([port_name, "Not present"])

            i += 1

    print tabulate(output_table, table_header, tablefmt="simple")


# 'lpmode' subcommand
def lpmode():
    print "Display low-power mode status of SFP transceiver(s)\n"
    logical_port_list = []
    output_table = []
    table_header = ["Port", "Low-power Mode"]

    # Create a list containing the logical port names of all ports we're interested in
    logical_port_list = platform_sfputil.logical

    for logical_port_name in logical_port_list:
        ganged = False
        i = 1

        physical_port_list = logical_port_name_to_physical_port_list(logical_port_name)
        if physical_port_list is None:
            print "ERROR: No physical ports found for logical port '%s'\n" % logical_port_name
            return

        if len(physical_port_list) > 1:
            ganged = True

        for physical_port in physical_port_list:
            port_name = get_physical_port_name(logical_port_name, i, ganged)

            try:
                lpmode = platform_sfputil.get_low_power_mode(physical_port)
            except NotImplementedError:
                print "This functionality is currently not implemented for this platform\n"
		return

            if lpmode:
                output_table.append([port_name, "On"])
            else:
                output_table.append([port_name, "Off"])

            i += 1

    print tabulate(output_table, table_header, tablefmt='simple')


# 'version' subcommand
def version():
    """Display version info"""
    print "diag_sfp version {0}".format(VERSION)


# ==================== Main Logic ====================
if len(sys.argv) != 2:
        print "Usage: <script> <logfile>"
        print len(sys.argv)
        sys.exit(1)

LOG_FILE=sys.argv[1]
stdout_org = sys.stdout
sys.stdout = open(LOG_FILE, "w+")

init()
version()
lpmode()
presence()
eeprom()

sys.stdout = stdout_org

diagUtil=DiagUtil()
diagUtil.check_log_file_err_msg('sfp', LOG_FILE)

