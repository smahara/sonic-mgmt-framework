import sys
import time
import json
import ast
import sonic_wred_profile_client
from rpipe_utils import pipestr
from sonic_wred_profile_client.rest import ApiException
from scripts.render_cli import show_cli_output

import urllib3
urllib3.disable_warnings()


plugins = dict()

PARAM_PATCH_PREFIX='patch_sonic_wred_profile_sonic_wred_profile_wred_profile_wred_profile_list_'
PARAM_PATCH_PREFIX_LEN=len(PARAM_PATCH_PREFIX)
PARAM_DELETE_PREFIX='delete_sonic_wred_profile_sonic_wred_profile_wred_profile_wred_profile_list_'
PARAM_DELETE_PREFIX_LEN=len(PARAM_DELETE_PREFIX)

def register(func):
    """Register sdk client method as a plug-in"""
    plugins[func.__name__] = func
    return func


def call_method(name, args):
    method = plugins[name]
    return method(args)

def generate_body(func, args):
    body = None
    keypath = []
    showSuccess = True

    # Get the rules of all ECN table entries.
    if func.__name__ == 'get_sonic_wred_profile_sonic_wred_profile_wred_profile':
        keypath = [args[0]]
    elif func.__name__ == 'get_sonic_wred_profile_sonic_wred_profile':
        keypath = []
    elif func.__name__ == 'patch_sonic_wred_profile_sonic_wred_profile_wred_profile_wred_profile_list':
       keypath = [ args[0] ]
       body = { "sonic-wred-profile:name": args[0] }
       showSuccess = False
    elif func.__name__ == 'delete_sonic_wred_profile_sonic_wred_profile_wred_profile_wred_profile_list':
       keypath = [args[0]]
    elif func.__name__[0:PARAM_PATCH_PREFIX_LEN] == PARAM_PATCH_PREFIX:
       keypath = [ args[0] ]
       body = { "sonic-wred-profile:" + func.__name__[PARAM_PATCH_PREFIX_LEN:] :  (args[1]) }
       if len(args) == 2:
           showSuccess = False
    elif func.__name__[0:PARAM_DELETE_PREFIX_LEN] == PARAM_DELETE_PREFIX:
       keypath = [ args[0] ]
       if len(args) == 1:
           showSuccess = False
    else:
       body = {}

    return keypath,body,showSuccess

def run(func, args):

    c = sonic_wred_profile_client.Configuration()
    c.verify_ssl = False
    aa = sonic_wred_profile_client.SonicWredProfileApi(api_client=sonic_wred_profile_client.ApiClient(configuration=c))

    # create a body block
    keypath, body, showSuccess = generate_body(func, args)

    try:
        if body is not None:
           api_response = getattr(aa,func.__name__)(*keypath, body=body)
        else :
           api_response = getattr(aa,func.__name__)(*keypath)

        if api_response is None:
            if showSuccess:
                print ("Success")
        else:
            # Get Command Output
            api_response = aa.api_client.sanitize_for_serialization(api_response)
            if 'sonic-wred-profile:sonic-wred-profile' in api_response:
                value = api_response['sonic-wred-profile:sonic-wred-profile']
                if 'WRED_PROFILE' in value:
                    tup = value['WRED_PROFILE']

            if api_response is None:
                print("Failed")
            else:
                if func.__name__ == 'get_sonic_wred_profile_sonic_wred_profile_wred_profile_wred_profile_list':
                     show_cli_output(args[1], api_response)
                elif func.__name__ == 'get_sonic_wred_profile_sonic_wred_profile':
                     show_cli_output(args[0], api_response)
                else:
                     return
    except ApiException as e:
        print("Exception when calling get_sonic_wred_profile_sonic_wred_profile ->%s : %s\n" %(func.__name__, e))
        if e.body != "":
            body = json.loads(e.body)
            if "ietf-restconf:errors" in body:
                 err = body["ietf-restconf:errors"]
                 if "error" in err:
                     errList = err["error"]

                     errDict = {}
                     for dict in errList:
                         for k, v in dict.iteritems():
                              errDict[k] = v

                     if "error-message" in errDict:
                         print "%Error: " + errDict["error-message"]
                         return
                     print "%Error: Transaction Failure"
                     return
            print "%Error: Transaction Failure"
        else:
            print "Failed"

if __name__ == '__main__':

    pipestr().write(sys.argv)
    func = eval(sys.argv[1], globals(), sonic_wred_profile_client.SonicWredProfileApi.__dict__)

    run(func, sys.argv[2:])

