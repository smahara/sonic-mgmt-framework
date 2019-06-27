#!/usr/bin/env python

import os
import commands
import sys, getopt
import logging
import re
import subprocess
import shutil
import time
import pddfparse
from collections import namedtuple

PLATFORM_ROOT_PATH = '/usr/share/sonic/device'
SONIC_CFGGEN_PATH = '/usr/local/bin/sonic-cfggen'
HWSKU_KEY = 'DEVICE_METADATA.localhost.hwsku'
PLATFORM_KEY = 'DEVICE_METADATA.localhost.platform'

PROJECT_NAME = 'PDDF'
version = '1.1'
verbose = False
DEBUG = False
args = []
ALL_DEVICE = {}               
FORCE = 0

if DEBUG == True:
    print sys.argv[0]
    print 'ARGV      :', sys.argv[1:]   

def main():
    global DEBUG
    global args
    global FORCE
        
    if len(sys.argv)<2:
        show_help()
         
    options, args = getopt.getopt(sys.argv[1:], 'hdf', ['help',
                                                       'debug',
                                                       'force',
                                                          ])
    if DEBUG == True:                                                           
        print options
        print args
        print len(sys.argv)
            
    for opt, arg in options:
        if opt in ('-h', '--help'):
            show_help()
        elif opt in ('-d', '--debug'):            
            DEBUG = True
            logging.basicConfig(level=logging.INFO)
        elif opt in ('-f', '--force'): 
            FORCE = 1
        else:
            logging.info('no option')                          
    for arg in args:            
        if arg == 'install':
            do_install()
        elif arg == 'clean':
           do_uninstall()
        else:
            show_help()
            
    return 0              
        
def show_help():
    print __doc__ % {'scriptName' : sys.argv[0].split("/")[-1]}
    sys.exit(0)

def my_log(txt):
    if DEBUG == True:
        print "[PDDF]"+txt    
    return
    
def log_os_system(cmd, show):
    logging.info('Run :'+cmd)  
    status, output = commands.getstatusoutput(cmd)    
    my_log (cmd +"with result:" + str(status))
    my_log ("      output:"+output)    
    if status:
        logging.info('Failed :'+cmd)
        if show:
            print('Failed :'+cmd)
    return  status, output
            
def driver_check():
    ret, lsmod = log_os_system("lsmod| grep pddf", 0)
    logging.info('mods:'+lsmod)
    if len(lsmod) ==0:
        return False   
    return True

kos = [
'modprobe i2c-ismt',
'modprobe i2c-i801',
'modprobe i2c_dev',
'modprobe i2c_mux_pca954x force_deselect_on_exit=1',
'modprobe pddf_client_module'  ,
'modprobe optoe'      ,
'modprobe pddf_cpld_module'  ,
'modprobe pddf_xcvr_module',
'modprobe pddf_mux_module'  ,
'modprobe pddf_cpld_driver' ,
'modprobe pddf_xcvr_driver_module' ,
'modprobe pddf_psu_driver_module' ,
'modprobe pddf_psu_module' ,
'modprobe pddf_fan_driver_module' ,
'modprobe pddf_fan_module' ,
'modprobe pddf_led_module' ,
'modprobe pddf_sysstatus_module'
]

devs = []

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

def get_path_to_device_plugin():
    # Get platform and hwsku
    (platform, hwsku) = get_platform_and_hwsku()

    # Load platform module from source
    platform_path = "/".join([PLATFORM_ROOT_PATH, platform])
    hwsku_path = "/".join([platform_path, hwsku])
    plugin_path = "/".join([platform_path, "plugins"])

    return plugin_path

def get_path_to_pddf_plugin():
    pddf_path = "/".join([PLATFORM_ROOT_PATH, "pddf/plugins"])
    return pddf_path

def config_pddf_utils():
    device_path = get_path_to_device_plugin()
    pddf_path = get_path_to_pddf_plugin()

    backup_path = "/".join([device_path, "orig"])

    if os.path.exists(backup_path) is False:
        os.mkdir(backup_path)
    log_os_system("mv "+device_path+"/*.*"+" "+backup_path, 0)
    for item in os.listdir(pddf_path):
        shutil.copy(pddf_path+"/"+item, device_path+"/"+item)
    
    shutil.copy('/usr/local/bin/pddfparse.py', device_path+"/pddfparse.py")

    return 0

def cleanup_pddf_utils():
    device_path = get_path_to_device_plugin()
    backup_path = "/".join([device_path, "orig"])
    if os.path.exists(backup_path) is True:
        for item in os.listdir(device_path):
            if os.path.isdir(device_path+"/"+item) is False:
                os.remove(device_path+"/"+item)

        status = log_os_system("mv "+backup_path+"/*"+" "+device_path, 1)
        os.rmdir(backup_path)
    else:
        print "\nERR: Unable to locate original device files...\n" 
    return 0

def driver_install():
    global FORCE
    status, output = log_os_system("depmod", 1)
    for i in range(0,len(kos)):
        status, output = log_os_system(kos[i], 1)
        if status:
            if FORCE == 0:        
                return status       

    output = config_pddf_utils()

    # trigger the pddfparse script for FAN, PSU, CPLD, MUX, etc
    status = pddfparse.create_pddf_devices()

    if status:
        if FORCE == 0:
            return status


    return 0
    
def driver_uninstall():
    global FORCE

    status = cleanup_pddf_utils()

    for i in range(0,len(kos)):
        rm = kos[-(i+1)].replace("modprobe", "modprobe -rq")
        rm = rm.replace("insmod", "rmmod")        
        status, output = log_os_system(rm, 1)
        if status:
            if FORCE == 0:        
                return status              
    return 0

def device_uninstall():
    return 
        
def do_install():
    print "Checking system...."
    print "No driver, installing...."    
    status = driver_install()
    if status:
        return  status
    return
    
def do_uninstall():
    print "Checking system...."
    if driver_check()== False :
        print PROJECT_NAME.upper() +" has no driver installed...."
    else:
        print "Remove all the devices..."
        pddfparse.delete_pddf_devices()

        print "Removing installed driver...."
        status = driver_uninstall()
        if status:
            if FORCE == 0:        
                return  status                          
    return       

if __name__ == "__main__":
    main()
