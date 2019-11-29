#!/usr/bin/env python

import swsssdk
import time
import sys
import logging
import syslog
from swsscommon import swsscommon

REDIS_HOSTNAME = "127.0.0.1"
REDIS_PORT = 6379
REDIS_TIMEOUT_MS = 0
SELECT_TIMEOUT_MSECS = 1000 * 2

SYSTEM_READY_TABLE = 'SYSTEM_READY'

def enable_counter_group(confdb, name):
    info = {}
    info['FLEX_COUNTER_STATUS'] = 'enable'
    confdb.mod_entry("FLEX_COUNTER_TABLE", name, info)

def enable_counters():
    confdb = swsssdk.ConfigDBConnector()
    confdb.connect()
    enable_counter_group(confdb, 'PORT')
    enable_counter_group(confdb, 'QUEUE')
    enable_counter_group(confdb, 'PFCWD')

    ## Check snapshot feature support.
    appl_db = swsssdk.SonicV2Connector(host='127.0.0.1')
    appl_db.connect(appl_db.APPL_DB)

    key = "SWITCH_TABLE:switch"
    entry = appl_db.get_all(appl_db.APPL_DB, key)
    if 'snapshot_supported' not in entry or entry['snapshot_supported'] == "False":
        enable_counter_group(confdb, 'PG_WATERMARK')
        enable_counter_group(confdb, 'QUEUE_WATERMARK')

def log_message(level, string):
    syslog.openlog("enable_counter", syslog.LOG_PID, facility=syslog.LOG_DAEMON)
    syslog.syslog( level, string )

def main():
    db = swsscommon.DBConnector(swsscommon.STATE_DB, REDIS_HOSTNAME, REDIS_PORT, REDIS_TIMEOUT_MS)
    sel = swsscommon.Select()
    st = swsscommon.SubscriberStateTable(db, SYSTEM_READY_TABLE)
    sel.addSelectable(st)

    while True:
        (state, c) = sel.select(SELECT_TIMEOUT_MSECS)
        if state == swsscommon.Select.OBJECT:
            (key, op, cfvs) = st.pop()
            if key == 'SYSTEM_STATE':
                fvp_dict = dict(cfvs)
                if op == "SET" and "Status" in fvp_dict:
                    if fvp_dict["Status"] == "UP":
                        time.sleep(2)
                        enable_counters()
                        log_message( syslog.LOG_INFO, "Flex counters enabled" )
                        break

if __name__ == '__main__':
    main()
