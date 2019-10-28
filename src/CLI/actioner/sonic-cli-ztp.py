#!/usr/bin/python
import sys
import time
import json
import ast
import openconfig_ztp_client
from rpipe_utils import pipestr
from openconfig_ztp_client.rest import ApiException
from scripts.render_cli import show_cli_output


import urllib3
urllib3.disable_warnings()

plugins = dict()
temp_resp = {   'ZTP Admin Mode' : 'True',
                'ZTP Service'    : 'Inactive',
                'ZTP Status'     : 'SUCCESS',
                'ZTP Source'     : 'dhcp-opt67 (eth0)',
                'Runtime'        : '05m 31s',
                'Timestamp'      : '2019-09-11 19:12:16 UTC',
                'ZTP JSON Version' : '1.0',
                'activity-string':'ZTP Service is not running',
                'config-list' : {'configdb-json':{
                                                'Status'          : 'SUCCESS',
                                                'Runtime'         : '02m 48s',
                                                'Timestamp'       : '2019-09-11 19:11:55 UTC',
                                                'Exit Code'       : '0',
                                                'Ignore Result'   : 'False' },
                                 'connectivity-check':{
                                                'Status'          : 'SUCCESS',
                                                'Runtime'         : '04s',
                                                'Timestamp'       : '2019-09-11 19:12:16 UTC',
                                                'Exit Code'       : '0',
                                                'Ignore Result'   : 'False'}
                                }
                }
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

    if func.__name__ == 'get_openconfig_ztp_ztp_ztp_status':
        keypath = []

    else:
       body = {}

    return keypath,body


def run(func, args):
    c = openconfig_ztp_client.Configuration()
    c.verify_ssl = False
    aa = openconfig_ztp_client.OpenconfigZtpApi(api_client=openconfig_ztp_client.ApiClient(configuration=c))

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
            api_response = aa.api_client.sanitize_for_serialization(api_response)
            if 'ztp-status' in sys.argv:
               #show_cli_output(sys.argv[2],temp_resp)
                print(api_response)
            else:
                print('Success')

    except ApiException as e:
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
    #pdb.set_trace()
    func = eval(sys.argv[1], globals(), openconfig_ztp_client.OpenconfigZtpApi.__dict__)
    run(func, sys.argv[2:])


