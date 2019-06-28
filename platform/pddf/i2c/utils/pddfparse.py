#!/usr/bin/env python
import sys
import json
import re
import argparse
import subprocess
import glob
import os

cache={}
SONIC_CFGGEN_PATH = '/usr/local/bin/sonic-cfggen'
HWSKU_KEY = 'DEVICE_METADATA.localhost.hwsku'
PLATFORM_KEY = 'DEVICE_METADATA.localhost.platform'

dirname=os.path.dirname(os.path.realpath(__file__))

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

if not os.path.exists("/usr/share/sonic/platform"):
    platform, hwsku = get_platform_and_hwsku()
    os.symlink("/usr/share/sonic/device/"+platform, "/usr/share/sonic/platform")

with open('/usr/share/sonic/platform/pddf/pddf-device.json') as f:
          data = json.load(f)
f.close()

#################################################################################################################################
#   GENERIC DEFS
#################################################################################################################################
def get_dev_idx(tree, dev, ops):
	parent=dev['dev_info']['virt_parent']
	pdev=tree[parent]
	
	return pdev['dev_attr']['dev_idx']


def get_path(target, attr):
    aa = target + attr

    if aa in cache:
        return cache[aa]

    op={ "cmd": "show_attr", "target":target, "attr":attr }
    #print data[target]
    str = dev_parse(data, data[target], op)
    #print "[test] str is %s" %str
    str = str.rstrip('\n')
    cache[aa]=str
    return str


def get_device_type(key):
    return data[key]['dev_info']['device_type']

def get_platform():
    return data['PLATFORM']



#################################################################################################################################
#   CREATE DEFS
#################################################################################################################################
def create_device(tree, attr, path, ops):

	for key in attr.keys():
		cmd="echo '%s' > /sys/kernel/%s/%s"%(attr[key], path, key)
		#print cmd
		os.system(cmd)

def create_psu_i2c_device(tree, dev, ops):
    if dev['i2c']['topo_info']['dev_type'] in tree['PLATFORM']['drivers']['PSU']:
	create_device(tree, dev['i2c']['topo_info'], "pddf/devices/psu/i2c", ops)
        cmd= "echo '%s' > /sys/kernel/pddf/devices/psu/i2c/i2c_name"%(dev['dev_info']['device_name'])
        #print cmd
        os.system(cmd)
	cmd= "echo '%s'  > /sys/kernel/pddf/devices/psu/i2c/psu_idx\n"%( get_dev_idx(tree, dev, ops))
        #print cmd
        os.system(cmd)
	for attr in dev['i2c']['attr_list']:
                create_device(tree, attr, "pddf/devices/psu/i2c", ops)
                cmd= "echo 'add' > /sys/kernel/pddf/devices/psu/i2c/attr_ops\n"
                #print cmd
                os.system(cmd)

	cmd = "echo 'add' > /sys/kernel/pddf/devices/psu/i2c/dev_ops\n"
	#print cmd
        os.system(cmd)
    else:
        cmd = "echo %s 0x%x > /sys/bus/i2c/devices/i2c-%d/new_device" % (dev['i2c']['topo_info']['dev_type'], int(dev['i2c']['topo_info']['dev_addr'], 0), int(dev['i2c']['topo_info']['parent_bus'], 0))
        #print cmd
        os.system(cmd)


    ##os.system("sleep 1")


def create_psu_bmc_device(tree, dev, ops):
	print ""


def create_psu_device(tree, dev, ops):
	#if 'i2c' in dev:
		create_psu_i2c_device(tree, dev, ops )
                return

	#if 'bmc' in dev:
		#create_psu_bmc_device(tree, dev)
		
def create_fan_device(tree, dev, ops):
    if dev['i2c']['topo_info']['dev_type'] in tree['PLATFORM']['drivers']['FAN']:
        create_device(tree, dev['i2c']['topo_info'], "pddf/devices/fan/i2c", ops)
        cmd= "echo '%s' > /sys/kernel/pddf/devices/fan/i2c/i2c_name"%(dev['dev_info']['device_name'])
        #print cmd
        os.system(cmd)
        create_device(tree, dev['i2c']['dev_attr'], "pddf/devices/fan/i2c", ops)
        for attr in dev['i2c']['attr_list']:
            create_device(tree, attr, "pddf/devices/fan/i2c", ops)
            cmd= "echo 'add' > /sys/kernel/pddf/devices/fan/i2c/attr_ops\n"
            #print cmd
            os.system(cmd)

        cmd= "echo 'add' > /sys/kernel/pddf/devices/fan/i2c/dev_ops\n"
        #print cmd
        os.system(cmd)
    else:
        cmd= "echo %s 0x%x > /sys/bus/i2c/devices/i2c-%d/new_device\n" % (dev['i2c']['topo_info']['dev_type'], int(dev['i2c']['topo_info']['dev_addr'], 0), int(dev['i2c']['topo_info']['parent_bus'], 0))
        #print cmd
        os.system(cmd)

    #os.system("sleep 1")

def create_temp_sensor_device(tree, dev, ops):
    # NO PDDF driver for temp_sensors device
    #if dev['i2c']['topo_info']['dev_type'] in tree['PLATFORM']['drivers']['TEMP_SENSOR']:
        #create_device(tree, dev['i2c']['topo_info'], "pddf/devices/fan/i2c", ops)
        #create_device(tree, dev['i2c']['dev_attr'], "pddf/devices/fan/i2c", ops)
        #for attr in dev['i2c']['attr_list']:
            #create_device(tree, attr, "pddf/devices/fan/i2c", ops)
            #print "echo 'add' > /sys/kernel/pddf/devices/fan/i2c/attr_ops\n"

        #print "echo 'add' > /sys/kernel/pddf/devices/fan/i2c/dev_ops\n"
    #else:
        cmd= "echo %s 0x%x > /sys/bus/i2c/devices/i2c-%d/new_device\n" % (dev['i2c']['topo_info']['dev_type'], int(dev['i2c']['topo_info']['dev_addr'], 0), int(dev['i2c']['topo_info']['parent_bus'], 0))
        #print cmd
        os.system(cmd)

        #os.system("sleep 1")


