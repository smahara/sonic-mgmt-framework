#!/usr/bin/python
import sys
import json
from rpipe_utils import pipestr
import sonic_watermark_telemetry_client
from scripts.render_cli import show_cli_output
from sonic_watermark_telemetry_client.rest import ApiException

import urllib3
urllib3.disable_warnings()

plugins = dict()

def register (func):
    plugins[func.__name__] = func
    return func

def call_method(name, args):
    method = plugins[name]
    return method(args)

def generate_body(func, args):
    body = None
    keypath = []
    if func.__name__ == 'get_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval':
        keypath = []
    elif func.__name__ =='patch_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval':
        keypath =[]
        body = {"sonic-watermark-telemetry:interval": int(args[0]) }
    else:
       body = {}

    return keypath,body

def run(func, args):

    c = sonic_watermark_telemetry_client.Configuration()
    c.verify_ssl = False
    aa = sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi(api_client=sonic_watermark_telemetry_client.ApiClient(configuration=c))

    # create a body block
    keypath, body = generate_body(func, args)

    try:
       if func.__name__ == 'get_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval':
            api_response = 120
            show_cli_output(args[0], api_response)
            return

        if body is not None:
           api_response = getattr(aa,func.__name__)(*keypath, body=body)
        else :
            api_response = getattr(aa,func.__name__)(*keypath)
            print (api_response)

        if api_response is None:
            print ("Success")
        else:
            api_response = aa.api_client.sanitize_for_serialization(api_response)
            if 'sonic-watermark-telemetry:interval' in api_response:
                value = api_response['sonic-watermark-telemetry:interval']
                if 'WATERMARK_TABLE' in value:
                    tup = value['WATERMARK_TABLE']
        if api_response is None:
            print("Failed")
        #else:
           #if func.__name__ == 'get_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval':
                #print (api_response)
                #show_cli_output(args[1], api_response)
           #return

    except ApiException as e:
        print("Exception when calling SonicTelemetryApi->%s : %s\n" %(func.__name__, e))
        return

if __name__ == '__main__':

    pipestr().write(sys.argv)
    func = eval(sys.argv[1], globals(), sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi.__dict__)

    print sys.argv

    run(func, sys.argv[2:])
