#!/bin/bash

DISABLE_COREDUMP_CONF="/etc/sysctl.d/50-disable-coredump.conf"

if [ "$(redis-cli -n 4 HGET "COREDUMP|config" "enabled")" = "false" ] ; then
   echo "kernel.core_pattern=" > ${DISABLE_COREDUMP_CONF}
else
   rm -f ${DISABLE_COREDUMP_CONF}
fi

# Read sysctl conf files again
systemctl restart systemd-sysctl

## Update kdump configuration file

# Is kdump enabled?
kdump_enabled=$(redis-cli -n 4 HGET "KDUMP|config" "enabled")
if [ -z "$kdump_enabled" ]; then
    kdump_enabled="false"
fi
if [ "$kdump_enabled" = "false" ] ; then
    sed -i -e 's/USE_KDUMP=.*/USE_KDUMP=0/' /etc/default/kdump-tools
else
    sed -i -e 's/USE_KDUMP=.*/USE_KDUMP=1/' /etc/default/kdump-tools
fi

# Maximum number of dump files stored locally
kdump_num_dumps=$(redis-cli -n 4 HGET "KDUMP|config" "num_dumps")
if [ -z "$kdump_num_dumps" ]; then
    kdump_num_dumps=3
fi
sed -i -e "s/#*KDUMP_NUM_DUMPS=.*/KDUMP_NUM_DUMPS=${kdump_num_dumps}/" /etc/default/kdump-tools

# Memory allocated for kdump
kdump_memory=$(redis-cli -n 4 HGET "KDUMP|config" "memory")
if [ ! "$kdump_enabled" = "false" ] ; then
    # Changing in grub.cfg only the value differs from the one in /proc/cmdline
    sonic-kdump-config --memory $kdump_memory
fi

exit 0