def create_cpld_device(tree, dev, ops):
    if dev['i2c']['topo_info']['dev_type'] in tree['PLATFORM']['drivers']['CPLD']:
	create_device(tree, dev['i2c']['topo_info'], "pddf/devices/cpld", ops)
        cmd= "echo '%s' > /sys/kernel/pddf/devices/cpld/i2c_name"%(dev['dev_info']['device_name'])
        #print cmd
        os.system(cmd)
	#create_device(tree, dev['i2c']['dev_attr'], "pddf/devices/cpld", ops)
        # TODO: If attributes are provided then, use 'create_device' for them too
	cmd= "echo 'add' > /sys/kernel/pddf/devices/cpld/dev_ops\n"
        #print cmd
        os.system(cmd)
    else:
        cmd= "echo %s 0x%x > /sys/bus/i2c/devices/i2c-%d/new_device\n" % (dev['i2c']['topo_info']['dev_type'], int(dev['i2c']['topo_info']['dev_addr'], 0), int(dev['i2c']['topo_info']['parent_bus'], 0))
        #print cmd
        os.system(cmd)

    #os.system("sleep 1")


def create_mux_device(tree, dev, ops):
	create_device(tree, dev['i2c']['topo_info'], "pddf/devices/mux", ops)
        cmd= "echo '%s' > /sys/kernel/pddf/devices/mux/i2c_name"%(dev['dev_info']['device_name'])
        #print cmd
        os.system(cmd)
	create_device(tree, dev['i2c']['dev_attr'], "pddf/devices/mux", ops)
	cmd= "echo 'add' > /sys/kernel/pddf/devices/mux/dev_ops\n"
        #print cmd
        os.system(cmd)
        #os.system("sleep 1")

def create_xcvr_i2c_device(tree, dev, ops):
    if dev['i2c']['topo_info']['dev_type'] in tree['PLATFORM']['drivers']['PORT_MODULE']:
        create_device(tree, dev['i2c']['topo_info'], "pddf/devices/xcvr/i2c", ops)
        cmd= "echo '%s' > /sys/kernel/pddf/devices/xcvr/i2c/i2c_name"%(dev['dev_info']['device_name'])
        #print cmd
        os.system(cmd)
        #create_device(tree, dev['i2c']['dev_attr'], "pddf/devices/psu/i2c")
        cmd="echo '%s'  > /sys/kernel/pddf/devices/xcvr/i2c/dev_idx\n"%( get_dev_idx(tree, dev, ops))
        #print cmd
        os.system(cmd)
        for attr in dev['i2c']['attr_list']:
            create_device(tree, attr, "pddf/devices/xcvr/i2c", ops)
            cmd="echo 'add' > /sys/kernel/pddf/devices/xcvr/i2c/attr_ops\n"
            #print cmd
            os.system(cmd)

        cmd="echo 'add' > /sys/kernel/pddf/devices/xcvr/i2c/dev_ops\n"
        #print cmd
        os.system(cmd)
    else:
        cmd="echo %s 0x%x > /sys/bus/i2c/devices/i2c-%d/new_device\n" % (dev['i2c']['topo_info']['dev_type'], int(dev['i2c']['topo_info']['dev_addr'], 0), int(dev['i2c']['topo_info']['parent_bus'], 0))
        #print cmd
        os.system(cmd)

    #os.system("sleep 1")

def create_xcvr_bmc_device(tree, dev, ops):
        print ""

def create_xcvr_device(tree, dev, ops):
        #if 'i2c' in dev:
        create_xcvr_i2c_device(tree, dev, ops )
        return
        #if 'bmc' in dev:
        #create_psu_bmc_device(tree, dev)

def create_sysstatus_device(tree, dev, ops):
    for attr in dev['attr_list']:
        cmd= "echo '%s' > /sys/kernel/pddf/devices/sysstatus/i2c_name"%(dev['dev_info']['device_name'])
        #print cmd
        os.system(cmd)
        create_device(tree, attr, "pddf/devices/sysstatus", ops)
        cmd= "echo 'add' > /sys/kernel/pddf/devices/sysstatus/attr_ops\n\n"
        #print cmd
        os.system(cmd)

def create_eeprom_device(tree, dev, ops):
    if "EEPROM" in tree['PLATFORM']['drivers'] and dev['i2c']['topo_info']['dev_type'] in tree['PLATFORM']['drivers']['EEPROM']:
        create_device(tree, dev['i2c']['topo_info'], "pddf/devices/eeprom/i2c", ops)
        cmd= "echo '%s' > /sys/kernel/pddf/devices/eeprom/i2c/i2c_name"%(dev['dev_info']['device_name'])
        #print cmd
        os.system(cmd)
        create_device(tree, dev['i2c']['dev_attr'], "pddf/devices/eeprom/i2c", ops)
        cmd = "echo 'add' > /sys/kernel/pddf/devices/eeprom/i2c/dev_ops\n"
        #print cmd
        os.system(cmd)

    else:
        cmd= "echo %s 0x%x > /sys/bus/i2c/devices/i2c-%d/new_device\n" % (dev['i2c']['topo_info']['dev_type'], int(dev['i2c']['topo_info']['dev_addr'], 0), int(dev['i2c']['topo_info']['parent_bus'], 0))
        #print cmd
        os.system(cmd)

    #os.system("sleep 1")

