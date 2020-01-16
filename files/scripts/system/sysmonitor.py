#!/usr/bin/env python

from gi.repository import GObject
import sys
import dbus
import subprocess
from datetime import datetime
from dbus.mainloop.glib import DBusGMainLoop
import socket
import errno
import json
import time
import datetime
import netaddr
import netifaces
import os
import re
import subprocess
import sys
import signal
import threading 
import logging
import syslog
import logging.handlers
import argparse
import psutil
import pprint
from multiprocessing import Process,Value
import multiprocessing as mp
from ahab import Ahab
import collections


from swsscommon import swsscommon
import sonic_device_util
from swsssdk import ConfigDBConnector
from swsssdk import SonicV2Connector


SYSLOG_IDENTIFIER="system#monitor"
SYSTEM_STATE="DOWN"
REDIS_HOSTNAME = "127.0.0.1"
REDIS_PORT = 6379
REDIS_TIMEOUT_MS = 0
logger = None

SYSTEM_READY_TABLE = 'SYSTEM_READY'

#Logger class  for syslog
class Logger(object):
    def __init__(self, syslog_identifier):
        syslog.openlog(ident=syslog_identifier, logoption=syslog.LOG_NDELAY, facility=syslog.LOG_DAEMON)

    def __del__(self):
        syslog.closelog()

    def log_crit(self, msg, also_print_to_console=False):
        syslog.syslog(syslog.LOG_CRIT, msg)

        if also_print_to_console:
            print msg

    def log_alert(self, msg, also_print_to_console=False):
        syslog.syslog(syslog.LOG_ALERT, msg)

        if also_print_to_console:
            print msg


    def log_error(self, msg, also_print_to_console=False):
        syslog.syslog(syslog.LOG_ERR, msg)

        if also_print_to_console:
            print msg

    def log_warning(self, msg, also_print_to_console=False):
        syslog.syslog(syslog.LOG_WARNING, msg)

        if also_print_to_console:
            print msg

    def log_notice(self, msg, also_print_to_console=False):
        syslog.syslog(syslog.LOG_NOTICE, msg)

        if also_print_to_console:
            print msg

    def log_info(self, msg, also_print_to_console=False):
        syslog.syslog(syslog.LOG_INFO, msg)

        if also_print_to_console:
            print msg

    def log_debug(self, msg, also_print_to_console=False):
        syslog.syslog(syslog.LOG_DEBUG, msg)

        if also_print_to_console:
            print msg



#Initalise the syslog infrastructure
logger = Logger(SYSLOG_IDENTIFIER)


class dict2obj(object):
    """dict to dict2obj
    d: data"""

    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
                setattr(self, a, [dict2obj(x) if isinstance(
                    x, dict) else x for x in b])
            else:
                setattr(self, a, dict2obj(b) if isinstance(b, dict) else b)


def get_bgp_service_state():
    command = "docker exec bgp ps -e | grep fpmsyncd"
    
    try:
        #print "BGP service command :"+command
        proc = subprocess.Popen(command,
                                stdout=subprocess.PIPE,
                                shell=True,
                                stderr=subprocess.STDOUT)
        stdout = proc.communicate()[0]
        proc.wait()
        result = stdout.rstrip('\n')

    except OSError, e:
        raise OSError("Cannot detect routing-stack")

    return result

#Retrive the process state
def get_process_state(service):
    command = "systemctl status {} |grep running".format(service)

    try:
        proc = subprocess.Popen(command,
                                stdout=subprocess.PIPE,
                                shell=True,
                                stderr=subprocess.STDOUT)
        stdout = proc.communicate()[0]
        proc.wait()
        result = stdout.rstrip('\n')

    except OSError, e:
        raise OSError("Cannot detect routing-stack")

    #if service == "bgp" and result != "":
    #    result = get_bgp_service_state()

    return (result)



#Reterive the core service status
def get_system_status():
    """ Shows the system ready status"""
    service_list = [
        'swss',
        'bgp',
        'teamd',
        'pmon',
        'syncd',
        'database',
        'mgmt-framework',
    ]


    app_db = SonicV2Connector(host="127.0.0.1")
    app_db.connect(app_db.APPL_DB)


    pstate = "System is ready"
    for service in service_list:
        try:

            state = get_process_state(service)
            if state == "":
                pstate=None
                break
        except Exception as e:
            logger.log_error( str(e))

    if pstate is not None:
        pstate  = app_db.get(app_db.APPL_DB, 'PORT_TABLE:PortInitDone', 'lanes')
    else:
        return ("DOWN", "Core services are down")
    
    if pstate is not None:
        return ("UP", "Ready")
    else:
        return ("DOWN", "Ports are not initialized!")

