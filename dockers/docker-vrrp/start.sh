#!/usr/bin/env bash

rm -f /var/run/rsyslogd.pid
rm -f /var/run/keepalived/*

supervisorctl start rsyslogd


supervisorctl start vrrpsyncd

supervisorctl start keepalived
