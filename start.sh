#!/usr/bin/env bash

rm -f /var/run/rsyslogd.pid

supervisorctl start rsyslogd

echo "========================================================================="
echo "                    Starting Swagger Server for RESTCONF                 "
echo "========================================================================="
supervisorctl start swagger-server
