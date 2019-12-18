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
    "hundredGigE1/17/1":"ce0",
    "hundredGigE1/17/2":"ce1",
    "hundredGigE1/17/3":"ce2",
    "hundredGigE1/17/4":"ce3",
    "hundredGigE1/18/1":"ce4",
    "hundredGigE1/18/2":"ce5",
    "hundredGigE1/18/3":"ce6",
    "hundredGigE1/18/4":"ce7",
    "hundredGigE1/19/1":"ce8",
    "hundredGigE1/19/2":"ce9",
    "hundredGigE1/19/3":"ce10",
    "hundredGigE1/19/4":"ce11",
    "hundredGigE1/20/1":"ce12",
    "hundredGigE1/20/2":"ce13",
    "hundredGigE1/20/3":"ce14",
    "hundredGigE1/20/4":"ce15",
    "hundredGigE1/21/1":"ce16",
    "hundredGigE1/21/2":"ce17",
    "hundredGigE1/21/3":"ce18",
    "hundredGigE1/21/4":"ce19",
    "hundredGigE1/22/1":"ce20",
    "hundredGigE1/22/2":"ce21",
    "hundredGigE1/22/3":"ce22",
    "hundredGigE1/22/4":"ce23",
    "hundredGigE1/23/1":"ce24",
    "hundredGigE1/23/2":"ce25",
    "hundredGigE1/23/3":"ce26",
    "hundredGigE1/23/4":"ce27",
    "hundredGigE1/24/1":"ce28",
    "hundredGigE1/24/2":"ce29",
    "hundredGigE1/24/3":"ce30",
    "hundredGigE1/24/4":"ce31",
    "hundredGigE1/25/1":"ce32",
    "hundredGigE1/25/2":"ce33",
    "hundredGigE1/25/3":"ce34",
    "hundredGigE1/25/4":"ce35",
    "hundredGigE1/26/1":"ce36",
    "hundredGigE1/26/2":"ce37",
    "hundredGigE1/26/3":"ce38",
    "hundredGigE1/26/4":"ce39",
    "hundredGigE1/27/1":"ce40",
    "hundredGigE1/27/2":"ce41",
    "hundredGigE1/27/3":"ce42",
    "hundredGigE1/27/4":"ce43",
    "hundredGigE1/28/1":"ce44",
    "hundredGigE1/28/2":"ce45",
    "hundredGigE1/28/3":"ce46",
    "hundredGigE1/28/4":"ce47",
    "hundredGigE1/29/1":"ce48",
    "hundredGigE1/29/2":"ce49",
    "hundredGigE1/29/3":"ce50",
    "hundredGigE1/29/4":"ce51",
    "hundredGigE1/30/1":"ce52",
    "hundredGigE1/30/2":"ce53",
    "hundredGigE1/30/3":"ce54",
    "hundredGigE1/30/4":"ce55",
    "hundredGigE1/31/1":"ce56",
    "hundredGigE1/31/2":"ce57",
    "hundredGigE1/31/3":"ce58",
    "hundredGigE1/31/4":"ce59",
    "hundredGigE1/32/1":"ce60",
    "hundredGigE1/32/2":"ce61",
    "hundredGigE1/32/3":"ce62",
    "hundredGigE1/32/4":"ce63",
    "fourhundredGigE1/1":"cd0",
    "fourhundredGigE1/2":"cd1",
    "fourhundredGigE1/3":"cd2",
    "fourhundredGigE1/4":"cd3",
    "fourhundredGigE1/5":"cd4",
    "fourhundredGigE1/6":"cd5",
    "fourhundredGigE1/7":"cd6",
    "fourhundredGigE1/8":"cd7",
    "fourhundredGigE1/9":"cd8",
    "fourhundredGigE1/10":"cd9",
    "fourhundredGigE1/11":"cd10",
    "fourhundredGigE1/12":"cd11",
    "fourhundredGigE1/13":"cd12",
    "fourhundredGigE1/14":"cd13",
    "fourhundredGigE1/15":"cd14",
    "fourhundredGigE1/16":"cd15"
}

