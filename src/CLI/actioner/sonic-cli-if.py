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
import time
import json
import ast
import openconfig_interfaces_client
from rpipe_utils import pipestr
from openconfig_interfaces_client.rest import ApiException
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
    body = None
    keypath = []
    # Get the rules of all ACL table entries.
    if func.__name__ == 'patch_openconfig_interfaces_interfaces_interface_config_description':
       keypath = [ args[0] ]
       body = { "openconfig-interfaces:description": args[1] }
    elif func.__name__ == 'patch_openconfig_interfaces_interfaces_interface_config_enabled':
       keypath = [ args[0] ]
       if args[1] == "True":
           body = { "openconfig-interfaces:enabled": True }
       else:
           body = { "openconfig-interfaces:enabled": False }
    elif func.__name__ == 'patch_openconfig_interfaces_interfaces_interface_config_mtu':
       keypath = [ args[0] ]
       body = { "openconfig-interfaces:mtu":  int(args[1]) }
    elif func.__name__ == 'patch_openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_config':
       sp = args[1].split('/')
       keypath = [ args[0], 0, sp[0] ]
       body = { "openconfig-if-ip:config":  {"ip" : sp[0], "prefix-length" : int(sp[1])} }
    elif func.__name__ == 'patch_openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_config':
       sp = args[1].split('/')
       keypath = [ args[0], 0, sp[0] ]
       body = { "openconfig-if-ip:config":  {"ip" : sp[0], "prefix-length" : int(sp[1])} }
    elif func.__name__ == 'delete_openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_config_prefix_length':
       keypath = [args[0], 0, args[1]]
    elif func.__name__ == 'delete_openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_config_prefix_length':
       keypath = [args[0], 0, args[1]]
    elif func.__name__ == 'get_openconfig_interfaces_interfaces_interface':
	keypath = [args[0]]
    elif func.__name__ == 'get_openconfig_interfaces_interfaces':
        keypath = []
    elif func.__name__ == 'get_openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv4_neighbors':
	    keypath = [args[0], 0]
    elif func.__name__ == 'get_openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv6_neighbors':
	    keypath = [args[0], 0]
    else:
       body = {}

    return keypath,body

def getId(item):
    prfx = "Ethernet"
    state_dict = item['state']
    ifName = state_dict['name']

    if ifName.startswith(prfx):
        ifId = int(ifName[len(prfx):])
        return ifId
    return ifName

