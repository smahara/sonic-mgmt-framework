# sfputil.py
#
# Platform-specific SFP transceiver interface for SONiC
#

from __future__ import print_function

try:
    import struct
    import sys
    import getopt
    import time
    import select
    from os import *
    from mmap import *
    import threading

except ImportError as e:
    raise ImportError("%s - required module not found" % str(e))

alias_to_bcm_map = {
}

alias_to_if_map = {
}

if_to_alias_map = {
}

def run_cmd(cmd, supressError=False):
    dbg_print("Will run %s" %cmd)
    import subprocess as sp
    if supressError:
        process = sp.Popen(cmd, shell = True, stdout = sp.PIPE, stderr = sp.PIPE)
    else:
        process = sp.Popen(cmd, shell = True, stdout = sp.PIPE, stderr = sp.STDOUT)
    out = process.communicate()[0]
    dbg_print("run cmd %s"%out)
    time.sleep(0.5)
    return process.returncode, out

def construct_interfaces_from_physical_port_num(port):

    #if int(port) & 0x01 == 0:
    #    return ['fourhundredGigE1/'+str(port)]
    return ["hundredGigE1/%s/%u" %(str(port), c) for c in range(1, 5, 1)]

def get_port_ids(port):
    mp = dict()
    for i in construct_interfaces_from_physical_port_num(port):
        sub = dict()
        sub['if_name'] = 'Ethernet'+alias_to_if_map[i]
        sub['bcm_port'] = alias_to_bcm_map[i]
        mp[i] = sub
        dbg_print("Mp %s"%str(mp))
    return mp

def get_if_state_by_ifname(ifname):
    cmd = 'show interfaces status '+ifname
    #if_str = 'Ethernet' + interface
    dbg_print ("ifname %s %s"%(str(ifname), cmd))
    err, res = run_cmd(cmd)
    if err:
       dbg_print ("Error running %s %s"%(str(ifname), cmd))
       return False, False
    #print(res)
    output = res.splitlines()
    if len(output) < 3 : return err, False
    dbg_print("%s %s"%( str(output), str(len(output))))
    dbg_print("**************if_info*******************************************%s"%str(output[2]))
    arr = output[2].split()
    return (arr[6] == 'up', arr[7] == 'up' )

def set_if_state_by_bcmsh(alias, state):
    bcm_port = alias_to_bcm_map[alias]
    st = int(state)
    cmd = "bcmcmd -t 60  \"port %s en=%u\"" %(bcm_port, st)
    err, res = run_cmd(cmd)

def set_if_speed_100g_by_bcmsh(alias):
    bcm_port = alias_to_bcm_map[alias]
    cmd = "bcmcmd -t 60  \"port %s sp=100000\"" %bcm_port

    err, res = run_cmd(cmd)

DBG = False

_port_to_i2c_mapping = {
        1:  10,
        2:  11,
        3:  12,
        4:  13,
        5:  14,
        6:  15,
        7:  16,
        8:  17,
        9:  18,
        10: 19,
        11: 20,
        12: 21,
        13: 22,
        14: 23,
        15: 24,
        16: 25,
        17: 26,
        18: 27,
        19: 28,
        20: 29,
        21: 30,
        22: 31,
        23: 32,
        24: 33,
        25: 34,
        26: 35,
        27: 36,
        28: 37,
        29: 38,
        30: 39,
        31: 40,
        32: 41,
        33: 1,
        34: 2,
        }

# Default to top (odd) ports

def is_port_allowed(port):
    port = int(port)
    if script_mode == 'LEFT_PORTS':
        return (port >= 1) and (port <= 16)
    if script_mode == 'RIGHT_PORTS':
        return (port >= 17) and (port <= 32)
    elif script_mode == 'ODD_PORTS':
        return port % 2 == 1
    return False

def dbg_print(st):
    if DBG:
        print(st,file=sys.stderr)

def unload_driver(port):
    i2c_val = _port_to_i2c_mapping[port]
    cmd = 'echo 0x50 > /sys/bus/i2c/devices/i2c-%s/delete_device' % i2c_val
    run_cmd(cmd)