#################################################################################################################################
#   DELETE DEFS
#################################################################################################################################
def delete_eeprom_device(tree, dev, ops):
    if "EEPROM" in tree['PLATFORM']['drivers'] and dev['i2c']['topo_info']['dev_type'] in tree['PLATFORM']['drivers']['EEPROM']:
        cmd= "echo '%s' > /sys/kernel/pddf/devices/eeprom/i2c/i2c_name"%(dev['dev_info']['device_name'])
        #print cmd
        os.system(cmd)
        cmd = "echo 'delete' > /sys/kernel/pddf/devices/eeprom/i2c/dev_ops\n"
        #print cmd
        os.system(cmd)
    else:
        cmd= "echo 0x%x > /sys/bus/i2c/devices/i2c-%d/delete_device\n" % (int(dev['i2c']['topo_info']['dev_addr'], 0), int(dev['i2c']['topo_info']['parent_bus'], 0))
        #print cmd
        os.system(cmd)
    #os.system("sleep 1")

def delete_sysstatus_device(tree, dev, ops):
    # NOT A PHYSICAL DEVICE.... rmmod on module would remove all the artifacts
    pass

    #for attr in dev['attr_list']:
        #cmd= "echo '%s' > /sys/kernel/pddf/devices/sysstatus/i2c_name"%(dev['dev_info']['device_name'])
        ##print cmd
        #os.system(cmd)
        #cmd= "echo 'delete' > /sys/kernel/pddf/devices/sysstatus/attr_ops\n\n"
        ##print cmd
        #os.system(cmd)

def delete_xcvr_i2c_device(tree, dev, ops):
    if dev['i2c']['topo_info']['dev_type'] in tree['PLATFORM']['drivers']['PORT_MODULE']:
        cmd= "echo '%s' > /sys/kernel/pddf/devices/xcvr/i2c/i2c_name"%(dev['dev_info']['device_name'])
        #print cmd
        os.system(cmd)
        cmd="echo 'delete' > /sys/kernel/pddf/devices/xcvr/i2c/dev_ops\n"
        #print cmd
        os.system(cmd)
    else:
        cmd="echo 0x%x > /sys/bus/i2c/devices/i2c-%d/delete_device\n" % (int(dev['i2c']['topo_info']['dev_addr'], 0), int(dev['i2c']['topo_info']['parent_bus'], 0))
        #print cmd
        os.system(cmd)
    #os.system("sleep 1")

def delete_xcvr_device(tree, dev, ops):
    delete_xcvr_i2c_device(tree, dev, ops)
    return

def delete_mux_device(tree, dev, ops):
        cmd= "echo '%s' > /sys/kernel/pddf/devices/mux/i2c_name"%(dev['dev_info']['device_name'])
        #print cmd
        os.system(cmd)
	cmd= "echo 'delete' > /sys/kernel/pddf/devices/mux/dev_ops\n"
        #print cmd
        os.system(cmd)
        #os.system("sleep 1")

def delete_cpld_device(tree, dev, ops):
    if dev['i2c']['topo_info']['dev_type'] in tree['PLATFORM']['drivers']['CPLD']:
        cmd= "echo '%s' > /sys/kernel/pddf/devices/cpld/i2c_name"%(dev['dev_info']['device_name'])
        #print cmd
        os.system(cmd)
	cmd= "echo 'delete' > /sys/kernel/pddf/devices/cpld/dev_ops\n"
        #print cmd
        os.system(cmd)
    else:
        cmd= "echo 0x%x > /sys/bus/i2c/devices/i2c-%d/delete_device\n" % (int(dev['i2c']['topo_info']['dev_addr'], 0), int(dev['i2c']['topo_info']['parent_bus'], 0))
        #print cmd
        os.system(cmd)
    #os.system("sleep 1")

def delete_temp_sensor_device(tree, dev, ops):
    # NO PDDF driver for temp_sensors device
    #if dev['i2c']['topo_info']['dev_type'] in tree['PLATFORM']['drivers']['TEMP_SENSOR']:
        #cmd= "echo '%s' > /sys/kernel/pddf/devices/temp_sensor/i2c/i2c_name"%(dev['dev_info']['device_name'])
        ##print cmd
        #os.system(cmd)
        #cmd= "echo 'add' > /sys/kernel/pddf/devices/temp_sensor/i2c/dev_ops\n"
        ##print cmd
        #os.system(cmd)
    #else:
        cmd= "echo 0x%x > /sys/bus/i2c/devices/i2c-%d/delete_device\n" % (int(dev['i2c']['topo_info']['dev_addr'], 0), int(dev['i2c']['topo_info']['parent_bus'], 0))
        #print cmd
        os.system(cmd)

        #os.system("sleep 1")

def delete_fan_device(tree, dev, ops):
    if dev['i2c']['topo_info']['dev_type'] in tree['PLATFORM']['drivers']['FAN']:
        cmd= "echo '%s' > /sys/kernel/pddf/devices/fan/i2c/i2c_name"%(dev['dev_info']['device_name'])
        #print cmd
        os.system(cmd)
        cmd= "echo 'delete' > /sys/kernel/pddf/devices/fan/i2c/dev_ops\n"
        #print cmd
        os.system(cmd)
    else:
        cmd= "echo 0x%x > /sys/bus/i2c/devices/i2c-%d/delete_device\n" % (int(dev['i2c']['topo_info']['dev_addr'], 0), int(dev['i2c']['topo_info']['parent_bus'], 0))
        #print cmd
        os.system(cmd)
    #os.system("sleep 1")


