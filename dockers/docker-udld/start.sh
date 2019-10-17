#!/usr/bin/env bash

rm -f /var/run/rsyslogd.pid
rm -f /var/run/udldd/*
#rm -f /var/run/udldsyncd/*
rm -f /var/run/udldmgrd/*

supervisorctl start rsyslogd

supervisorctl start udldd

#supervisorctl start udldsyncd

supervisorctl start udldmgrd