def load_driver(port):
    i2c_val = _port_to_i2c_mapping[port]
    cmd = 'echo sff8436 0x50 > /sys/bus/i2c/devices/i2c-%s/new_device' % i2c_val
    run_cmd(cmd)
    
def select_page(port):
    i2c_val = _port_to_i2c_mapping[port]
    # page select to page 16 0x10
    cmd = 'i2cset -y %s 0x50 0x7F 0x10' % i2c_val
    run_cmd(cmd)

def deselect_page(port):
    i2c_val = _port_to_i2c_mapping[port]
    # page deselect to page 16 0x10
    cmd = 'i2cset -y %s 0x50 0x7F 0x00' % i2c_val
    run_cmd(cmd)    
def datapath_set(port, enable):
    i2c_val = _port_to_i2c_mapping[port]
    byte = '0x00'
    if enable == True:
        byte = '0xFF'
    # page must have been selected to 0x10
    cmd = 'i2cset -y %s 0x50 0x80 %s' % (i2c_val, byte)
    run_cmd(cmd)
    
def tx_control_set(port, enable):
    i2c_val = _port_to_i2c_mapping[port]
    byte = '0xFF'
    if enable == True:
        byte = '0x00'
    # page must have been selected to 0x10
    cmd = 'i2cset -y %s 0x50 0x82 %s' % (i2c_val, byte)
    run_cmd(cmd)

def app_set(port):
    i2c_val = _port_to_i2c_mapping[port]
    # page must have been selected to 0x10
    cmd = 'i2cset -y %s 0x50 0xB2 0xFF' % i2c_val
    run_cmd(cmd)

def is_smf(port):
    dbg_print("is_smf")
    unload_driver(port)
    i2c_val = _port_to_i2c_mapping[port]
    cmd = 'i2cget -y %s 0x50 85' % i2c_val
    err, res = run_cmd(cmd)
    dbg_print("is_smf %s"% str(res))
    load_driver(port)
    #retrun true of type is SMF 'byte 85' in CMIS spec
    if (res[3] == "2"):
        return True
    else:
        return False


# Returns true if the module is has an active fiber link
# Return true for now 
def fiber_link_state_get(port):
    return True

def module_init(port):
    dbg_print("Unloading driver for port %s" %port)
    unload_driver(port)
    dbg_print("Selecting page 0x10 for port %s" %port)
    select_page(port)
    dbg_print("App set for %s" % port)
    app_set(port)
    dbg_print("Turning off tx control/laser for port %s" %port);
    tx_control_set(port, False)
    dbg_print("Turning off datapath for port %s" %port);
    datapath_set(port, False)
    dbg_print("Waiting for module to power down for port %s" %port);
    time.sleep(1) # sri changed from 2 sec

    dbg_print("Turning on datapath and waiting 10 seconds for port %s" %port);
    datapath_set(port, True)
    time.sleep(7) # sri changed from 10 sec
    dbg_print("Turning on tx control/laser for port %s" %port);
    tx_control_set(port, True)
    dbg_print("Reverting and selecting page 0x00 for port %s" %port)
    deselect_page(port)
    dbg_print("Loading driver for port %s" %port)
    load_driver(port)


port_mon_lock = threading.Lock()
ports_to_monitor = []

def media_presence_change_handler(port, state):

    if is_port_allowed(port) ==  False:
        dbg_print("Rejecting " + str(port))
        return True
    dbg_print (" Enter media_presence_change_handler portnum %d state %s"%(port,state))

    # Media removed. Remove entry from poller list
    if state == False:
        if port in ports_to_monitor:
            remove_port_to_monitor(port)
        return True

    # List of lanes on module that will need to be cfg
    lanes_to_cfg = []
    for alias,val in get_port_ids(port).items():
        # Only act on ports broken out into 100G
        if 'hundredGigE1'not in alias:
            return True

        oper, admin = get_if_state_by_ifname(val['if_name'])
        dbg_print ("alias %s  operi %s, admin %s"%(alias, str(oper),str(admin)))

        # Case 0: New media presence, but admin down. No action
        if admin == False:
            continue

        # Case 1: New media presence, but admin up, oper up
        if admin == True and oper ==  True:
            continue

        # Case 2: New media presence, but admin up, oper down
        # Let link stabilize
        time.sleep(2)
        oper, admin = get_if_state_by_ifname(val['if_name'])
        # It came up automatically
        if oper ==  True:
            break
        # Admin has been brought down while waiting 
        if admin == False:
            break
        dbg_print("Let link stabilize %s"%alias)
        lanes_to_cfg.append(alias)

    if len(lanes_to_cfg) > 0:
        #check for SMF/optical interface
        if(is_smf(port)):
        # Run module init
            module_init(port)

    # Add port to list for poller to stabilize monitor and stabilize
    if port not in ports_to_monitor:
        add_port_to_monitor(port)

    dbg_print (" Exit media_presence_change_handler portnum %d"%port)




