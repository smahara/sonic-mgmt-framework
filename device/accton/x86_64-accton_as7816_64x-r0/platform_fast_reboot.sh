#!/bin/bash 

PLAT_SERVICES="as7816-platform-init.service"
PLAT_UTIL=/usr/local/bin/accton_as7816_util.py

for service in ${PLAT_SERVICES}
do
    echo "Stopping platform service $service"
    systemctl stop $service 
done

${PLAT_UTIL} clean >/dev/null

exit 0
