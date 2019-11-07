import sys
import time
import json
import ast
import sonic_config_mgmt_client
from sonic_config_mgmt_client.rest import ApiException
from scripts.render_cli import show_cli_output

import urllib3
urllib3.disable_warnings()


plugins = dict()

def register(func):
    """Register sdk client method as a plug-in"""
    plugins[func.__name__] = func
    return func


def call_method(name, args):
    method = plugins[name]
    return method(args)

def generate_body(func, args):
    
    print args
    body = None
    
    if func.__name__ == 'rpc_sonic_config_mgmt_config_save':
        keypath = []
        
        if len(args) > 0:
            body = { "sonic-config-mgmt:input": {"filename": args[0] }}
        else:
            body = []
    
    elif func.__name__ == 'get_sonic_error_sonic_error_error_neigh_table':
        keypath = []
    elif func.__name__ == 'get_sonic_error_sonic_error_error_route_table':
        keypath = []
    elif func.__name__ == 'get_sonic_error_sonic_error':
        keypath = []
    else:
       body = {}

    return keypath,body

def run(func, args):

    c = sonic_config_mgmt_client.Configuration()
    c.verify_ssl = False
    aa = sonic_config_mgmt_client.SonicConfigMgmtApi(api_client=sonic_config_mgmt_client.ApiClient(configuration=c))
    
    print "aa"
    print aa

    # create a body block
    keypath, body = generate_body(func, args)

    print "keypath"
    print keypath
    print "body"
    print body
    print "args"
    print args
    try:
        api_response = getattr(aa, func.__name__)(*keypath)
        print "api_response"  
        print api_response        
        if api_response is None:
            print ("Success")
        else:
            # Get Command Output
            api_response = aa.api_client.sanitize_for_serialization(api_response)

            if api_response is None:
                print("Failed")
            else:
               show_cli_output(args[0], api_response)

    except ApiException as e:
        #print("Exception when calling get_sonic_error ->%s : %s\n" %(func.__name__, e))
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

    func = eval(sys.argv[1], globals(), sonic_config_mgmt_client.SonicConfigMgmtApi.__dict__)

    run(func, sys.argv[2:])