def delete_psu_i2c_device(tree, dev, ops):
    if dev['i2c']['topo_info']['dev_type'] in tree['PLATFORM']['drivers']['PSU']:
        cmd= "echo '%s' > /sys/kernel/pddf/devices/psu/i2c/i2c_name"%(dev['dev_info']['device_name'])
        #print cmd
        os.system(cmd)
	cmd = "echo 'delete' > /sys/kernel/pddf/devices/psu/i2c/dev_ops\n"
	#print cmd
        os.system(cmd)
    else:
        cmd = "echo 0x%x > /sys/bus/i2c/devices/i2c-%d/delete_device\n" % (int(dev['i2c']['topo_info']['dev_addr'], 0), int(dev['i2c']['topo_info']['parent_bus'], 0))
        #print cmd
        os.system(cmd)
    #os.system("sleep 1")

def delete_psu_device(tree, dev, ops):
	#if 'i2c' in dev:
	delete_psu_i2c_device(tree, dev, ops )
        return


#################################################################################################################################
#   SHOW ATTRIBIUTES DEFS
#################################################################################################################################
data_sysfs_obj={}

def show_device_sysfs(tree, dev, ops):
    parent=dev['dev_info']['device_parent']
    #print parent
    pdev=tree[parent]
    if pdev['dev_info']['device_parent'] == 'SYSTEM':
        return "/sys/bus/i2c/devices/"+"i2c-%d"%int(pdev['i2c']['topo_info']['dev_addr'], 0)
    return show_device_sysfs(tree, pdev, ops) + "/" + "i2c-%d" % int(dev['i2c']['topo_info']['parent_bus'], 0)


# This is alid for 'at24' type of EEPROM devices. Only one attribtue 'eeprom' 
def show_attr_eeprom_device(tree, dev, ops):
    str = ""
    attr_name=ops['attr']
    attr_list=dev['i2c']['attr_list']
    KEY="eeprom"
    dsysfs_path=""

    if not KEY in data_sysfs_obj:
        data_sysfs_obj[KEY]=[]

    for attr in attr_list:
        if attr_name == attr['attr_name'] or attr_name == 'all':
            #print show_device_sysfs(tree, dev, ops)+"/%d-00%x" %(int(dev['i2c']['topo_info']['parent_bus'], 0), int(dev['i2c']['topo_info']['dev_addr'], 0))+"/%s"%attr['attr_name']
            dsysfs_path = show_device_sysfs(tree, dev, ops)+"/%d-00%x" %(int(dev['i2c']['topo_info']['parent_bus'], 0), int(dev['i2c']['topo_info']['dev_addr'], 0))+"/%s"%attr['attr_name']
            if not dsysfs_path in data_sysfs_obj[KEY]:
                data_sysfs_obj[KEY].append(dsysfs_path)
            str += dsysfs_path+"\n"
    return str


def show_attr_mux_device(tree, dev, ops):
    ret = ""
    KEY="mux"
    if not KEY in data_sysfs_obj:
        data_sysfs_obj[KEY]=[]

    return ret

def show_attr_psu_i2c_device(tree, dev, ops):
    target=ops['target']
    attr_name=ops['attr']
    str = ""
    KEY="psu"
    dsysfs_path=""

    if not KEY in data_sysfs_obj:
        data_sysfs_obj[KEY]=[]

    if target == 'all' or target == dev['dev_info']['virt_parent'] :
        attr_list=dev['i2c']['attr_list']
        for attr in attr_list:
            if attr_name == attr['attr_name'] or attr_name == 'all' :
                #print show_device_sysfs(tree, dev, ops)+"/%d-00%x" %(int(dev['i2c']['topo_info']['parent_bus'], 0), int(dev['i2c']['topo_info']['dev_addr'], 0))+"/%s"%attr['attr_name']
                dsysfs_path = show_device_sysfs(tree, dev, ops)+"/%d-00%x" %(int(dev['i2c']['topo_info']['parent_bus'], 0), int(dev['i2c']['topo_info']['dev_addr'], 0))+"/%s"%attr['attr_name']
                if not dsysfs_path in data_sysfs_obj[KEY]:
                    data_sysfs_obj[KEY].append(dsysfs_path)
                str += dsysfs_path+"\n"
    return str


def show_attr_psu_device(tree, dev, ops):
    return show_attr_psu_i2c_device(tree, dev, ops )


def show_attr_fan_device(tree, dev, ops):
    str = ""
    attr_name=ops['attr']
    attr_list=dev['i2c']['attr_list']
    KEY="fan"
    dsysfs_path=""

    if not KEY in data_sysfs_obj:
        data_sysfs_obj[KEY]=[]


    for attr in attr_list:
        if attr_name == attr['attr_name'] or attr_name == 'all':
            #print show_device_sysfs(tree, dev, ops)+"/%d-00%x" %(int(dev['i2c']['topo_info']['parent_bus'], 0), int(dev['i2c']['topo_info']['dev_addr'], 0))+"/%s"%attr['attr_name']
            dsysfs_path= show_device_sysfs(tree, dev, ops)+"/%d-00%x" %(int(dev['i2c']['topo_info']['parent_bus'], 0), int(dev['i2c']['topo_info']['dev_addr'], 0))+"/%s"%attr['attr_name']
            if not dsysfs_path in data_sysfs_obj[KEY]:
                data_sysfs_obj[KEY].append(dsysfs_path)
            str += dsysfs_path+"\n"
    return str

