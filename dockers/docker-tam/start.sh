#!/usr/bin/env bash

rm -f /var/run/rsyslogd.pid

supervisorctl start rsyslogd

supervisorctl start thresholdmgr

supervisorctl start tsmgrd

supervisorctl start dropmgrd

supervisorctl start ifamgrd

supervisorctl start snapshotmgr
