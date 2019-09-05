#!/usr/bin/env python
import subprocess
import json
import sys 

ERR_MSG_JSON='/var/local/hwdiag/i2c/peripherals_err_msg.json'
with open(ERR_MSG_JSON, 'r') as f:
        err_msg = json.load(f)

class DiagUtil:
	def check_log_file_err_msg(self, prog, logfile):
		cmd = "grep -i " + "'" + err_msg[prog]['logfile'] + "' " + logfile
        	try:
             		error=subprocess.check_output(cmd, shell=True);
        	except subprocess.CalledProcessError as grepexc:
             		error=""

        	if error:
              		print "FAILED"
        	else:
              		print "PASS"
	
