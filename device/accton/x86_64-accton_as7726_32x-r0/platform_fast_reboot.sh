#!/bin/bash 

PLAT_SERVICES="as7726-32x-platform-monitor.service as7726-32x-platform-monitor-psu.service as7726-32x-platform-monitor-fan.service"
PLAT_UTIL=/usr/local/bin/accton_as7726_32x_util.py

for service in ${PLAT_SERVICES}
do
    echo "Stopping platform service $service"
    systemctl stop $service 
done

${PLAT_UTIL} clean >/dev/null

exit 0
