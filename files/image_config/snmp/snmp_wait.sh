#!/bin/bash
RETRY_COUNT=24
RETRY_INTERVAL=5
wait_for_system_online()
{
   TRIES=${RETRY_COUNT}

   while [ ${TRIES} -gt 0 ]
   do
     RETRY=0
     STATUS="$(show system status 2> /dev/null)"
     if [ "${STATUS}" != "" ] && [ "${STATUS}" != "System is ready" ]; then
       RETRY=1
     fi

     logger -p DEBUG -t snmp "Waiting for system ready"

     [ ${RETRY} -eq 0 ] && break
     sleep ${RETRY_INTERVAL}
     TRIES=`expr $TRIES - 1`
   done

   if [ "${TRIES}" = "0" ]; then
     logger -t snmp "System is not ready, continuing"
     return 1
   fi

   return 0
}
wait_for_system_online
exit 0

