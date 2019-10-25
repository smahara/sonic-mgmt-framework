#!/bin/bash

asic_diag_log_file=$1
asic_diag_output=/var/log/bcm_diag_post

if [ $# -lt 1 ];then
	log=/dev/null;
else
	log=$1
fi
pass="PASS"
fail="FAIL"

verify_asic_diag() {
   #docker exec -it syncd bash

   docker ps | grep "syncd" &> /dev/null
   if [[ "$?" != "0" ]]
   then
	LOG "Syncd Error"
	exit
   fi

   docker cp syncd:${asic_diag_output} ${log} &> /dev/null
   if [[ -e ${log} ]]
   then
       cat ${log} | grep "ERROR" &> /dev/null
       if [[ "$?" == "1" ]]
       then
           echo $pass
           exit
       fi
       echo $fail
       exit
   fi
   echo $fail
   LOG 'missing log file'
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
