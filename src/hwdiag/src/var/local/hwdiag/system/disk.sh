#!/bin/bash
# Runs a quick test on SSD and prints results.
# Also extracts all the S.M.A.R.T data drom the disk and saves
# it to the logfile
#
if [ $# -lt 1 ];then
	log=/dev/null;
else
	log=$1
fi
pass="PASS"
fail="FAIL"

echo "--- Disk S.M.A.R.T Information ---" > $log
smartctl --all /dev/sda >> $log
echo "--- Running Quick Disk test  ---" >> $log
smartctl -H /dev/sda | grep PASSED >> $log

if [ $? -eq 0 ];then
	echo $pass
else
	echo $fail
fi