# This is only valid for LM75
def show_attr_temp_sensor_device(tree, dev, ops):
    str = ""
    attr_name=ops['attr']
    attr_list=dev['i2c']['attr_list']
    KEY="temp-sensors"
    dsysfs_path=""

    if not KEY in data_sysfs_obj:
        data_sysfs_obj[KEY]=[]


    for attr in attr_list:
        if attr_name == attr['attr_name'] or attr_name == 'all':
            path = show_device_sysfs(tree, dev, ops)+"/%d-00%x/" %(int(dev['i2c']['topo_info']['parent_bus'], 0), int(dev['i2c']['topo_info']['dev_addr'], 0))
            #print  glob.glob(path+'hwmon/hwmon*/'+attr['attr_name'])
	    if (os.path.exists(path)):
                full_path = glob.glob(path + 'hwmon/hwmon*/' + attr['attr_name'])[0]
                #full_path = path + 'hwmon/hwmon/' + attr['attr_name']
                dsysfs_path=full_path
                if not dsysfs_path in data_sysfs_obj[KEY]:
                    data_sysfs_obj[KEY].append(dsysfs_path)
                str += full_path + "\n"
    return str

def show_attr_sysstatus_device(tree, dev, ops):
    ret = ""
    attr_name=ops['attr']
    attr_list=dev['attr_list']
    KEY="sys-status"
    dsysfs_path=""

    if not KEY in data_sysfs_obj:
        data_sysfs_obj[KEY]=[]


    for attr in attr_list:
       if attr_name == attr['attr_name'] or attr_name == 'all':
          dsysfs_path = "/sys/kernel/pddf/devices/sysstatus/sysstatus_data/" + attr['attr_name']
          if not dsysfs_path in data_sysfs_obj[KEY]:
              data_sysfs_obj[KEY].append(dsysfs_path)
          #print path
          ret += dsysfs_path+"\n"
    return ret


def show_attr_xcvr_i2c_device(tree, dev, ops):
    target=ops['target']
    attr_name=ops['attr']
    str = ""
    dsysfs_path = ""
    KEY="xcvr"
    if not KEY in data_sysfs_obj:
        data_sysfs_obj[KEY]=[]

    if target == 'all' or target == dev['dev_info']['virt_parent'] :
        attr_list=dev['i2c']['attr_list']
        for attr in attr_list:
            if attr_name == attr['attr_name'] or attr_name == 'all' :
                dsysfs_path = show_device_sysfs(tree, dev, ops)+"/%d-00%x" %(int(dev['i2c']['topo_info']['parent_bus'], 0), int(dev['i2c']['topo_info']['dev_addr'], 0))+"/%s"%attr['attr_name']
                if not dsysfs_path in data_sysfs_obj[KEY]:
                    data_sysfs_obj[KEY].append(dsysfs_path)
                str += dsysfs_path+"\n"
    return str


def show_attr_xcvr_device(tree, dev, ops):
    return show_attr_xcvr_i2c_device(tree, dev, ops )

def show_attr_cpld_device(tree, dev, ops):
    ret = ""
    KEY="cpld"
    if not KEY in data_sysfs_obj:
        data_sysfs_obj[KEY]=[]

    return ret


#################################################################################################################################
#   SHOW DEFS
#################################################################################################################################
sysfs_obj={}

def check_led_cmds(tree, key, ops):
        name = ops['target']+'_LED'
        if (ops['target']=='config' or ops['attr']=='all') or (name==tree[key]['dev_info']['device_name'] and ops['attr']==tree[key]['dev_attr']['index']):
            return (True)
        else:
            return (False)

def dump_sysfs_obj(obj, key_type):
	if (key_type == 'keys'):
	    for key in obj.keys():	
	        print key
	    return

        for key in obj:
	    if (key == key_type or key_type == 'all'):
	        print key+":"
                for entry in obj[key]:
                    print "\t"+entry

def add_list_sysfs_obj(obj, KEY, list):
    for sysfs in list:
        if not sysfs in obj[KEY]:
            obj[KEY].append(sysfs)

def sysfs_attr(key, value, path, obj, obj_key):
        sysfs_path="/sys/kernel/%s/%s"%(path, key)
        if not sysfs_path in obj[obj_key]:
                obj[obj_key].append(sysfs_path)


def sysfs_device(tree, attr, path, obj, obj_key):
        for key in attr.keys():
                sysfs_path="/sys/kernel/%s/%s"%(path, key)
                if not sysfs_path in obj[obj_key]:
                        obj[obj_key].append(sysfs_path)

def show_eeprom_device(tree, dev, ops):
	return


def show_mux_device(tree, dev, ops):
        KEY ='mux'
        if not KEY in sysfs_obj:
                sysfs_obj[KEY] = []
                sysfs_device(tree, dev['i2c']['topo_info'], "pddf/devices/mux", sysfs_obj, KEY)
                sysfs_device(tree, dev['i2c']['dev_attr'], "pddf/devices/mux", sysfs_obj, KEY)
                sysfs_path= "/sys/kernel/pddf/devices/mux/dev_ops"
                if not sysfs_path in sysfs_obj[KEY]:
                        sysfs_obj[KEY].append(sysfs_path)
                list=['/sys/kernel/pddf/devices/mux/i2c_type',
                      '/sys/kernel/pddf/devices/mux/i2c_name',
                      '/sys/kernel/pddf/devices/mux/error']
                add_list_sysfs_obj(sysfs_obj, KEY, list)


def show_psu_i2c_device(tree, dev, ops):
    KEY ='psu'
    path='pddf/devices/psu/i2c'
    if dev['i2c']['topo_info']['dev_type'] in tree['PLATFORM']['drivers']['PSU']:
        if not KEY in sysfs_obj:
                sysfs_obj[KEY] = []
                sysfs_device(tree, dev['i2c']['topo_info'], path, sysfs_obj, KEY)
                sysfs_path = "/sys/kernel/pddf/devices/psu/i2c/psu_idx"
                sysfs_obj[KEY].append(sysfs_path)

                for attr in dev['i2c']['attr_list']:
                        sysfs_device(tree, attr, "pddf/devices/psu/i2c", sysfs_obj, KEY)
                        sysfs_path = "/sys/kernel/pddf/devices/psu/i2c/dev_ops"
                        if not sysfs_path in sysfs_obj[KEY]:
                                sysfs_obj[KEY].append(sysfs_path)
                list=['/sys/kernel/pddf/devices/psu/i2c/i2c_type',
                      '/sys/kernel/pddf/devices/fan/i2c/i2c_name',
                      '/sys/kernel/pddf/devices/psu/i2c/error',
                      '/sys/kernel/pddf/devices/psu/i2c/attr_ops']
                add_list_sysfs_obj(sysfs_obj, KEY, list)