#Shows the system status message on the console and syslog 
def show_system_status(state, msg):
    if state == "UP":
        logger.log_info( "System is ready")
        with open('/dev/console', 'a') as console:
            console.write("\n\n{} System is ready \n\n ".format(datetime.datetime.now().strftime("%b %d %H:%M:%S.%f")))
    else:
        logger.log_info( " System is not ready")
        with open('/dev/console', 'a') as console:
            console.write("\n\n{} System is not ready - {} \n\n ".format(datetime.datetime.now().strftime("%b %d %H:%M:%S.%f"), msg))

def post_system_status(state):
    state_db = swsscommon.DBConnector(swsscommon.STATE_DB, REDIS_HOSTNAME, REDIS_PORT, REDIS_TIMEOUT_MS)
    #sys_tbl = swsscommon.Table(state_db, swsscommon.SYSTEM_READY_TABLE)
    sys_tbl = swsscommon.Table(state_db, SYSTEM_READY_TABLE)

    fvs = swsscommon.FieldValuePairs([("Status", state)])
    sys_tbl.set("SYSTEM_STATE", fvs)

#Checks the currest system status
def check_system_status(event):
    global SYSTEM_STATE
    (cstate, msg) = get_system_status()
    if SYSTEM_STATE != cstate:
        SYSTEM_STATE=cstate
        show_system_status(SYSTEM_STATE, msg)
        post_system_status(SYSTEM_STATE)



##############################################################
#             Listern for APPDB state event                  #
##############################################################
def subscribe_appdb(queue):

    while True:
        try:
            logger.log_debug( "Listerning for AppDB event...")
            SELECT_TIMEOUT_MS = 1000 * 2

            db = swsscommon.DBConnector(swsscommon.APPL_DB, REDIS_HOSTNAME, REDIS_PORT, REDIS_TIMEOUT_MS)
            sel = swsscommon.Select()
            cst = swsscommon.SubscriberStateTable(db, swsscommon.STATE_PORT_TABLE_NAME)
            sel.addSelectable(cst)

            while True:
                (state, c) = sel.select(SELECT_TIMEOUT_MS)
                if state == swsscommon.Select.OBJECT:
                    (key, op, cfvs) = cst.pop()
                    sys.stdout.write("")
                    sys.stdout.flush()
                    if key == 'PortInitDone':
                        queue.put("PORT_EVENT")
        except Exception as e:
            logger.log_error( str(e))

        time.sleep(2)

#Start the subprocess to listernt the APPDB state event
def subscribe_appdb_event_thread(queue):
    while True:
        try:
            process_appdb_event = Process(target=subscribe_appdb, args=(queue,) )
            process_appdb_event.start()
            process_appdb_event.join()
        except Exception as e:
            logger.log_error( str(e))

        time.sleep(1)



##############################################################
#             Listern for System service event               #
##############################################################
QUEUE=None
def OnJobRemoved(id, job, unit, result):

    global QUEUE

    logger.log_debug('{}: Job Removed: {}, {}, {} '.format( id, job, unit, result))
    if result == "done":
        QUEUE.put("SERVICE_EVENT")
        return

#Sub process for listerning the systemd event on dbus
def subscribe_service_event(queue):

    logger.log_debug( "Listerning for systemd service event..")
    DBusGMainLoop(set_as_default=True)

    bus = dbus.SystemBus()
    systemd = bus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
    manager = dbus.Interface(systemd, 'org.freedesktop.systemd1.Manager')

    manager.Subscribe()
    manager.connect_to_signal('JobRemoved', OnJobRemoved)

    loop = GObject.MainLoop()
    loop.run()


#Start the subprocess to listern the systemd service state change event
def subscribe_service_event_thread(queue):
    while True:
        try:
            process_service_event = Process(target=subscribe_service_event, args=(queue,) )
            process_service_event.start()
            process_service_event.join()
        except Exception as e:
            logger.log_error( str(e))

        time.sleep(1)


#Handle docker events
def docker_event_handler(event, data):
        QUEUE.put("DOCKER_EVENT")


#Listern for docker events
def subscribe_docker_event_thread(queue):
    ahab = Ahab(handlers=[docker_event_handler])
    ahab.listen()




syscfg={}
syscfg['INTERVAL']=3*60 # Seconds


