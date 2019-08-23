#!/bin/bash
# Scans dmesg output for Machine Check Events
#
if [ $# -lt 1 ];then
	log=/dev/null;
else
	log=$1
fi
pass="PASS"
fail="FAIL"
 
dmesg | grep -i "hardware error" > $log
if [ $? -eq 0 ];then
	echo $fail
else
	echo $pass
fi
