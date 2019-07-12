#!/usr/bin/python
import sys
import time
import json
import ast
import openconfig_platform_client
from openconfig_platform_client.rest import ApiException
from scripts.render_cli import show_cli_output


import urllib3
urllib3.disable_warnings()

blocked_fields = {'parent':0, 'used_power':0, 'allocated_power':0, 'temperature':0}
plugins = dict()

def filter_json_value(value):
    for key,val in value.items():
        if key in blocked_fields:
            del value[key]
    return value

def register(func):
    """Register sdk client method as a plug-in"""
    plugins[func.__name__] = func
    return func


def call_method(name, args):
    method = plugins[name]
    return method(args)

def generate_body(func, args):
    body = None
    # Get the rules of all ACL table entries.

    if func.__name__ == 'get_openconfig_platform_components':
        keypath = []

    else:
       body = {}

    return keypath,body


def run(func, args):
    c = openconfig_platform_client.Configuration()
    c.verify_ssl = False
    aa = openconfig_platform_client.OpenconfigPlatformApi(api_client=openconfig_platform_client.ApiClient(configuration=c))

    # create a body block
    keypath, body = generate_body(func, args)

    try:
        if body is not None:
           api_response = getattr(aa,func.__name__)(*keypath, body=body)
           
        else :
           api_response = getattr(aa,func.__name__)(*keypath)
           
        if api_response is None:
            print ("Success")
        else:
            response = api_response.to_dict()
            value =  response['openconfig_platformcomponents']['component'][0]['state']
            if value is None:
                return
            show_cli_output(sys.argv[2],filter_json_value(value))

    except ApiException as e:
        print("Exception when calling OpenconfigPlatformApi->%s : %s\n" %(func.__name__, e))

if __name__ == '__main__':

    #pdb.set_trace()
    func = eval(sys.argv[1], globals(), openconfig_platform_client.OpenconfigPlatformApi.__dict__)
    run(func, sys.argv[2:])
