#!/bin/bash

asic_diag_log_file=$1
temp_file=/tmp/asic_diag

verify_asic_diag() {
   #docker exec -it syncd bash

   docker ps | grep "syncd" &> /dev/null
   if [[ "$?" != "0" ]]
   then
	LOG "Syncd Error"
	exit
   fi

   docker cp syncd:${asic_diag_log_file} ${temp_file} &> /dev/null
   if [[ -e ${temp_file} ]]
   then
       cat ${temp_file} | grep "ERROR" &> /dev/null
       if [[ "$?" == "1" ]]
       then
           echo "PASS"
           rm ${temp_file}
           exit
       fi
       echo "FAIL"
       rm ${temp_file}
       exit
   fi
   echo "FAIL"
   LOG '93missing log file'94
}

LOG()
{
    echo "[ `date '+%T'` ] "$1""
}

main() {
    LOG "Broadcom SONiC ASIC Diagnostic Test: "
	verify_asic_diag
}

main
