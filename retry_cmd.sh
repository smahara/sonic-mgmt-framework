#!/bin/bash

#set -x

## retry_cmd TRIES COMMAND....
##
## Attempts to issue the COMMAND up to TRIES times, with a short delay in between.
## - 1st arg:  number of attempts to try
## - remaining args:  the command to execute, along with all of its parameters
## Returns the final result of the command.
## A successful command execution prevents additional retries.
## example: retry_cmd 3 ping -c 1 localhost

if [ $# -le 1 ]; then
    echo "Usage $0 TRIES COMMAND..."
    exit 1
fi

tries=$1
shift;
# all remaining args comprise the command and its parameters
command="$@"

delay=1
rc=0

for i in $(seq 1 $tries); do
    [ $i -gt 1 ] && echo "Command failed, retrying ($i/$tries)"; sleep $delay
    eval $command && rc=0 && break || rc=$?
done
(exit $rc)
