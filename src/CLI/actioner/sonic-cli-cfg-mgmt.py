#!/usr/bin/python
###########################################################################
#
# Copyright 2019 Dell, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
###########################################################################

import sys
import json
import collections
import re
import cli_client as cc
from rpipe_utils import pipestr
from scripts.render_cli import show_cli_output



def invoke(func, args):
    body = None

    if len(args) < 2:
      print ("Error:Invalid arguments")
      exit(1)
    
    aa = cc.ApiClient()
    keypath = cc.Path('/restconf/operations/sonic-config-mgmt:copy')
    body = { "sonic-config-mgmt:input":{"source":args[0], "destination":args[1]}}
    if len(args) == 3:
        body["sonic-config-mgmt:input"].update({"overwrite":True})
    
    return aa.post(keypath, body)

def run(func, args):
    try:
        api_response = invoke(func, args)
        if api_response.ok():
            response = api_response.content
            if response is None:
                print "Success"
            else:
               status =response["sonic-config-mgmt:output"]
               if status["status"] != "SUCCESS.":
                  print status["status"] 
        else:
            #error response
            print api_response.error_message()

    except:
            # system/network error
            print "%Error: Transaction Failure"



if __name__ == '__main__':
    pipestr().write(sys.argv)
    #pdb.set_trace()
    run(sys.argv[1], sys.argv[2:])