def add_port_to_monitor(port):
    if port not in ports_to_monitor:
        port_mon_lock.acquire()
        ports_to_monitor.append(port)
        port_mon_lock.release()

def remove_port_to_monitor(port):
    if port in ports_to_monitor:
        port_mon_lock.acquire()
        ports_to_monitor.remove(port)
        port_mon_lock.release()

def link_state_speed_set():
    for port in ports_to_monitor:
        if is_port_allowed(port) == False:
            continue
        presence = get_presence(port)
        if presence ==  False:
            continue
        
        if port in _is_smf and _is_smf[port] is False:
            continue

        for alias,val in get_port_ids(port).items():
        # If the media has a loss of signal from fiber end
        # Or if something else on the media is faulty, link nothing to be done here
            if fiber_link_state_get(port) == False:
                continue

            oper, admin = get_if_state_by_ifname(val['if_name'])
            if oper == False and admin == True:
                # Attempt to recover link 
                set_if_state_by_bcmsh(alias, True)
                time.sleep(1)
                set_if_speed_100g_by_bcmsh(alias)

def link_state_monitor(period = 3):
    while True :
        port_mon_lock.acquire()
        link_state_speed_set()
        port_mon_lock.release()
        time.sleep(period)


def qsfp_ports():
    return range(PORT_START, PORTS_IN_BLOCK + 1)


def is_odd_port(port_num):
    return bool(port_num - ((port_num>>1)<<1))

def pci_mem_read(mm, offset):
    mm.seek(offset)
    read_data_stream = mm.read(4)
    reg_val = struct.unpack('I', read_data_stream)
    mem_val = str(reg_val)[1:-2]
    # print "reg_val read:%x"%reg_val
    return mem_val

def pci_mem_write(mm, offset, data):
    mm.seek(offset)
    # print "data to write:%x"%data
    mm.write(struct.pack('I', data))

def pci_set_value(resource, val, offset):
    fd = open(resource, O_RDWR)
    mm = mmap(fd, 0)
    val = pci_mem_write(mm, offset, val)
    mm.close()
    close(fd)
    return val

def pci_get_value(resource, offset):
    fd = open(resource, O_RDWR)
    mm = mmap(fd, 0)
    val = pci_mem_read(mm, offset)
    mm.close()
    close(fd)
    return val

def init_global_port_presence():
    for port_num in range(PORT_START, (PORT_END + 1)):
        presence = get_presence(port_num)
        if(presence):
            _global_port_pres_dict[port_num] = '1'
        else:
            _global_port_pres_dict[port_num] = '0'


def get_presence(port_num):
    # Check for invalid port_num
    if port_num < PORT_START or port_num > PORT_END:
        return False

    # No need to check presence for ports not allowed
    if is_port_allowed(port_num) == False:
        return False

    # Port offset starts with 0x4004
    port_offset = 16388 + ((port_num-1) * 16)

    status = pci_get_value(BASE_RES_PATH, port_offset)
    reg_value = int(status)

    # Absence of status throws error
    if (reg_value == ""):
        return False

    # Mask off 4th bit for presence
    mask = (1 << 4)

    # Mask off 1st bit for presence 33,34
    if (port_num > 32):
        mask =  (1 << 0)

    # ModPrsL is active low
    if reg_value & mask == 0:
        return True

    return False


