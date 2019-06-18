#!/usr/bin/env bash

rm -f /var/run/rsyslogd.pid
rm -f /var/run/nat/*

supervisorctl start rsyslogd

#supervisorctl start natmgrd