alias_to_if_map = {
    'fourhundredGigE1/1': '0',
    'fourhundredGigE1/2': '8',
    'fourhundredGigE1/3': '16',
    'fourhundredGigE1/4': '24',
    'fourhundredGigE1/5': '32',
    'fourhundredGigE1/6': '40',
    'fourhundredGigE1/7': '48',
    'fourhundredGigE1/8': '56',
    'fourhundredGigE1/9': '64',
    'fourhundredGigE1/10': '72',
    'fourhundredGigE1/11': '80',
    'fourhundredGigE1/12': '88',
    'fourhundredGigE1/13': '96',
    'fourhundredGigE1/14': '104',
    'fourhundredGigE1/15': '112',
    'fourhundredGigE1/16': '120',
    'hundredGigE1/17/1': '128',
    'hundredGigE1/17/2': '130',
    'hundredGigE1/17/3': '132',
    'hundredGigE1/17/4': '134',
    'hundredGigE1/18/1': '136',
    'hundredGigE1/18/2': '138',
    'hundredGigE1/18/3': '140',
    'hundredGigE1/18/4': '142',
    'hundredGigE1/19/1': '144',
    'hundredGigE1/19/2': '146',
    'hundredGigE1/19/3': '148',
    'hundredGigE1/19/4': '150',
    'hundredGigE1/20/1': '152',
    'hundredGigE1/20/2': '154',
    'hundredGigE1/20/3': '156',
    'hundredGigE1/20/4': '158',
    'hundredGigE1/21/1': '160',
    'hundredGigE1/21/2': '162',
    'hundredGigE1/21/3': '164',
    'hundredGigE1/21/4': '166',
    'hundredGigE1/22/1': '168',
    'hundredGigE1/22/2': '170',
    'hundredGigE1/22/3': '172',
    'hundredGigE1/22/4': '174',
    'hundredGigE1/23/1': '176',
    'hundredGigE1/23/2': '178',
    'hundredGigE1/23/3': '180',
    'hundredGigE1/23/4': '182',
    'hundredGigE1/24/1': '184',
    'hundredGigE1/24/2': '186',
    'hundredGigE1/24/3': '188',
    'hundredGigE1/24/4': '190',
    'hundredGigE1/25/1': '192',
    'hundredGigE1/25/2': '194',
    'hundredGigE1/25/3': '196',
    'hundredGigE1/25/4': '198',
    'hundredGigE1/26/1': '200',
    'hundredGigE1/26/2': '202',
    'hundredGigE1/26/3': '204',
    'hundredGigE1/26/4': '206',
    'hundredGigE1/27/1': '208',
    'hundredGigE1/27/2': '210',
    'hundredGigE1/27/3': '212',
    'hundredGigE1/27/4': '214',
    'hundredGigE1/28/1': '216',
    'hundredGigE1/28/2': '218',
    'hundredGigE1/28/3': '220',
    'hundredGigE1/28/4': '222',
    'hundredGigE1/29/1': '224',
    'hundredGigE1/29/2': '226',
    'hundredGigE1/29/3': '228',
    'hundredGigE1/29/4': '230',
    'hundredGigE1/30/1': '232',
    'hundredGigE1/30/2': '234',
    'hundredGigE1/30/3': '236',
    'hundredGigE1/30/4': '238',
    'hundredGigE1/31/1': '240',
    'hundredGigE1/31/2': '242',
    'hundredGigE1/31/3': '244',
    'hundredGigE1/31/4': '246',
    'hundredGigE1/32/1': '248',
    'hundredGigE1/32/2': '250',
    'hundredGigE1/32/3': '252',
    'hundredGigE1/32/4': '254',
}