def media_config(port_dict):
        for port_num in range(PORT_START, (PORT_END - 1)):
            presence = get_presence(port_num)
            #dbg_print("Media %d present %s : %s"%(port_num, presence, _global_port_pres_dict[port_num]))
            #if ((port_num % 2) == 0): continue
            if is_port_allowed(port_num) == False:
                continue
            if(presence and _global_port_pres_dict[port_num] == '0'):
                _global_port_pres_dict[port_num] = '1'
                port_dict[port_num] = '1'
                dbg_print("Media %d present , calling presence_change_handler"%port_num)
                _is_smf[port_num] = is_smf(port_num) 
                media_presence_change_handler(port_num, True)

            elif(not presence and
                 _global_port_pres_dict[port_num] == '1'):
                _global_port_pres_dict[port_num] = '0'
                port_dict[port_num] = '0'
                media_presence_change_handler(port_num, False)
                _is_smf.pop(port_num)


def get_transceiver_change_event():
    port_dict = {}
    media_config(port_dict)
    time.sleep(1)

eeprom_path = "/sys/class/i2c-adapter/i2c-{0}/{0}-0050/eeprom"

PORT_START = 1
PORT_END = 34 
PORTS_IN_BLOCK = 34 

BASE_RES_PATH = "/sys/bus/pci/devices/0000:09:00.0/resource0"
_is_smf = {}
_port_to_i2c_mapping = {
            1:  10,
            2:  11,
            3:  12,
            4:  13,
            5:  14,
            6:  15,
            7:  16,
            8:  17,
            9:  18,
            10: 19,
            11: 20,
            12: 21,
            13: 22,
            14: 23,
            15: 24,
            16: 25,
            17: 26,
            18: 27,
            19: 28,
            20: 29,
            21: 30,
            22: 31,
            23: 32,
            24: 33,
            25: 34,
            26: 35,
            27: 36,
            28: 37,
            29: 38,
            30: 39,
            31: 40,
            32: 41,
            33: 1,
            34: 2,
            }

_port_to_eeprom_mapping = {}

_global_port_pres_dict = {}

def create_mappings():

    cmd = 'show interfaces status '
    err, res = run_cmd(cmd)
    if err:
       dbg_print ("Error running %s %s"%(str(ifname), cmd))
       return
    #print(res)
    output = res.splitlines()
    if len(output) < 3 : return err, False
    output.pop(0)
    output.pop(0)
    for line in output:
        v = line.split()
        alias = v[4]
        if_num = v[0][len('Ethernet'):]
        if_to_alias_map[if_num] = alias
        alias_to_if_map[alias] = if_num


    # Create NPU mappings 

    ce_counter = 0
    cd_counter = 0
    xe_counter = 0

    tmp_if_nums = if_to_alias_map.keys()
    tmp_if_nums.sort()

    for c in  range(0, len(tmp_if_nums), 1):
        alias = if_to_alias_map[tmp_if_nums[c]]
        if 'hundredGigE1' in alias:
            alias_to_bcm_map[alias] = 'ce' + str(ce_counter)
            ce_counter = ce_counter+1
        elif 'fourhundredGigE1' in alias:
            alias_to_bcm_map[alias] = 'cd' + str(cd_counter)
            cd_counter = cd_counter+1
        else:
            alias_to_bcm_map[alias] = 'xe' + str(xe_counter)
            xe_counter = xe_counter+1

def main():
    dbg_print ("mediautil: __Init__ ")

    global script_mode
    # Default 
    script_mode = 'ODD_PORTS'
    if len(sys.argv) > 1:
        c = sys.argv[1]
        if c == '0' or c == 'LEFT_PORTS':
            script_mode = 'LEFT_PORTS'
        elif c == '1' or c == 'RIGHT_PORTS':
            script_mode = 'RIGHT_PORTS'


    create_mappings()
    #return
    dbg_print("Operating on %s " % script_mode)

    for x in range(PORT_START, PORT_END + 1):
        _port_to_eeprom_mapping[x] = eeprom_path.format(
                _port_to_i2c_mapping[x])
        _global_port_pres_dict[x] = '0'
    port_dict = {}
    thr = threading.Thread(target=link_state_monitor)
    thr.start()
    media_config(port_dict)
    init_global_port_presence()
    #Call media init

    while True:
        get_transceiver_change_event()

if __name__ == "__main__":
    main()