def show_psu_device(tree, dev, ops):
        show_psu_i2c_device(tree, dev, ops )
        return

def show_client_device():
    KEY ='client'
    if not KEY in sysfs_obj:
           sysfs_obj[KEY] = []
           list=['/sys/kernel/pddf/devices/showall']
           add_list_sysfs_obj(sysfs_obj, KEY, list)


def show_fan_device(tree, dev, ops):
    KEY ='fan'
    path='pddf/devices/fan/i2c'
    if dev['i2c']['topo_info']['dev_type'] in tree['PLATFORM']['drivers']['FAN']:
        if not KEY in sysfs_obj:
                sysfs_obj[KEY] = []

                sysfs_device(tree, dev['i2c']['topo_info'], path, sysfs_obj, KEY)
                sysfs_device(tree, dev['i2c']['dev_attr'], path, sysfs_obj, KEY)
                for attr in dev['i2c']['attr_list']:
                        sysfs_device(tree, attr, path, sysfs_obj, KEY)
                list=['/sys/kernel/pddf/devices/fan/i2c/i2c_type',
                      '/sys/kernel/pddf/devices/fan/i2c/i2c_name',
                      '/sys/kernel/pddf/devices/fan/i2c/error',
                      '/sys/kernel/pddf/devices/fan/i2c/attr_ops',
                      '/sys/kernel/pddf/devices/fan/i2c/dev_ops']
                add_list_sysfs_obj(sysfs_obj, KEY, list)


def show_temp_sensor_device(tree, dev, ops):
	#path= "/sys/bus/i2c/devices/i2c-%d/new_device\n" % (int(dev['i2c']['topo_info']['parent_bus'], 0))
	#print "temp: "+ path
	return

def show_sysstatus_device(tree, dev, ops):
    KEY ='sysstatus'
    if not KEY in sysfs_obj:
        sysfs_obj[KEY] = []
        for attr in dev['attr_list']:
                sysfs_device(tree, attr, "pddf/devices/sysstatus", sysfs_obj, KEY)
                sysfs_path= "/sys/kernel/pddf/devices/sysstatus/attr_ops"
                if not sysfs_path in sysfs_obj[KEY]:
                        sysfs_obj[KEY].append(sysfs_path)


def show_xcvr_i2c_device(tree, dev, ops):
    KEY ='xcvr'
    if dev['i2c']['topo_info']['dev_type'] in tree['PLATFORM']['drivers']['PORT_MODULE']:
        if not KEY in sysfs_obj:
                sysfs_obj[KEY] = []
                sysfs_device(tree, dev['i2c']['topo_info'], "pddf/devices/xcvr/i2c", sysfs_obj, KEY)

                for attr in dev['i2c']['attr_list']:
                        sysfs_device(tree, attr, "pddf/devices/xcvr/i2c", sysfs_obj, KEY)
                        sysfs_path = "/sys/kernel/pddf/devices/xcvr/i2c/dev_ops"
                        if not sysfs_path in sysfs_obj[KEY]:
                                sysfs_obj[KEY].append(sysfs_path)
                list=['/sys/kernel/pddf/devices/xcvr/i2c/i2c_type',
                      '/sys/kernel/pddf/devices/xcvr/i2c/i2c_name',
                      '/sys/kernel/pddf/devices/xcvr/i2c/error',
                      '/sys/kernel/pddf/devices/xcvr/i2c/attr_ops']
                add_list_sysfs_obj(sysfs_obj, KEY, list)


def show_xcvr_device(tree, dev, ops):
        show_xcvr_i2c_device(tree, dev, ops )

def show_cpld_device(tree, dev, ops):
    KEY ='cpld'
    if dev['i2c']['topo_info']['dev_type'] in tree['PLATFORM']['drivers']['CPLD']:
        if not KEY in sysfs_obj:
                sysfs_obj[KEY] = []
                sysfs_device(tree, dev['i2c']['topo_info'], "pddf/devices/cpld", sysfs_obj, KEY)
                sysfs_path= "/sys/kernel/pddf/devices/cpld/dev_ops"
                if not sysfs_path in sysfs_obj[KEY]:
                        sysfs_obj[KEY].append(sysfs_path)
                list=['/sys/kernel/pddf/devices/cpld/i2c_type',
                      '/sys/kernel/pddf/devices/cpld/i2c_name',
                      '/sys/kernel/pddf/devices/cpld/error']
                add_list_sysfs_obj(sysfs_obj, KEY, list)

def show_led_platform_device(tree, key, ops):
        if ops['attr']=='all' or ops['attr']=='PLATFORM':
                KEY='platform'
                if not KEY in sysfs_obj:
                        sysfs_obj[KEY] = []
                        path='pddf/devices/platform'
                        sysfs_attr('num_psus', tree['PLATFORM']['num_psus'], path, sysfs_obj, KEY)
                        sysfs_attr('num_fans', tree['PLATFORM']['num_fans'], path, sysfs_obj, KEY)