if_to_alias_map = {

    '0': 'fourhundredGigE1/1',
    '8': 'fourhundredGigE1/2',
    '16': 'fourhundredGigE1/3',
    '24': 'fourhundredGigE1/4',
    '32': 'fourhundredGigE1/5',
    '40': 'fourhundredGigE1/6',
    '48': 'fourhundredGigE1/7',
    '56': 'fourhundredGigE1/8',
    '64': 'fourhundredGigE1/9',
    '72': 'fourhundredGigE1/10',
    '80': 'fourhundredGigE1/11',
    '88': 'fourhundredGigE1/12',
    '96': 'fourhundredGigE1/13',
    '104': 'fourhundredGigE1/14',
    '112': 'fourhundredGigE1/15',
    '120': 'fourhundredGigE1/16',
    '128': 'hundredGigE1/17/1',
    '130': 'hundredGigE1/17/2',
    '132': 'hundredGigE1/17/3',
    '134': 'hundredGigE1/17/4',
    '136': 'hundredGigE1/18/1',
    '138': 'hundredGigE1/18/2',
    '140': 'hundredGigE1/18/3',
    '142': 'hundredGigE1/18/4',
    '144': 'hundredGigE1/19/1',
    '146': 'hundredGigE1/19/2',
    '148': 'hundredGigE1/19/3',
    '150': 'hundredGigE1/19/4',
    '152': 'hundredGigE1/20/1',
    '154': 'hundredGigE1/20/2',
    '156': 'hundredGigE1/20/3',
    '158': 'hundredGigE1/20/4',
    '160': 'hundredGigE1/21/1',
    '162': 'hundredGigE1/21/2',
    '164': 'hundredGigE1/21/3',
    '166': 'hundredGigE1/21/4',
    '168': 'hundredGigE1/22/1',
    '170': 'hundredGigE1/22/2',
    '172': 'hundredGigE1/22/3',
    '174': 'hundredGigE1/22/4',
    '176': 'hundredGigE1/23/1',
    '178': 'hundredGigE1/23/2',
    '180': 'hundredGigE1/23/3',
    '182': 'hundredGigE1/23/4',
    '184': 'hundredGigE1/24/1',
    '186': 'hundredGigE1/24/2',
    '188': 'hundredGigE1/24/3',
    '190': 'hundredGigE1/24/4',
    '192': 'hundredGigE1/25/1',
    '194': 'hundredGigE1/25/2',
    '196': 'hundredGigE1/25/3',
    '198': 'hundredGigE1/25/4',
    '200': 'hundredGigE1/26/1',
    '202': 'hundredGigE1/26/2',
    '204': 'hundredGigE1/26/3',
    '206': 'hundredGigE1/26/4',
    '208': 'hundredGigE1/27/1',
    '210': 'hundredGigE1/27/2',
    '212': 'hundredGigE1/27/3',
    '214': 'hundredGigE1/27/4',
    '216': 'hundredGigE1/28/1',
    '218': 'hundredGigE1/28/2',
    '220': 'hundredGigE1/28/3',
    '222': 'hundredGigE1/28/4',
    '224': 'hundredGigE1/29/1',
    '226': 'hundredGigE1/29/2',
    '228': 'hundredGigE1/29/3',
    '230': 'hundredGigE1/29/4',
    '232': 'hundredGigE1/30/1',
    '234': 'hundredGigE1/30/2',
    '236': 'hundredGigE1/30/3',
    '238': 'hundredGigE1/30/4',
    '240': 'hundredGigE1/31/1',
    '242': 'hundredGigE1/31/2',
    '244': 'hundredGigE1/31/3',
    '246': 'hundredGigE1/31/4',
    '248': 'hundredGigE1/32/1',
    '250': 'hundredGigE1/32/2',
    '252': 'hundredGigE1/32/3',
    '254': 'hundredGigE1/32/4',
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

    if int(port) < 17:
        return ['fourhundredGigE1/'+str(port)]
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
        presence = get_presence(port)
        if presence ==  False:
            continue
        if (port < 17): 
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
            if (port_num < 17): continue

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

def main():
    dbg_print ("mediautil: __Init__ ")

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
