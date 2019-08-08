#!/usr/bin/env bash

sleep 60
rm -f /var/run/checkers.pid
rm -f /var/run/vrrp.pid
rm -f /var/run/keepalived.pid
keepalived