def show_led_device(tree, key, ops):
        if check_led_cmds(tree, key, ops):
                KEY='led'
                if not KEY in sysfs_obj:
                        sysfs_obj[KEY] = []
                        path="pddf/devices/led"
                        for attr in tree[key]['i2c']['attr_list']:
                                sysfs_attr('device_name', tree[key]['dev_info']['device_name'], path, sysfs_obj, KEY)
                                sysfs_attr('swpld_addr', tree[key]['dev_info']['device_name'], path, sysfs_obj, KEY)
                                sysfs_attr('swpld_addr_offset', tree[key]['dev_info']['device_name'], path, sysfs_obj, KEY)
                                sysfs_device(tree, tree[key]['dev_attr'], path, sysfs_obj, KEY)
                                for attr_key in attr.keys():
                                        attr_path="pddf/devices/led/" + attr['attr_name']
                                        if (attr_key != 'attr_name' and attr_key != 'swpld_addr' and attr_key != 'swpld_addr_offset'):
                                                sysfs_attr(attr_key, attr[attr_key], attr_path, sysfs_obj, KEY)
                        sysfs_path="/sys/kernel/pddf/devices/led/dev_ops"
                        if not sysfs_path in sysfs_obj[KEY]:
                                sysfs_obj[KEY].append(sysfs_path)
                	list=['/sys/kernel/pddf/devices/led/cur_state/color',
                		'/sys/kernel/pddf/devices/led/cur_state/color_state']
                	add_list_sysfs_obj(sysfs_obj, KEY, list)


#################################################################################################################################
#  SPYTEST 
#################################################################################################################################
def validate_sysfs_creation(obj, validate_type):
        dir = '/sys/kernel/pddf/devices/'+validate_type
        if (os.path.exists(dir) or validate_type=='client'):
            for sysfs in obj[validate_type]:
                if(not os.path.exists(sysfs)):
                    print "[SYSFS FILE] " + sysfs + ": does not exist"
        else:
            print "[SYSFS DIR] " + dir + ": does not exist"

def validate_dsysfs_creation(obj, validate_type):
    # There is a possibility that some components dont have any device-data attr
    if not obj[validate_type]:
        print "[SYSFS ATTR] for " + validate_type  + ": does not exist"
    else:
        for sysfs in obj[validate_type]:
            if(not os.path.exists(sysfs)):
                print "[SYSFS FILE] " + sysfs + ": does not exist"


#################################################################################################################################
#   PARSE DEFS
#################################################################################################################################
def psu_parse(tree, dev, ops):
        str=""
        ret=""
	for ifce in dev['i2c']['interface']:
	    ret=globals()[ops['cmd']+"_psu_device"](tree, tree[ifce['dev']], ops )
            if not ret is None:
                str+=ret
        return str

def fan_parse(tree, dev, ops):
        str=""
	str=globals()[ops['cmd']+"_fan_device"](tree, dev, ops )
        #print "psu_parse -- %s"%str
        return str

def temp_sensor_parse(tree, dev, ops):
        str=""
	str=globals()[ops['cmd']+"_temp_sensor_device"](tree, dev, ops )
        #print "temp_sensor_parse -- %s"%str
        return str

def cpld_parse(tree, dev, ops):
    ret = ""
    ret = globals()[ops['cmd']+"_cpld_device"](tree, dev, ops)
    return ret




def sysstatus_parse(tree,dev,ops):
    ret = ""
    ret = globals()[ops['cmd']+"_sysstatus_device"](tree, dev, ops)
    return ret 


def mux_parse(tree, dev, ops):
        str = ""
	ret = globals()[ops['cmd']+"_mux_device"](tree, dev, ops)
        if not ret is None:
            str += ret

	for ch in dev['i2c']['channel']:
            ret = dev_parse(tree, tree[ch['dev']], ops)	
            if not ret is None:
                str += ret
        return str

def mux_parse_reverse(tree, dev, ops):
        str = ""
	for ch in dev['i2c']['channel']:
            ret = dev_parse(tree, tree[ch['dev']], ops)	
            if not ret is None:
                str += ret

	ret = globals()[ops['cmd']+"_mux_device"](tree, dev, ops)
        if not ret is None:
            str += ret

        return str


def eeprom_parse(tree, dev, ops):
    str = ""
    str = globals()[ops['cmd']+"_eeprom_device"](tree, dev, ops)
    return str

def optic_parse(tree, dev, ops):
        str=""
        ret=""
        for ifce in dev['i2c']['interface']:
            ret=globals()[ops['cmd']+"_xcvr_device"](tree, tree[ifce['dev']], ops )
            if not ret is None:
                str+=ret
        return str

def cpu_parse(tree, bus, ops):
    str = ""
    for dev in bus['i2c']['CONTROLLERS']:
        dev1 = tree[dev['dev']]
        for d in dev1['i2c']['DEVICES']:
            ret=dev_parse(tree, tree[d['dev']], ops)
            if not ret is None:
                str += ret
    return str


def dev_parse(tree, dev, ops):
	attr=dev['dev_info']
	if attr['device_type'] == 'CPU':
		return cpu_parse(tree, dev, ops)
    
        if attr['device_type'] == 'EEPROM':
            return eeprom_parse(tree, dev, ops)

        if attr['device_type'] == 'MUX':
            if ops['cmd']=='delete':
		return mux_parse_reverse(tree, dev, ops)
            else:
                return mux_parse(tree, dev, ops)

	if attr['device_type'] == 'PSU':
		return psu_parse(tree, dev, ops)

	if attr['device_type'] == 'FAN':
		return fan_parse(tree, dev, ops)

	if attr['device_type'] == 'TEMP_SENSOR':
		return temp_sensor_parse(tree, dev, ops)

        if attr['device_type'] == 'SFP' or attr['device_type'] == 'QSFP':
                return optic_parse(tree, dev, ops)

	if attr['device_type'] == 'CPLD':
		return cpld_parse(tree, dev, ops)

        if attr['device_type'] == 'SYSSTAT':
                return sysstatus_parse(tree,dev,ops)