def convert_bytes(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n


def dump_memory_usage():

    total=0
    for p in sorted( psutil.process_iter(attrs=['name', 'memory_info']), key=lambda p: p.info['memory_info'].rss,reverse=True):
        if p.info['memory_info'].rss > 10*1024*1024 : # 10 MB
            #logger.log_info("MEM:: {}".format(p.info))
            logger.log_info("MEM :: Name:{}, Pid:{}, Rss:{} ".format( get_proc_name(p), p.pid, convert_bytes(p.info['memory_info'].rss)))

        total += p.info['memory_info'].rss

    logger.log_info("MEM :: All the process memory usage: {}".format( convert_bytes(total)))



def dump_disk_usage():
    disk_partitions = psutil.disk_partitions(all=False)
    for partition in disk_partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        device = {'device': partition.device,
	      'mountpoint': partition.mountpoint,
	      'fstype': partition.fstype,
	      'opts': partition.opts,
	      'total': usage.total,
	      'used': usage.used,
	      'free': usage.free,
	      'percent': usage.percent
	      }

	logger.log_info("DISK:: {}".format(device))
    

class Data:
    size=10
    sidx=0
    data={}
    state=None
    LogLevel=None
    CurrentLevel=None

    def __init__(self):
	pass
    
    def getSize(self):
        return self.psize

    def setNextIdx(self):
        self.sidx+=1
        if self.sidx == self.size:
            self.sidx=0
        
    def setData(self, obj):
        self.data[self.sidx]=obj
        self.setNextIdx()

    def getData(self, idx):
        return self.data[idx]

    def printAll(self):
        logger.log_info( "{}".format([self.data[idx].used for idx in range(0,self.size) if idx in  self.data ]))


class DataArray:
    size=10
    sidx=0
    data={}
    state=None
    LogLevel=None

    def __init__(self):
	pass
    
    def getSize(self):
        return self.psize

    def setNextIdx(self):
        self.sidx+=1
        if self.sidx == self.size:
            self.sidx=0

    def setData(self,obj, attr):
        obj.attr = attr
        if attr not in self.data.keys():
            self.data[self.sidx] = {}
        self.data[self.sidx][attr]=obj

    def setDataNext(self,obj, attr):
        self.setData(obj,attr)
        self.setNextIdx()

    def getData(self, idx):
        return self.data[idx]

    def printAll(self):
        for idx in range(0,self.size):
            if idx in  self.data:
                for attr in self.data[idx].keys():
                    if attr in self.data[idx]:
                        logger.log_info( "PPMM attr:{}, name:{}".format(  self.data[idx][attr].attr , self.data[idx][attr]._name)  )


class DataList:
    data={}

    def __init__(self):
	pass

    def setData(self,obj, attr):
        obj.attr = attr
        if attr not in self.data.keys():
            self.data[self.sidx] = {}
        self.data[self.sidx][attr]=obj

    def setDataNext(self,obj, attr):
        self.setData(obj,attr)
        self.setNextIdx()

    def getData(self, idx):
        return self.data[idx]

    def printAll(self):
        for idx in range(0,self.size):
            if idx in  self.data:
                for attr in self.data[idx].keys():
                    if attr in self.data[idx]:
                        logger.log_info( "PPMM attr:{}, name:{}".format(  self.data[idx][attr].attr , self.data[idx][attr]._name)  )


            


def get_threshold(resource, total, config):
    
    tlimit = resource/(total/100)

    for cfg in config['Range']:
        if tlimit >= cfg['Start'] and tlimit <= cfg['End']:
            return cfg


def send_syslog(config, level,  msg):

    for cfg in config['Range']:
        if cfg['Level'] == level:
            cfg['LogLevel'](msg)

def get_threshold_percent(threshold):
    if threshold['Start'] == 00:
        return "[{}-{}%]".format(threshold['Start'],threshold['End'])
    return "{}%".format(threshold['Start'])


class SYSMEM:
    
    Threshold={"Range":[ \
            { "Level":"NORMAL",   "Start":00, "End": 70, "LogLevel": logger.log_info },    \
            { "Level":"WARNING",  "Start":70, "End": 80, "LogLevel": logger.log_warning }, \
            { "Level":"ALERT",    "Start":80, "End": 90, "LogLevel": logger.log_alert },   \
            { "Level":"CRITICAL", "Start":90, "End": 100, "LogLevel": logger.log_crit }    \
            ]}
    FreeLevel="NORMAL"
    UsedLevel="NORMAL"

    def checkRange(self, smem):

        show_dump=0

        # Check for System free Memory usage
        #logger.log_info("SYSMEM:: Total {}, Free {}, Used {}, Avail {}".\
                #format(convert_bytes(smem.total), convert_bytes(smem.free), convert_bytes(smem.used), convert_bytes(smem.available)))
        free_clevel = get_threshold(smem.total-(smem.free), smem.total, self.Threshold)
        free_tlimit = smem.free/((smem.total)/100)
        #logger.log_info("SYSMEM:: FREE THRESHOLD {} Level: {}".format(free_tlimit, free_clevel['Level']))

        if self.FreeLevel != free_clevel['Level'] :
            show_dump=1
            self.FreeLevel = free_clevel['Level']
            send_syslog(self.Threshold, free_clevel['Level'], "System free memory usage is below {}%, Total: {}, Free: {}, Used: {}, Buffers: {}, Cached: {}, Avail: {}".\
                    format( free_tlimit, convert_bytes(smem.total), \
                    convert_bytes(smem.free), convert_bytes(smem.used), \
                    convert_bytes(smem.buffers), convert_bytes(smem.cached), \
                    convert_bytes(smem.available)))
        

        # Check for System free Memory usage
        used_clevel = get_threshold(smem.used, smem.total, self.Threshold)
        used_tlimit = smem.used/(smem.total/100)
        #logger.log_info("SYSMEM:: USED THRESHOLD {} Level: {}".format(used_tlimit, used_clevel['Level']))

        if self.UsedLevel != used_clevel['Level'] :
            show_dump=1
            self.UsedLevel = used_clevel['Level']
            send_syslog(self.Threshold, used_clevel['Level'], "System used memory usage is above {}%, Total: {}, Free: {}, Used: {}, Buffers: {}, Cached: {}, Avail: {}".\
                    format( used_tlimit, convert_bytes(smem.total), \
                    convert_bytes(smem.free), convert_bytes(smem.used), \
                    convert_bytes(smem.buffers), convert_bytes(smem.cached), \
                    convert_bytes(smem.available)))

        if show_dump == 1 :
             dump_memory_usage()




class ProcessData:
    data={}

    def __init__(self):
	pass
    
    def getData(self,obj, attr):
        obj.attr = attr
        if attr not in self.data.keys():
            self.data[attr] = {"MemLogLevel":"NORMAL", "CpuLogLevel":"NORMAL","Data":obj}

        return self.data[attr]


    def printAll(self):
        for attr in self.data.keys():
            logger.log_info( "PPMM data:{}".format(  self.data[attr].data)  )


def get_proc_name(p):
    if p.name().startswith('python') or \
       p.name() == 'bash' or \
       p.name() == 'sh':
           for cmd in p.cmdline()[1:]:
               if cmd.startswith('-'):
                   continue
               return "[{} {}]".format(p.cmdline()[0],cmd)

    return p.info['name']

class SYSPPMEM:
    
    MemThreshold={ "Range":[ 
            { "Level":"NORMAL",   "Start":00, "End": 50, "LogLevel": logger.log_info },    \
            { "Level":"WARNING",  "Start":50, "End": 60, "LogLevel": logger.log_warning }, \
            { "Level":"ALERT",    "Start":60, "End": 70, "LogLevel": logger.log_alert },   \
            { "Level":"CRITICAL", "Start":70, "End": 100, "LogLevel": logger.log_crit }    \
            ]}

    CpuThreshold={ "Range":[
            { "Level":"NORMAL",   "Start":00, "End": 70, "LogLevel": logger.log_info },    \
            { "Level":"WARNING",  "Start":70, "End": 80, "LogLevel": logger.log_warning }, \
            { "Level":"ALERT",    "Start":80, "End": 90, "LogLevel": logger.log_alert },   \
            { "Level":"CRITICAL", "Start":90, "End": 100, "LogLevel": logger.log_crit }    \
            ]}
    Data=ProcessData()

    def checkRange(self, sysmem, ppmem):


        # Check for System free Memory usage
        for p in ppmem:
            try:

                if p.info['memory_info'].rss ==0:
                    continue

                data=self.Data.getData(p, p.pid)

                used_tlimit = p.info['memory_info'].rss/(sysmem.total/100)       
                #logger.log_info("SYSMEM:: Name: {}, Pid:{}, USED RSS {} Total: {}, Percentag:{} ".\
                        #format( get_proc_name(p), p.pid, \
                        #convert_bytes(p.info['memory_info'].rss),convert_bytes(sysmem.total), used_tlimit))
                used_clevel=get_threshold(p.info['memory_info'].rss, sysmem.total, self.MemThreshold)
                if data['MemLogLevel'] != used_clevel['Level'] :
                    used_tlimit = p.info['memory_info'].rss/(sysmem.total/100)
                    show_dump=1
                    data['MemLogLevel'] = used_clevel['Level']
                    send_syslog(self.MemThreshold, used_clevel['Level'], "Per process memory threshold exceeded for process {}[{}], threshold {} of system memory, current usage {}".\
                        format( \
                        get_proc_name(p), p.pid, \
                        get_threshold_percent(used_clevel), \
                        convert_bytes(p.info['memory_info'].rss)))



                pcpu = p.cpu_percent(interval=None)
                # Per Process CPU monitoring
                #cpu_clevel=get_threshold(pcpu/psutil.cpu_count(), 100, self.CpuThreshold)
                cpu_clevel=get_threshold(pcpu, 100, self.CpuThreshold)
                if data['CpuLogLevel'] != cpu_clevel['Level'] :
                    data['CpuLogLevel'] = cpu_clevel['Level']
                    send_syslog(self.CpuThreshold, cpu_clevel['Level'], "CPU usage of process {}[{}] is {}%".\
                            format(get_proc_name(p), p.pid, pcpu))
            except Exception as e:
                #TypeError
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(e).__name__, e.args)




