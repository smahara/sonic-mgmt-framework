#!/usr/bin/env bash

rm -f /var/run/rsyslogd.pid
rm -f /var/run/udldd/*
#rm -f /var/run/udldsyncd/*
rm -f /var/run/udldmgrd/*

grep "\-d 1:0:c:cc:cc:cc \-j DROP" <(ebtables -L) ; if [[ "$?" -eq "1" ]]; then ebtables -A FORWARD -d 01:00:0c:cc:cc:cc -j DROP; fi

supervisorctl start rsyslogd

supervisorctl start udldd

#supervisorctl start udldsyncd

supervisorctl start udldmgrd