def create_attr(key, value, path):
        cmd = "echo '%s' > /sys/kernel/%s/%s"%(value,  path, key)
        #print cmd
        os.system(cmd)

def create_led_platform_device(tree, key, ops):
        if ops['attr']=='all' or ops['attr']=='PLATFORM':
		path='pddf/devices/led'
		create_attr('num_psus', tree['PLATFORM']['num_psus'], path)
		create_attr('num_fans', tree['PLATFORM']['num_fans'], path)

def create_led_device(tree, key, ops):
        if ops['attr']=='all' or ops['attr']==tree[key]['dev_info']['device_name']:
		path="pddf/devices/led"
		ops_state=""
                for attr in tree[key]['i2c']['attr_list']:
                        create_attr('device_name', tree[key]['dev_info']['device_name'], path)
                        create_device(tree, tree[key]['dev_attr'], path, ops)
                        for attr_key in attr.keys():
				if (attr_key == 'swpld_addr_offset' or attr_key == 'swpld_addr'):
                                        create_attr(attr_key, attr[attr_key], path)
                                elif (attr_key != 'attr_name'):
					state_path=path+'/'+attr['attr_name']
                                        create_attr(attr_key, attr[attr_key],state_path)
                        cmd="echo '" + ops['cmd'] + '_' + attr['attr_name']+"' > /sys/kernel/pddf/devices/led/dev_ops\n"
                        #print cmd
                        os.system(cmd)

def get_led_device(device_name):
    create_attr('device_name', data[device_name]['dev_info']['device_name'], "pddf/devices/led")
    create_attr('index', data[device_name]['dev_attr']['index'], "pddf/devices/led")
    cmd="echo 'verify'  > /sys/kernel/pddf/devices/led/dev_ops\n"
    os.system(cmd)


def led_parse(tree, ops):
        #print "led_parse cmd: " + ops['cmd']
        globals()[ops['cmd']+"_led_platform_device"](tree, "PLATFORM", ops)
        for key in tree.keys():
                if key != 'PLATFORM':
                        attr=tree[key]['dev_info']
                        if attr['device_type'] == 'LED':
                                globals()[ops['cmd']+"_led_device"](tree, key, ops)


def get_device_list(list, type):
        for key in data.keys():
                if key != 'PLATFORM':
                        attr=data[key]['dev_info']
                        if attr['device_type'] == type:
                                list.append(data[key])


def create_pddf_devices():
    dev_parse(data, data['SYSTEM'], { "cmd": "create", "target":"all", "attr":"all" } )
    dev_parse(data, data['SYSSTATUS'], { "cmd": "create", "target":"all", "attr":"all" } )
    led_parse(data, { "cmd": "create", "target":"all", "attr":"all" })
    
def delete_pddf_devices():
    dev_parse(data, data['SYSTEM'], { "cmd": "delete", "target":"all", "attr":"all" } )
    dev_parse(data, data['SYSSTATUS'], { "cmd": "delete", "target":"all", "attr":"all" } )

def show_pddf_devices():
    dev_parse(data, data['SYSTEM'], { "cmd": "show", "target":"all", "attr":"all" } )
    dev_parse(data, data['SYSSTATUS'], { "cmd": "show", "target":"all", "attr":"all" } )
    led_parse(data, { "cmd": "show", "target":"all", "attr":"all" })
    show_client_device()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--create", action='store_true', help="create the I2C topology")
    parser.add_argument("--sysfs", action='store', nargs="+",  help="show access-attributes sysfs for the I2C topology")
    parser.add_argument("--dsysfs", action='store', nargs="+",  help="show data-attributes sysfs for the I2C topology")
    parser.add_argument("--delete", action='store_true', help="Remove all the created I2C clients from topology")
    args = parser.parse_args()
    #print args
    str = ""
    if args.create:
        create_pddf_devices()

    if args.sysfs:
        if args.sysfs[0] == 'all':
		show_pddf_devices()
        if args.sysfs[0] == 'print':
		show_pddf_devices()
		dump_sysfs_obj(sysfs_obj, args.sysfs[1])
        if args.sysfs[0] == 'validate':
		show_pddf_devices()
		validate_sysfs_creation(sysfs_obj, args.sysfs[1])

    if args.dsysfs:
	if args.dsysfs[0] == 'validate':
            dev_parse(data, data['SYSTEM'], { "cmd": "show_attr", "target":"all", "attr":"all" } )
            dev_parse(data, data['SYSSTATUS'], { "cmd": "show_attr", "target":"all", "attr":"all" } )
            validate_dsysfs_creation(data_sysfs_obj, args.dsysfs[1])

        elif args.dsysfs[0] == 'print':
            dev_parse(data, data['SYSTEM'], { "cmd": "show_attr", "target":"all", "attr":"all" } )
            dev_parse(data, data['SYSSTATUS'], { "cmd": "show_attr", "target":"all", "attr":"all" } )
            dump_sysfs_obj(data_sysfs_obj, args.dsysfs[1])

        elif args.dsysfs[0] == 'all':
            ret = dev_parse(data, data['SYSTEM'], { "cmd": "show_attr", "target":"all", "attr":"all" } )
            ret += dev_parse(data, data['SYSSTATUS'], { "cmd": "show_attr", "target":"all", "attr":"all" } )
            dump_sysfs_obj(data_sysfs_obj, 'all')
            #if not ret is None:
                #ret = ret.rstrip('\n')
                #print ret
        else:
            ret = dev_parse(data, data[args.dsysfs[0]], { "cmd": "show_attr", "target":args.dsysfs[0], "attr":args.dsysfs[1] })
            #if not ret is None:
                #ret = ret.rstrip('\n')
                #print ret

    if args.delete:
        delete_pddf_devices()




if __name__ == "__main__" :
        main()