def run(func, args):

    c = openconfig_interfaces_client.Configuration()
    c.verify_ssl = False
    aa = openconfig_interfaces_client.OpenconfigInterfacesApi(api_client=openconfig_interfaces_client.ApiClient(configuration=c))

    # create a body block
    keypath, body = generate_body(func, args)

    try:
        if func.__name__ == 'get_openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv4_neighbors':
            if args[1] == 'summary':
                api_response = {"NEIGH_TABLE": {"Ethernet0:20.0.0.1" : {"type":"hash","value":{"neigh":"00:01:e8:8b:44:71","family":"IPv4"}},
                                       "Vlan10:30.0.0.1": {"type":"hash","value":{"neigh":"00:11:22:33:44:55","family":"IPv4"}},
                                       "Vlan2:40.0.0.1" :{"type":"hash","value":{"neigh":"00:01:02:03:04:05","family":"IPv4"}}}}
            elif args[1] == 'ip':
                if args[2] == '20.0.0.1':
                    api_response = {"NEIGH_TABLE": {"Ethernet0:20.0.0.1" : {"type":"hash","value":{"neigh":"00:01:e8:8b:44:71","family":"IPv4"}}}}
                elif args[2] == '30.0.0.1':
                    api_response = {"NEIGH_TABLE": {"Vlan10:30.0.0.1" : {"type":"hash","value":{"neigh":"00:11:22:33:44:55","family":"IPv4"}}},
                            "FDB_TABLE": {"Vlan10:00:11:22:33:44:55" : {"type":"hash","value":{"port":"Ethernet4","type":"dynamic"}}}}
                elif args[2] == '40.0.0.1':
                    api_response = {"NEIGH_TABLE": {"Vlan2:40.0.0.1" : {"type":"hash","value":{"neigh":"00:01:02:03:04:05","family":"IPv4"}}},
                            "FDB_TABLE": {"Vlan2:00:01:02:03:04:05" : {"type":"hash","value":{"port":"Ethernet8","type":"dynamic"}}}}
                else:
                    return
            elif args[1] == 'mac':
                if args[2] == '00:01:e8:8b:44:71':
                    api_response = {"NEIGH_TABLE": {"Ethernet0:20.0.0.1" : {"type":"hash","value":{"neigh":"00:01:e8:8b:44:71","family":"IPv4"}}}}
                elif args[2] == '00:11:22:33:44:55':
                    api_response = {"NEIGH_TABLE": {"Vlan10:30.0.0.1" : {"type":"hash","value":{"neigh":"00:11:22:33:44:55","family":"IPv4"}}},
                            "FDB_TABLE": {"Vlan10:00:11:22:33:44:55" : {"type":"hash","value":{"port":"Ethernet4","type":"dynamic"}}}}
                elif args[2] == '00:01:02:03:04:05':
                    api_response = {"NEIGH_TABLE": {"Vlan2:40.0.0.1" : {"type":"hash","value":{"neigh":"00:01:02:03:04:05","family":"IPv4"}}},
                            "FDB_TABLE": {"Vlan2:00:01:02:03:04:05" : {"type":"hash","value":{"port":"Ethernet8","type":"dynamic"}}}}
                else:
                    return
            elif args[1] == 'Ethernet0':
                api_response = {"NEIGH_TABLE": {"Ethernet0:20.0.0.1" : {"type":"hash","value":{"neigh":"00:01:e8:8b:44:71","family":"IPv4"}}}}
            elif args[1] == 'Ethernet0' and args[2] == 'summary':
                api_response = {"NEIGH_TABLE": {"Ethernet0:20.0.0.1" : {"type":"hash","value":{"neigh":"00:01:e8:8b:44:71","family":"IPv4"}}}}
            else:
                api_response = {"NEIGH_TABLE": {"Ethernet0:20.0.0.1" : {"type":"hash","value":{"neigh":"00:01:e8:8b:44:71","family":"IPv4"}},
                                       "Vlan10:30.0.0.1": {"type":"hash","value":{"neigh":"00:11:22:33:44:55","family":"IPv4"}},
                                       "Vlan2:40.0.0.1" :{"type":"hash","value":{"neigh":"00:01:02:03:04:05","family":"IPv4"}}},
                            "FDB_TABLE": {"Vlan10:00:11:22:33:44:55" : {"type":"hash","value":{"port":"Ethernet4","type":"dynamic"}},
                                       "Vlan2:00:01:02:03:04:05"  : {"type":"hash","value":{"port":"Ethernet8","type":"dynamic"}}}}

            show_cli_output(args[0], api_response)
            return
        elif func.__name__ == 'get_openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv6_neighbors':
            if args[1] == 'summary':
                api_response = {"NEIGH_TABLE": {"Ethernet0:20::1" : {"type":"hash","value":{"neigh":"00:01:e8:8b:44:71","family":"IPv6"}},
                                       "Vlan10:30::1": {"type":"hash","value":{"neigh":"00:11:22:33:44:55","family":"IPv6"}},
                                       "Vlan2:40::1" :{"type":"hash","value":{"neigh":"00:01:02:03:04:05","family":"IPv6"}}}}
            elif args[1] == 'ip':
                if args[2] == '20::1':
                    api_response = {"NEIGH_TABLE": {"Ethernet0:20::1" : {"type":"hash","value":{"neigh":"00:01:e8:8b:44:71","family":"IPv6"}}}}
                elif args[2] == '30::1':
                    api_response = {"NEIGH_TABLE": {"Vlan10:30::1" : {"type":"hash","value":{"neigh":"00:11:22:33:44:55","family":"IPv6"}}},
                            "FDB_TABLE": {"Vlan10:00:11:22:33:44:55" : {"type":"hash","value":{"port":"Ethernet4","type":"dynamic"}}}}
                elif args[2] == '40::1':
                    api_response = {"NEIGH_TABLE": {"Vlan2:40::1" : {"type":"hash","value":{"neigh":"00:01:02:03:04:05","family":"IPv6"}}},
                            "FDB_TABLE": {"Vlan2:00:01:02:03:04:05" : {"type":"hash","value":{"port":"Ethernet8","type":"dynamic"}}}}
                else:
                    return
            elif args[1] == 'mac':
                if args[2] == '00:01:e8:8b:44:71':
                    api_response = {"NEIGH_TABLE": {"Ethernet0:20::1" : {"type":"hash","value":{"neigh":"00:01:e8:8b:44:71","family":"IPv6"}}}}
                elif args[2] == '00:11:22:33:44:55':
                    api_response = {"NEIGH_TABLE": {"Vlan10:30::1" : {"type":"hash","value":{"neigh":"00:11:22:33:44:55","family":"IPv6"}}},
                            "FDB_TABLE": {"Vlan10:00:11:22:33:44:55" : {"type":"hash","value":{"port":"Ethernet4","type":"dynamic"}}}}
                elif args[2] == '00:01:02:03:04:05':
                    api_response = {"NEIGH_TABLE": {"Vlan2:40::1" : {"type":"hash","value":{"neigh":"00:01:02:03:04:05","family":"IPv6"}}},
                            "FDB_TABLE": {"Vlan2:00:01:02:03:04:05" : {"type":"hash","value":{"port":"Ethernet8","type":"dynamic"}}}}
                else:
                    return
            elif args[1] == 'Ethernet0':
                    api_response = {"NEIGH_TABLE": {"Ethernet0:20::1" : {"type":"hash","value":{"neigh":"00:01:e8:8b:44:71","family":"IPv6"}}}}
            elif args[1] == 'Ethernet0' and args[2] == 'summary':
                    api_response = {"NEIGH_TABLE": {"Ethernet0:20::1" : {"type":"hash","value":{"neigh":"00:01:e8:8b:44:71","family":"IPv6"}}}}
            else:
                api_response = {"NEIGH_TABLE": {"Ethernet0:20::1" : {"type":"hash","value":{"neigh":"00:01:e8:8b:44:71","family":"IPv6"}},
                                       "Vlan10:30::1": {"type":"hash","value":{"neigh":"00:11:22:33:44:55","family":"IPv6"}},
                                       "Vlan2:40::1" :{"type":"hash","value":{"neigh":"00:01:02:03:04:05","family":"IPv6"}}},
                            "FDB_TABLE": {"Vlan10:00:11:22:33:44:55" : {"type":"hash","value":{"port":"Ethernet4","type":"dynamic"}},
                                       "Vlan2:00:01:02:03:04:05"  : {"type":"hash","value":{"port":"Ethernet8","type":"dynamic"}}}}
            show_cli_output(args[0], api_response)
            return

        # Temporary code for #show vlan command with dummy data
        if func.__name__ == "get_openconfig_vlan_interfaces_interface_ethernet_switched_vlan_state":
            api_response = {'Vlan100': {'Ethernet20': 'tagged', 'Ethernet40': 'untagged'}}
            show_cli_output(args[0], api_response)
            return
        if body is not None:
           api_response = getattr(aa,func.__name__)(*keypath, body=body)
        else:
           api_response = getattr(aa,func.__name__)(*keypath)

        if api_response is None:
            print ("Success")
        else:
            # Get Command Output
            api_response = aa.api_client.sanitize_for_serialization(api_response)
            if 'openconfig-interfaces:interfaces' in api_response:
                value = api_response['openconfig-interfaces:interfaces']
                if 'interface' in value:
                    tup = value['interface']
                    value['interface'] = sorted(tup, key=getId)

            if api_response is None:
                print("Failed")
            else:
                if func.__name__ == 'get_openconfig_interfaces_interfaces_interface':
                     show_cli_output(args[1], api_response)
                elif func.__name__ == 'get_openconfig_interfaces_interfaces':
                     show_cli_output(args[0], api_response)
                else:
                     return
    except ApiException as e:
        #print("Exception when calling OpenconfigInterfacesApi->%s : %s\n" %(func.__name__, e))
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
    func = eval(sys.argv[1], globals(), openconfig_interfaces_client.OpenconfigInterfacesApi.__dict__)

    run(func, sys.argv[2:])