class DISK:

    Threshold={ "Range":[
            { "Level":"NORMAL",   "Start":00, "End": 70, "LogLevel": logger.log_info },    \
            { "Level":"WARNING",  "Start":70, "End": 80, "LogLevel": logger.log_warning }, \
            { "Level":"ALERT",    "Start":80, "End": 90, "LogLevel": logger.log_alert },   \
            { "Level":"CRITICAL", "Start":90, "End": 100, "LogLevel": logger.log_crit }    \
            ]}
    DiskLevel="NORMAL"
    Partition="/"

    def __init__(self, partition):
        self.Partition=partition

    def checkRange(self):

        root = psutil.disk_usage(self.Partition)
        disk_clevel=get_threshold(root.used, root.total, self.Threshold)
        if self.DiskLevel != disk_clevel['Level']:
            self.DiskLevel = disk_clevel['Level']
            send_syslog(self.Threshold, disk_clevel['Level'], "DISK usage of '/' is above {}, Total: {}, Free: {}, Used: {}".\
                format(get_threshold_percent(disk_clevel), convert_bytes(root.total), \
                convert_bytes(root.free), convert_bytes(root.used)))
            dump_disk_usage()



class ResourceMonitor:

    smem = SYSMEM()
    pmem = SYSPPMEM()
    pdisk = DISK('/')
    pdisklog = DISK('/var/log')

    def Monitor(self, queue):
        sysmem = psutil.virtual_memory()

        try:
            self.smem.checkRange(sysmem)
            ppmem=[p for p in sorted(psutil.process_iter(attrs=['name', 'memory_info', 'cpu_times','cmdline']),key=lambda p: p.info['memory_info'].rss,reverse=True)]
            self.pmem.checkRange(sysmem, ppmem)
        except Exception as e:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, e.args)


        self.pdisk.checkRange()
        self.pdisklog.checkRange()


