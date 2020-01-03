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

   # check if ASIC is detected
   lspci | grep "Ethernet controller: Broadcom Limited Device b" &> /dev/null
   if [[ "$?" != "0" ]]
   then
       echo $fail
       exit
   fi

   docker ps | grep "syncd" &> /dev/null
   if [[ "$?" != "0" ]]
   then
	echo "Syncd Error"
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
   echo "(error reading diagnostic log)"
}

LOG()
{
    echo "[ `date '+%T'` ] "$1""
}

main() {
    verify_asic_diag
}

main
