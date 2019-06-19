#!/bin/bash

ifdown --force eth0

sonic-cfggen -d -t /usr/share/sonic/templates/interfaces.j2 > /etc/network/interfaces

[ -f /var/run/dhclient.eth0.pid ] && kill `cat /var/run/dhclient.eth0.pid` && rm -f /var/run/dhclient.eth0.pid
[ -f /var/run/dhclient6.eth0.pid ] && kill `cat /var/run/dhclient6.eth0.pid` && rm -f /var/run/dhclient6.eth0.pid

for intf_pid in $(ls -1 /var/run/dhclient*.Ethernet*.pid 2> /dev/null); do
  [ -f ${intf_pid} ] && kill `cat ${intf_pid}` && rm -f ${intf_pid}
done

systemctl restart networking

ifdown lo && ifup lo
