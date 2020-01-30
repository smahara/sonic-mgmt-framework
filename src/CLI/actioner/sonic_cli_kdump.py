#!/usr/bin/python3

import sys
import os
import json
import collections
import re
import cli_client as cc
from scripts.render_cli import show_cli_output

## Run an external command
def run_config_cmd(data):
    aa = cc.ApiClient()
    keypath = cc.Path('/restconf/operations/sonic-kdump:kdump-config')
    body = { "sonic-kdump:input":data}

    api_response = aa.post(keypath, body)
    if api_response.ok():
        response = api_response.content
        if response is not None and 'sonic-kdump:output' in response:
            print(response['sonic-kdump:output']['result'])
    else:
        print(api_response.error_message())

## Run an external command
def run_show_cmd(data):
    aa = cc.ApiClient()
    keypath = cc.Path('/restconf/operations/sonic-kdump:kdump-state')
    body = { "sonic-kdump:input":data}

    api_response = aa.post(keypath, body)
    if api_response.ok():
        response = api_response.content
        if response is not None and 'sonic-kdump:output' in response:
            print(response['sonic-kdump:output']['result'])
    else:
        print(api_response.error_message())

## Run a kdump 'show' command
def kdump_show_cmd(cmd):
    run_show_cmd({})

## Display kdump status
def cmd_show_status():
    run_show_cmd({"Param":"status"})

## Display kdump memory
def cmd_show_memory():
    run_show_cmd({"Param":"memory"})

## Display kdump num_dumps
def cmd_show_num_dumps():
    run_show_cmd({"Param":"num_dumps"})

## Enable kdump
def cmd_enable():
    run_config_cmd({"Enabled":True, "Num_Dumps":0, "Memory":""})

## Disable kdump
def cmd_disable():
    run_config_cmd({"Enabled":False, "Num_Dumps":0, "Memory":""})

## Set memory allocated for kdump
def cmd_set_memory(memory):
    run_config_cmd({"Enabled":False, "Num_Dumps":0, "Memory":memory})

## Set max numbers of kernel core files
def cmd_set_num_dumps(num_dumps):
    run_config_cmd({"Enabled":False, "Num_Dumps":num_dumps, "Memory":""})

def run(func, args):

    if func == 'show':
        if args[0] == 'kdump' and args[1] == 'status':
            cms_show_status()

if __name__ == '__main__':

    return run(sys.argv[1], sys.argv[2:])
