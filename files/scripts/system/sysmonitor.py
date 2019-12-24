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
from multiprocessing import Process,Value
import multiprocessing as mp
from ahab import Ahab

from swsscommon import swsscommon
import sonic_device_util
from swsssdk import ConfigDBConnector
from swsssdk import SonicV2Connector


SYSLOG_IDENTIFIER="system#state"
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
def init_log():
    global logger
    logger = Logger(SYSLOG_IDENTIFIER)

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

    init_log()

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

