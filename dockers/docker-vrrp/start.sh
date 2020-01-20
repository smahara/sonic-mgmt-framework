#!/usr/bin/env bash

rm -f /var/run/rsyslogd.pid
rm -f /var/run/keepalived*
rm -f /var/run/vrrpmgrd/*

supervisorctl start rsyslogd


supervisorctl start vrrpsyncd

supervisorctl start vrrpmgrd
