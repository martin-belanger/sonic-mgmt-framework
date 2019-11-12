#!/usr/bin/python
import sys
import time
import json
import ast
from rpipe_utils import pipestr
from scripts.render_cli import show_cli_output
import cli_client as cc
import re
import urllib3
urllib3.disable_warnings()

def invoke(func, args):
    body = {}
    aa = cc.ApiClient()

    if func == 'get_openconfig_ztp_ztp_state':
        path = cc.Path('/restconf/data/openconfig-ztp:ztp/state')
	return aa.get(path)
    else:
        print('in else')
	path = cc.Path('/restconf/data/openconfig-ztp:ztp/config')
	print("path done:",sys.argv)
	if 'enable' in sys.argv:
	    body["openconfig-ztp:admin_mode"] =  True 
        else:
	    body["openconfig-ztp:admin_mode"] = False
        return aa.post(path,body)



def run(func, args):
    try:
	api_response = invoke(func, args)
        if api_response.ok():
	    response = api_response.content
	    if response is None:
                print ("Success")
            elif 'openconfig-ztp:state' in response.keys():
                value = response['openconfig-ztp:state']
		if value is not None:
                    show_cli_output(sys.argv[2],value)
        else:
            print('Success')
    except:
	print("%Error: Transaction Failure")

if __name__ == '__main__':

    pipestr().write(sys.argv)
    run(sys.argv[1], sys.argv[2:])