rm = ResourceMonitor()

# Monitor the memory usage periodically
def memory_monitor_service_thread(queue):

    while True:
        rm.Monitor(queue)
        time.sleep(syscfg['INTERVAL'])


#Start the thread for monitoring the APPDB and systemd service state change event 
def system_service():

    global QUEUE
    QUEUE = mp.Queue()

    thread_service_event = threading.Thread(target=subscribe_service_event_thread, name='service', args=(QUEUE,)) 
    thread_service_event.start()


    thread_statedb = threading.Thread(target=subscribe_appdb_event_thread, name='appdb', args=(QUEUE,)) 
    thread_statedb.start()


    thread_docker_event = threading.Thread(target=subscribe_docker_event_thread, name='docker', args=(QUEUE,)) 
    thread_docker_event.start()


    thread_docker_event = threading.Thread(target=memory_monitor_service_thread, name='memory', args=(QUEUE,)) 
    thread_docker_event.start()


    # Queue to receive the APPDB and Systemd state change event
    while True:
        event = QUEUE.get()
        logger.log_debug( "System event [ "+event+" ] is received")
        check_system_status(event)

    thread_statedb.join()
    thread_service_event.join()
    thread_docker_event.join()


#Main method to lanch the process in background
if __name__ == "__main__":

    #init_log()

    parser = argparse.ArgumentParser()
    parser.add_argument("--daemon", action='store_true', help="Start with daemon mode")
    args = parser.parse_args()

    if args.daemon:
        try:
            pid = os.fork()
        except OSError:
            logger.log_error("Could not create a child process\n")
        #parent
        if pid != 0:
            exit()
    
    system_service()

