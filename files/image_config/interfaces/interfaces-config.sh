#!/bin/bash

ifdown --force eth0

# Obtain port operational state information
redis-dump -d 0 -k "PORT_TABLE:Ethernet*"  -y > /tmp/port_table_data.json
if [ ! -e /tmp/port_table_data.json ] || \
   [ "$(cat /tmp/port_table_data.json)" = "" ]; then
   echo "{}" > /tmp/port_table_data.json
fi

# Create an input file with port operational state information
echo "{ \"PORT_TABLE\" : $(cat /tmp/port_table_data.json) }" > \
      /tmp/port_table.json

# Create /e/n/i file for existing and active interfaces
sonic-cfggen -d -j /tmp/port_table.json -t /usr/share/sonic/templates/interfaces.j2 > /etc/network/interfaces

# Clean-up created files
rm -f /tmp/port_table.json /tmp/port_table.json

[ -f /var/run/dhclient.eth0.pid ] && kill `cat /var/run/dhclient.eth0.pid` && rm -f /var/run/dhclient.eth0.pid
[ -f /var/run/dhclient6.eth0.pid ] && kill `cat /var/run/dhclient6.eth0.pid` && rm -f /var/run/dhclient6.eth0.pid

for intf_pid in $(ls -1 /var/run/dhclient*.Ethernet*.pid 2> /dev/null); do
  [ -f ${intf_pid} ] && kill `cat ${intf_pid}` && rm -f ${intf_pid}
done

sonic-cfggen -d -t /usr/share/sonic/templates/dhclient.conf.j2 > /etc/dhcp/dhclient.conf
systemctl restart networking

ifdown lo && ifup lo
