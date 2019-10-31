#!/usr/bin/env bash

rm -f /var/run/rsyslogd.pid
rm -f /var/run/nat/*

mkdir -p /var/warmboot/nat

supervisorctl start rsyslogd

supervisorctl start natmgrd

sleep 2

supervisorctl start natsyncd

supervisorctl start restore_nat_entries

