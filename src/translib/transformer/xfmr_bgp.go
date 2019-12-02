package transformer

import (
    "errors"
    "strings"
    "encoding/json"
    "translib/ocbinds"
    "os/exec"
    log "github.com/golang/glog"
)

func getBgpRoot (inParams XfmrParams) (*ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp, string, error) {
    pathInfo := NewPathInfo(inParams.uri)
    niName := pathInfo.Var("name")
    bgpId := pathInfo.Var("identifier")
    protoName := pathInfo.Var("name#2")
    var err error

    if len(pathInfo.Vars) <  3 {
        return nil, "", errors.New("Invalid Key length")
    }

    if len(niName) == 0 {
        return nil, "", errors.New("vrf name is missing")
    }
    if strings.Contains(bgpId,"BGP") == false {
        return nil, "", errors.New("BGP ID is missing")
    }
    if len(protoName) == 0 {
        return nil, "", errors.New("Protocol Name is missing")
    }

	deviceObj := (*inParams.ygRoot).(*ocbinds.Device)
    netInstsObj := deviceObj.NetworkInstances

    if netInstsObj.NetworkInstance == nil {
        return nil, "", errors.New("Network-instances container missing")
    }

    netInstObj := netInstsObj.NetworkInstance[niName]
    if netInstObj == nil {
        return nil, "", errors.New("Network-instance obj missing")
    }

    if netInstObj.Protocols == nil || len(netInstObj.Protocols.Protocol) == 0 {
        return nil, "", errors.New("Network-instance protocols-container missing or protocol-list empty")
    }

    var protoKey ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Key
    protoKey.Identifier = ocbinds.OpenconfigPolicyTypes_INSTALL_PROTOCOL_TYPE_BGP
    protoKey.Name = protoName
    protoInstObj := netInstObj.Protocols.Protocol[protoKey]
    if protoInstObj == nil {
        return nil, "", errors.New("Network-instance BGP-Protocol obj missing")
    }
    return protoInstObj.Bgp, niName, err
}

func exec_vtysh_cmd (vtysh_cmd string) (map[string]interface{}, error) {
    var err error
    oper_err := errors.New("Opertational error")

    log.Infof("Going to execute vtysh cmd ==> \"%s\"", vtysh_cmd)

    cmd := exec.Command("/usr/bin/docker", "exec", "bgp", "vtysh", "-c", vtysh_cmd)
    out_stream, err := cmd.StdoutPipe()
    if err != nil {
        log.Errorf("Can't get stdout pipe: %s\n", err)
        return nil, oper_err
    }

    err = cmd.Start()
    if err != nil {
        log.Errorf("cmd.Start() failed with %s\n", err)
        return nil, oper_err
    }

    var outputJson map[string]interface{}
    err = json.NewDecoder(out_stream).Decode(&outputJson)
    if err != nil {
        log.Errorf("Not able to decode vtysh json output: %s\n", err)
        return nil, oper_err
    }

    err = cmd.Wait()
    if err != nil {
        log.Errorf("Command execution completion failed with %s\n", err)
        return nil, oper_err
    }

    log.Infof("Successfully executed vtysh-cmd ==> \"%s\"", vtysh_cmd)

    if outputJson == nil {
        log.Errorf("VTYSH output empty !!!")
        return nil, oper_err
    }

    return outputJson, err
}

func fake_rib_exec_vtysh_cmd (vtysh_cmd string) (map[string]interface{}, error) {
    var err error
    var outputJson map[string]interface{}
//    outJsonBlob := `{
//        "vrfId": 0,
//        "vrfName": "default",
//        "tableVersion": 54,
//        "routerId": "200.9.0.4",
//        "defaultLocPrf": 100,
//        "localAS": 400,
//        "routes": {
//            "4.4.4.4\/32": {
//                "prefix":"4.4.4.4\/32",
//                "advertisedTo":{
//                    "10.10.10.1":{
//                    }
//                },
//                "paths":[
//                {
//                    "aspath":{
//                        "string":"Local",
//                        "segments":[
//                        ],
//                        "length":0
//                    },
//                    "origin":"incomplete",
//                    "med":0,
//                    "metric":0,
//                    "weight":32768,
//                    "valid":true,
//                    "sourced":true,
//                    "bestpath":{
//                        "overall":true
//                    },
//                    "lastUpdate":{
//                        "epoch":1494011680,
//                        "string":"Fri May  5 19:14:40 2017\n"
//                    },
//                    "nexthops":[
//                    {
//                        "ip":"0.0.0.0",
//                        "afi":"ipv4",
//                        "metric":0,
//                        "accessible":true,
//                        "used":true
//                    }
//                    ],
//                    "peer":{
//                        "peerId":"0.0.0.0",
//                        "routerId":"200.9.0.4"
//                    }
//                }
//                ]
//            },
//            "10.10.10.0\/24": {
//                "prefix":"10.10.10.0\/24",
//                "advertisedTo":{
//                    "10.10.10.1":{
//                    }
//                },
//                "paths":[
//                {
//                    "aspath":{
//                        "string":"Local",
//                        "segments":[
//                        ],
//                        "length":0
//                    },
//                    "origin":"incomplete",
//                    "med":0,
//                    "metric":0,
//                    "weight":32768,
//                    "valid":true,
//                    "sourced":true,
//                    "bestpath":{
//                        "overall":true
//                    },
//                    "lastUpdate":{
//                        "epoch":1494011680,
//                        "string":"Fri May  5 19:14:40 2017\n"
//                    },
//                    "nexthops":[
//                    {
//                        "ip":"0.0.0.0",
//                        "afi":"ipv4",
//                        "metric":0,
//                        "accessible":true,
//                        "used":true
//                    }
//                    ],
//                    "peer":{
//                        "peerId":"0.0.0.0",
//                        "routerId":"200.9.0.4"
//                    }
//                }
//                ]
//            },
//            "10.59.128.0\/20": {
//                "prefix":"10.59.128.0\/20",
//                "advertisedTo":{
//                    "10.10.10.1":{
//                    }
//                },
//                "paths":[
//                {
//                    "aspath":{
//                        "string":"Local",
//                        "segments":[
//                        ],
//                        "length":0
//                    },
//                    "origin":"incomplete",
//                    "med":0,
//                    "metric":0,
//                    "weight":32768,
//                    "valid":true,
//                    "sourced":true,
//                    "bestpath":{
//                        "overall":true
//                    },
//                    "lastUpdate":{
//                        "epoch":1494011680,
//                        "string":"Fri May  5 19:14:40 2017\n"
//                    },
//                    "nexthops":[
//                    {
//                        "ip":"0.0.0.0",
//                        "afi":"ipv4",
//                        "metric":0,
//                        "accessible":true,
//                        "used":true
//                    }
//                    ],
//                    "peer":{
//                        "peerId":"0.0.0.0",
//                        "routerId":"200.9.0.4"
//                    }
//                }
//                ]
//            },
//            "69.10.20.0\/24": {
//                "prefix":"69.10.20.0\/24",
//                "advertisedTo":{
//                    "10.10.10.1":{
//                    }
//                },
//                "paths":[
//                {
//                    "aspath":{
//                        "string":"200 {100,300,500}",
//                        "segments":[
//                        {
//                            "type":"as-sequence",
//                            "list":[
//                                200
//                            ]
//                        },
//                        {
//                            "type":"as-set",
//                            "list":[
//                                100,
//                            300,
//                            500
//                            ]
//                        }
//                        ],
//                        "length":2
//                    },
//                    "origin":"IGP",
//                    "valid":true,
//                    "bestpath":{
//                        "overall":true
//                    },
//                    "community":{
//                        "string":"500:700",
//                        "list":[
//                            "500:700"
//                        ]
//                    },
//                    "lastUpdate":{
//                        "epoch":1494011770,
//                        "string":"Fri May  5 19:16:10 2017\n"
//                    },
//                    "nexthops":[
//                    {
//                        "ip":"10.10.10.1",
//                        "afi":"ipv4",
//                        "metric":0,
//                        "accessible":true,
//                        "used":true
//                    }
//                    ],
//                    "peer":{
//                        "peerId":"10.10.10.1",
//                        "routerId":"25.98.0.1",
//                        "type":"external"
//                    }
//                }
//                ]
//            },
//            "69.10.21.0\/24": {
//                "prefix":"69.10.21.0\/24",
//                "advertisedTo":{
//                    "10.10.10.1":{
//                    }
//                },
//                "paths":[
//                {
//                    "aspath":{
//                        "string":"200 {100,300,500}",
//                        "segments":[
//                        {
//                            "type":"as-sequence",
//                            "list":[
//                                200
//                        ]
//                        },
//                        {
//                            "type":"as-set",
//                            "list":[
//                                100,
//                            300,
//                            500
//                            ]
//                        }
//                ],
//                "length":2
//                    },
//                    "origin":"IGP",
//                    "valid":true,
//                    "bestpath":{
//                        "overall":true
//                    },
//                    "community":{
//                        "string":"500:700",
//                        "list":[
//                            "500:700"
//                        ]
//                    },
//                    "lastUpdate":{
//                        "epoch":1494011770,
//                        "string":"Fri May  5 19:16:10 2017\n"
//                    },
//                    "nexthops":[
//                    {
//                        "ip":"10.10.10.1",
//                        "afi":"ipv4",
//                        "metric":0,
//                        "accessible":true,
//                        "used":true
//                    }
//                    ],
//                    "peer":{
//                        "peerId":"10.10.10.1",
//                        "routerId":"25.98.0.1",
//                        "type":"external"
//                    }
//                }
//                ]
//            },
//            "69.10.22.0\/24": {
//                "prefix":"69.10.22.0\/24",
//                "advertisedTo":{
//                    "10.10.10.1":{
//                    }
//                },
//                "paths":[
//                {
//                    "aspath":{
//                        "string":"200 {100,300,500}",
//                        "segments":[
//                        {
//                            "type":"as-sequence",
//                            "list":[
//                                200
//                            ]
//                        },
//                        {
//                            "type":"as-set",
//                            "list":[
//                                100,
//                            300,
//                            500
//                            ]
//                        }
//                        ],
//                        "length":2
//                    },
//                    "origin":"IGP",
//                    "valid":true,
//                    "bestpath":{
//                        "overall":true
//                    },
//                    "community":{
//                        "string":"500:700",
//                        "list":[
//                            "500:700"
//                        ]
//                    },
//                    "lastUpdate":{
//                        "epoch":1494011770,
//                        "string":"Fri May  5 19:16:10 2017\n"
//                    },
//                    "nexthops":[
//                    {
//                        "ip":"10.10.10.1",
//                        "afi":"ipv4",
//                        "metric":0,
//                        "accessible":true,
//                        "used":true
//                    }
//                    ],
//                    "peer":{
//                        "peerId":"10.10.10.1",
//                        "routerId":"25.98.0.1",
//                        "type":"external"
//                    }
//                }
//                ]
//            },
//            "69.10.23.0\/24": {
//                "prefix":"69.10.23.0\/24",
//                "advertisedTo":{
//                    "10.10.10.1":{
//                    }
//                },
//                "paths":[
//                {
//                    "aspath":{
//                        "string":"200 {100,300,500}",
//                        "segments":[
//                        {
//                            "type":"as-sequence",
//                            "list":[
//                                200
//                            ]
//                        },
//                        {
//                            "type":"as-set",
//                            "list":[
//                                100,
//                            300,
//                            500
//                            ]
//                        }
//                        ],
//                        "length":2
//                    },
//                    "origin":"IGP",
//                    "valid":true,
//                    "bestpath":{
//                        "overall":true
//                    },
//                    "community":{
//                        "string":"500:700",
//                        "list":[
//                            "500:700"
//                        ]
//                    },
//                    "lastUpdate":{
//                        "epoch":1494011770,
//                        "string":"Fri May  5 19:16:10 2017\n"
//                    },
//                    "nexthops":[
//                    {
//                        "ip":"10.10.10.1",
//                        "afi":"ipv4",
//                        "metric":0,
//                        "accessible":true,
//                        "used":true
//                    }
//                    ],
//                    "peer":{
//                        "peerId":"10.10.10.1",
//                        "routerId":"25.98.0.1",
//                        "type":"external"
//                    }
//                }
//                ]
//            },
//            "69.10.24.0\/24": {
//                "prefix":"69.10.24.0\/24",
//                "advertisedTo":{
//                    "10.10.10.1":{
//                    }
//                },
//                "paths":[
//                {
//                    "aspath":{
//                        "string":"200 {100,300,500}",
//                        "segments":[
//                        {
//                            "type":"as-sequence",
//                            "list":[
//                                200
//                            ]
//                        },
//                        {
//                            "type":"as-set",
//                            "list":[
//                                100,
//                            300,
//                            500
//                            ]
//                        }
//                        ],
//                        "length":2
//                    },
//                    "origin":"IGP",
//                    "valid":true,
//                    "bestpath":{
//                        "overall":true
//                    },
//                    "community":{
//                        "string":"500:700",
//                        "list":[
//                            "500:700"
//                        ]
//                    },
//                    "lastUpdate":{
//                        "epoch":1494011770,
//                        "string":"Fri May  5 19:16:10 2017\n"
//                    },
//                    "nexthops":[
//                    {
//                        "ip":"10.10.10.1",
//                        "afi":"ipv4",
//                        "metric":0,
//                        "accessible":true,
//                        "used":true
//                    }
//                    ],
//                    "peer":{
//                        "peerId":"10.10.10.1",
//                        "routerId":"25.98.0.1",
//                        "type":"external"
//                    }
//                }
//                ]
//            },
//            "69.10.25.0\/24": {
//                "prefix":"69.10.25.0\/24",
//                "advertisedTo":{
//                    "10.10.10.1":{
//                    }
//                },
//                "paths":[
//                {
//                    "aspath":{
//                        "string":"200 {100,300,500}",
//                        "segments":[
//                        {
//                            "type":"as-sequence",
//                            "list":[
//                                200
//                            ]
//                        },
//                        {
//                            "type":"as-set",
//                            "list":[
//                                100,
//                            300,
//                            500
//                            ]
//                        }
//                        ],
//                        "length":2
//                    },
//                    "origin":"IGP",
//                    "valid":true,
//                    "bestpath":{
//                        "overall":true
//                    },
//                    "community":{
//                        "string":"500:700",
//                        "list":[
//                            "500:700"
//                        ]
//                    },
//                    "lastUpdate":{
//                        "epoch":1494011770,
//                        "string":"Fri May  5 19:16:10 2017\n"
//                    },
//                    "nexthops":[
//                    {
//                        "ip":"10.10.10.1",
//                        "afi":"ipv4",
//                        "metric":0,
//                        "accessible":true,
//                        "used":true
//                    }
//                    ],
//                    "peer":{
//                        "peerId":"10.10.10.1",
//                        "routerId":"25.98.0.1",
//                        "type":"external"
//                    }
//                }
//                ]
//            },
//            "69.10.26.0\/24": {
//                "prefix":"69.10.26.0\/24",
//                "advertisedTo":{
//                    "10.10.10.1":{
//                    }
//                },
//                "paths":[
//                {
//                    "aspath":{
//                        "string":"200 {100,300,500}",
//                        "segments":[
//                        {
//                            "type":"as-sequence",
//                            "list":[
//                                200
//                            ]
//                        },
//                        {
//                            "type":"as-set",
//                            "list":[
//                                100,
//                            300,
//                            500
//                            ]
//                        }
//                        ],
//                        "length":2
//                    },
//                    "origin":"IGP",
//                    "valid":true,
//                    "bestpath":{
//                        "overall":true
//                    },
//                    "community":{
//                        "string":"500:700",
//                        "list":[
//                            "500:700"
//                        ]
//                    },
//                    "lastUpdate":{
//                        "epoch":1494011770,
//                        "string":"Fri May  5 19:16:10 2017\n"
//                    },
//                    "nexthops":[
//                    {
//                        "ip":"10.10.10.1",
//                        "afi":"ipv4",
//                        "metric":0,
//                        "accessible":true,
//                        "used":true
//                    }
//                    ],
//                    "peer":{
//                        "peerId":"10.10.10.1",
//                        "routerId":"25.98.0.1",
//                        "type":"external"
//                    }
//                }
//                ]
//            },
//            "69.10.27.0\/24": {
//                "prefix":"69.10.27.0\/24",
//                "advertisedTo":{
//                    "10.10.10.1":{
//                    }
//                },
//                "paths":[
//                {
//                    "aspath":{
//                        "string":"200 {100,300,500}",
//                        "segments":[
//                        {
//                            "type":"as-sequence",
//                            "list":[
//                                200
//                            ]
//                        },
//                        {
//                            "type":"as-set",
//                            "list":[
//                                100,
//                            300,
//                            500
//                            ]
//                        }
//                        ],
//                        "length":2
//                    },
//                    "origin":"IGP",
//                    "valid":true,
//                    "bestpath":{
//                        "overall":true
//                    },
//                    "community":{
//                        "string":"500:700",
//                        "list":[
//                            "500:700"
//                        ]
//                    },
//                    "lastUpdate":{
//                        "epoch":1494011770,
//                        "string":"Fri May  5 19:16:10 2017\n"
//                    },
//                    "nexthops":[
//                    {
//                        "ip":"10.10.10.1",
//                        "afi":"ipv4",
//                        "metric":0,
//                        "accessible":true,
//                        "used":true
//                    }
//                    ],
//                    "peer":{
//                        "peerId":"10.10.10.1",
//                        "routerId":"25.98.0.1",
//                        "type":"external"
//                    }
//                }
//                ]
//            },
//            "69.10.28.0\/24": {
//                "prefix":"69.10.28.0\/24",
//                "advertisedTo":{
//                    "10.10.10.1":{
//                    }
//                },
//                "paths":[
//                {
//                    "aspath":{
//                        "string":"200 {100,300,500}",
//                        "segments":[
//                        {
//                            "type":"as-sequence",
//                            "list":[
//                                200
//                            ]
//                        },
//                        {
//                            "type":"as-set",
//                            "list":[
//                                100,
//                            300,
//                            500
//                            ]
//                        }
//                        ],
//                        "length":2
//                    },
//                    "origin":"IGP",
//                    "valid":true,
//                    "bestpath":{
//                        "overall":true
//                    },
//                    "community":{
//                        "string":"500:700",
//                        "list":[
//                            "500:700"
//                        ]
//                    },
//                    "lastUpdate":{
//                        "epoch":1494011770,
//                        "string":"Fri May  5 19:16:10 2017\n"
//                    },
//                    "nexthops":[
//                    {
//                        "ip":"10.10.10.1",
//                        "afi":"ipv4",
//                        "metric":0,
//                        "accessible":true,
//                        "used":true
//                    }
//                    ],
//                    "peer":{
//                        "peerId":"10.10.10.1",
//                        "routerId":"25.98.0.1",
//                        "type":"external"
//                    }
//                }
//                ]
//            },
//            "69.10.29.0\/24": {
//                "prefix":"69.10.29.0\/24",
//                "advertisedTo":{
//                    "10.10.10.1":{
//                    }
//                },
//                "paths":[
//                {
//                    "aspath":{
//                        "string":"200 {100,300,500}",
//                        "segments":[
//                        {
//                            "type":"as-sequence",
//                            "list":[
//                                200
//                            ]
//                        },
//                        {
//                            "type":"as-set",
//                            "list":[
//                                100,
//                            300,
//                            500
//                            ]
//                        }
//                        ],
//                        "length":2
//                    },
//                    "origin":"IGP",
//                    "valid":true,
//                    "bestpath":{
//                        "overall":true
//                    },
//                    "community":{
//                        "string":"500:700",
//                        "list":[
//                            "500:700"
//                        ]
//                    },
//                    "lastUpdate":{
//                        "epoch":1494011770,
//                        "string":"Fri May  5 19:16:10 2017\n"
//                    },
//                    "nexthops":[
//                    {
//                        "ip":"10.10.10.1",
//                        "afi":"ipv4",
//                        "metric":0,
//                        "accessible":true,
//                        "used":true
//                    }
//                    ],
//                    "peer":{
//                        "peerId":"10.10.10.1",
//                        "routerId":"25.98.0.1",
//                        "type":"external"
//                    }
//                }
//                ]
//            },
//            "69.10.30.0\/24": {
//                "prefix":"69.10.30.0\/24",
//                "advertisedTo":{
//                    "10.10.10.1":{
//                    }
//                },
//                "paths":[
//                {
//                    "aspath":{
//                        "string":"200 {100,300,500}",
//                        "segments":[
//                        {
//                            "type":"as-sequence",
//                            "list":[
//                                200
//                            ]
//                        },
//                        {
//                            "type":"as-set",
//                            "list":[
//                                100,
//                            300,
//                            500
//                            ]
//                        }
//                        ],
//                        "length":2
//                    },
//                    "origin":"IGP",
//                    "valid":true,
//                    "bestpath":{
//                        "overall":true
//                    },
//                    "community":{
//                        "string":"500:700",
//                        "list":[
//                            "500:700"
//                        ]
//                    },
//                    "lastUpdate":{
//                        "epoch":1494011770,
//                        "string":"Fri May  5 19:16:10 2017\n"
//                    },
//                    "nexthops":[
//                    {
//                        "ip":"10.10.10.1",
//                        "afi":"ipv4",
//                        "metric":0,
//                        "accessible":true,
//                        "used":true
//                    }
//                    ],
//                    "peer":{
//                        "peerId":"10.10.10.1",
//                        "routerId":"25.98.0.1",
//                        "type":"external"
//                    }
//                }
//                ]
//            },
//            "69.10.31.0\/24": {
//                "prefix":"69.10.31.0\/24",
//                "advertisedTo":{
//                    "10.10.10.1":{
//                    }
//                },
//                "paths":[
//                {
//                    "aspath":{
//                        "string":"200 {100,300,500}",
//                        "segments":[
//                        {
//                            "type":"as-sequence",
//                            "list":[
//                                200
//                            ]
//                        },
//                        {
//                            "type":"as-set",
//                            "list":[
//                                100,
//                            300,
//                            500
//                            ]
//                        }
//                        ],
//                        "length":2
//                    },
//                    "origin":"IGP",
//                    "valid":true,
//                    "bestpath":{
//                        "overall":true
//                    },
//                    "community":{
//                        "string":"500:700",
//                        "list":[
//                            "500:700"
//                        ]
//                    },
//                    "lastUpdate":{
//                        "epoch":1494011770,
//                        "string":"Fri May  5 19:16:10 2017\n"
//                    },
//                    "nexthops":[
//                    {
//                        "ip":"10.10.10.1",
//                        "afi":"ipv4",
//                        "metric":0,
//                        "accessible":true,
//                        "used":true
//                    }
//                    ],
//                    "peer":{
//                        "peerId":"10.10.10.1",
//                        "routerId":"25.98.0.1",
//                        "type":"external"
//                    }
//                }
//                ]
//            },
//            "69.10.32.0\/24": {
//                "prefix":"69.10.32.0\/24",
//                "advertisedTo":{
//                    "10.10.10.1":{
//                    }
//                },
//                "paths":[
//                {
//                    "aspath":{
//                        "string":"200 {100,300,500}",
//                        "segments":[
//                        {
//                            "type":"as-sequence",
//                            "list":[
//                                200
//                            ]
//                        },
//                        {
//                            "type":"as-set",
//                            "list":[
//                                100,
//                            300,
//                            500
//                            ]
//                        }
//                        ],
//                        "length":2
//                    },
//                    "origin":"IGP",
//                    "valid":true,
//                    "bestpath":{
//                        "overall":true
//                    },
//                    "community":{
//                        "string":"500:700",
//                        "list":[
//                            "500:700"
//                        ]
//                    },
//                    "lastUpdate":{
//                        "epoch":1494011770,
//                        "string":"Fri May  5 19:16:10 2017\n"
//                    },
//                    "nexthops":[
//                    {
//                        "ip":"10.10.10.1",
//                        "afi":"ipv4",
//                        "metric":0,
//                        "accessible":true,
//                        "used":true
//                    }
//                    ],
//                    "peer":{
//                        "peerId":"10.10.10.1",
//                        "routerId":"25.98.0.1",
//                        "type":"external"
//                    }
//                }
//                ]
//            },
//            "69.10.33.0\/24": {
//                "prefix":"69.10.33.0\/24",
//                "advertisedTo":{
//                    "10.10.10.1":{
//                    }
//                },
//                "paths":[
//                {
//                    "aspath":{
//                        "string":"200 {100,300,500}",
//                        "segments":[
//                        {
//                            "type":"as-sequence",
//                            "list":[
//                                200
//                            ]
//                        },
//                        {
//                            "type":"as-set",
//                            "list":[
//                                100,
//                            300,
//                            500
//                            ]
//                        }
//                        ],
//                        "length":2
//                    },
//                    "origin":"IGP",
//                    "valid":true,
//                    "bestpath":{
//                        "overall":true
//                    },
//                    "community":{
//                        "string":"500:700",
//                        "list":[
//                            "500:700"
//                        ]
//                    },
//                    "lastUpdate":{
//                        "epoch":1494011770,
//                        "string":"Fri May  5 19:16:10 2017\n"
//                    },
//                    "nexthops":[
//                    {
//                        "ip":"10.10.10.1",
//                        "afi":"ipv4",
//                        "metric":0,
//                        "accessible":true,
//                        "used":true
//                    }
//                    ],
//                    "peer":{
//                        "peerId":"10.10.10.1",
//                        "routerId":"25.98.0.1",
//                        "type":"external"
//                    }
//                }
//                ]
//            },
//            "69.10.34.0\/24": {
//                "prefix":"69.10.34.0\/24",
//                "advertisedTo":{
//                    "10.10.10.1":{
//                    }
//                },
//                "paths":[
//                {
//                    "aspath":{
//                        "string":"200 {100,300,500}",
//                        "segments":[
//                        {
//                            "type":"as-sequence",
//                            "list":[
//                                200
//                            ]
//                        },
//                        {
//                            "type":"as-set",
//                            "list":[
//                                100,
//                            300,
//                            500
//                            ]
//                        }
//                        ],
//                        "length":2
//                    },
//                    "origin":"IGP",
//                    "valid":true,
//                    "bestpath":{
//                        "overall":true
//                    },
//                    "community":{
//                        "string":"500:700",
//                        "list":[
//                            "500:700"
//                        ]
//                    },
//                    "lastUpdate":{
//                        "epoch":1494011770,
//                        "string":"Fri May  5 19:16:10 2017\n"
//                    },
//                    "nexthops":[
//                    {
//                        "ip":"10.10.10.1",
//                        "afi":"ipv4",
//                        "metric":0,
//                        "accessible":true,
//                        "used":true
//                    }
//                    ],
//                    "peer":{
//                        "peerId":"10.10.10.1",
//                        "routerId":"25.98.0.1",
//                        "type":"external"
//                    }
//                }
//                ]
//            },
//            "69.10.35.0\/24": {
//                "prefix":"69.10.35.0\/24",
//                "advertisedTo":{
//                    "10.10.10.1":{
//                    }
//                },
//                "paths":[
//                {
//                    "aspath":{
//                        "string":"200 {100,300,500}",
//                        "segments":[
//                        {
//                            "type":"as-sequence",
//                            "list":[
//                                200
//                            ]
//                        },
//                        {
//                            "type":"as-set",
//                            "list":[
//                                100,
//                            300,
//                            500
//                            ]
//                        }
//                        ],
//                        "length":2
//                    },
//                    "origin":"IGP",
//                    "valid":true,
//                    "bestpath":{
//                        "overall":true
//                    },
//                    "community":{
//                        "string":"500:700",
//                        "list":[
//                            "500:700"
//                        ]
//                    },
//                    "lastUpdate":{
//                        "epoch":1494011770,
//                        "string":"Fri May  5 19:16:10 2017\n"
//                    },
//                    "nexthops":[
//                    {
//                        "ip":"10.10.10.1",
//                        "afi":"ipv4",
//                        "metric":0,
//                        "accessible":true,
//                        "used":true
//                    }
//                    ],
//                    "peer":{
//                        "peerId":"10.10.10.1",
//                        "routerId":"25.98.0.1",
//                        "type":"external"
//                    }
//                }
//                ]
//            }
//        }
//    }`

    outJsonBlob := `{
        "vrfId": 0,
        "vrfName": "default",
        "tableVersion": 54,
        "routerId": "200.9.0.4",
        "defaultLocPrf": 100,
        "localAS": 400,
        "routes": {
            "4.4.4.4\/32": {
                "prefix":"4.4.4.4\/32",
                "advertisedTo":{
                    "10.10.10.1":{
                    }
                },
                "paths":{
                    "1" : {
                        "aspath":{
                            "string":"Local",
                            "segments":[
                            ],
                            "length":0
                        },
                        "origin":"incomplete",
                        "med":0,
                        "metric":0,
                        "weight":32768,
                        "valid":true,
                        "sourced":true,
                        "bestpath":{
                            "overall":true
                        },
                        "lastUpdate":{
                            "epoch":1494011680,
                            "string":"Fri May  5 19:14:40 2017\n"
                        },
                        "nexthops":[
                        {
                            "ip":"0.0.0.0",
                            "afi":"ipv4",
                            "metric":0,
                            "accessible":true,
                            "used":true
                        }
                        ],
                        "peer":{
                            "peerId":"0.0.0.0",
                            "routerId":"200.9.0.4"
                        }
                    },
                    "2" : {
                        "aspath":{
                            "string":"200 {100,300,500}",
                            "segments":[
                            {
                                "type":"as-sequence",
                                "list":[
                                    200
                                ]
                            },
                            {
                                "type":"as-set",
                                "list":[
                                    100,
                                300,
                                500
                                ]
                            }
                            ],
                            "length":2
                        },
                        "origin":"IGP",
                        "valid":true,
                        "bestpath":{
                            "overall":true
                        },
                        "community":{
                            "string":"500:700",
                            "list":[
                                "500:700"
                            ]
                        },
                        "lastUpdate":{
                            "epoch":1494011770,
                            "string":"Fri May  5 19:16:10 2017\n"
                        },
                        "nexthops":[
                        {
                            "ip":"10.10.10.1",
                            "afi":"ipv4",
                            "metric":0,
                            "accessible":true,
                            "used":true
                        }
                        ],
                        "peer":{
                            "peerId":"10.10.10.1",
                            "routerId":"25.98.0.1",
                            "type":"external"
                        }
                    }
                }
            },
            "69.10.30.0\/24": {
                "prefix":"69.10.30.0\/24",
                "advertisedTo":{
                    "10.10.10.1":{
                    }
                },
                "paths":{
                    "1" : {
                        "aspath":{
                            "string":"200 {100,300,500}",
                            "segments":[
                            {
                                "type":"as-sequence",
                                "list":[
                                    200
                                ]
                            },
                            {
                                "type":"as-set",
                                "list":[
                                    100,
                                300,
                                500
                                ]
                            }
                            ],
                            "length":2
                        },
                        "origin":"IGP",
                        "valid":true,
                        "bestpath":{
                            "overall":true
                        },
                        "community":{
                            "string":"500:700",
                            "list":[
                                "500:700"
                            ]
                        },
                        "lastUpdate":{
                            "epoch":1494011770,
                            "string":"Fri May  5 19:16:10 2017\n"
                        },
                        "nexthops":[
                        {
                            "ip":"10.10.10.1",
                            "afi":"ipv4",
                            "metric":0,
                            "accessible":true,
                            "used":true
                        }
                        ],
                        "peer":{
                            "peerId":"10.10.10.2",
                            "routerId":"25.98.0.1",
                            "type":"external"
                        }
                    }
                }
            }
        }
    }`

    if err = json.Unmarshal([]byte(outJsonBlob), &outputJson) ; err != nil {
        return nil, err
    }

    return outputJson, err
}

func fake_rib_nbrs_in_post_exec_vtysh_cmd (vtysh_cmd string) (map[string]interface{}, error) {
    var err error
    var outputJson map[string]interface{}

    outJsonBlob := `{
	"vrfId": 0,
	"vrfName": "default",
	"tableVersion": 54,
	"routerId": "200.9.0.4",
	"defaultLocPrf": 100,
	"localAS": 400,
	"routes": {
	    "4.4.4.4\/32": {
		"prefix":"4.4.4.4\/32",
		"advertisedTo":{
		    "10.10.10.1":{
		    }
		},
		"paths": [
		 {
                        "pathId":0,
			"aspath":{                                           
			    "string":"100 {300,400,1600,1700}",                
			    "segments":[                                       
			    {                                                
				"type":"as-sequence",                          
				"list":[                                       
			 	  100                                          
				]                                              
			    },                                               
			    {                                                
				"type":"as-set",                               
				"list":[                                       
                                    300,                                         
				    400,                                         
			   	    1600,                                        
			     	    1700                                         
				]                                              
			    }                                                
			    ],                                                 
			    "length":2                                         
			},

			"as4path":{                                           
			    "string":"100000 {300000,170000}",                
			    "segments":[                                       
			    {                                                
				"type":"as-sequence",                          
				"list":[                                       
		  		100000                                         
				]                                              
			    },                                               
			    {                                                
				"type":"as-set",                               
				"list":[                                       
				300000,                                                                                 
				170000                                         
				]                                              
			    }                                                
			    ],                                                 
			    "length":2                                         
			},  
			"origin":"incomplete",  
			"localPref":200,
			"originatorId":"1.1.1.1",
			"med":0,
			"metric":0,
			"weight":32768,
			"aggregatorAs":600,
			"aggregatorAs4":75535,                                            
			"aggregatorId":"10.20.30.40",                                
			"atomicAggregate":true,
			"valid":true,
			"sourced":true,
			"bestpath":{
			    "overall":false
			},
			"lastUpdate":{
			    "epoch":1494011680,
			    "string":"Fri May  5 19:14:40 2017\n"
			},

			"nexthops":[
			{
			    "ip":"2.2.2.2",
			    "afi":"ipv4",
			    "metric":0,
			    "accessible":true,
			    "used":true
			}
			],

			"peer":{                        
			    "peerId":"10.10.10.1",                             
			    "routerId":"210.135.0.1",                          
			    "type":"external"
			}, 

			"cluster":{
                          "list":[                                       
			    "1.1.1.1",                                                                                 
		            "2.2.2.2"                                         
			   ]
                        },

			"community":{                                                 
			    "string":"local-AS 800:900 1000:2000",                               
			    "list":[
 		               "local-AS",                                                    
			       "800:900",                                                
			       "1000:2000"                                               
			    ]                                                           
			},

			"extendedCommunity":{                                         
			    "string":"RT:2000:168496141 RO:2000:168496141", 
			    "list":[                                                    
			        "RT:2000:168496141",                                                
			        "RO:2000:168496141"                                               
			    ]                                     
			}                                                                                 
		    },
		    { 
                        "pathId":1,
			"aspath":{                                           
			    "string":"100 {300,400,1600,1700}",                
			    "segments":[                                       
			    {                                                
				"type":"as-sequence",                          
				"list":[                                       
			 	  100                                          
				]                                              
			    },                                               
			    {                                                
				"type":"as-set",                               
				"list":[                                       
                                    300,                                         
				    400,                                         
			   	    1600,                                        
			     	    1700                                         
				]                                              
			    }                                                
			    ],                                                 
			    "length":2                                         
			},

			"as4path":{                                           
			    "string":"100000 {300000,170000}",                
			    "segments":[                                       
			    {                                                
				"type":"as-sequence",                          
				"list":[                                       
		  		100000                                         
				]                                              
			    },                                               
			    {                                                
				"type":"as-set",                               
				"list":[                                       
				300000,                                                                                 
				170000                                         
				]                                              
			    }                                                
			    ],                                                 
			    "length":2                                         
			},  
			"origin":"incomplete",  
			"localPref":200,
			"originatorId":"3.3.3.3",
			"med":1,
			"metric":1,
			"weight":32768,
			"aggregatorAs":600,
			"aggregatorAs4":75535,                                            
			"aggregatorId":"10.20.30.40",                                
			"atomicAggregate":true,
			"valid":false,
			"sourced":false,
			"bestpath":{
			    "overall":false
			},
			"lastUpdate":{
			    "epoch":1494011680,
			    "string":"Fri May  5 19:14:40 2017\n"
			},

			"nexthops":[
			{
			    "ip":"3.3.3.3",
			    "afi":"ipv4",
			    "metric":0,
			    "accessible":true,
			    "used":true
			}
			],

			"peer":{                        
			    "peerId":"10.10.10.1",                             
			    "routerId":"210.135.0.1",                          
			    "type":"external"
			}, 

			"cluster":{
                          "list":[                                       
			    "3.3.3.3",                                                                                 
		            "4.4.4.4"                                         
			   ]
                        },

			"community":{                                                 
			    "string":"no-peer 800:900 1000:2000",                               
			    "list":[
 		               "no-peer",                                                    
			       "800:900",                                                
			       "1000:2000"                                               
			    ]                                                           
			},

			"extendedCommunity":{                                         
			    "string":"RT:3000:168496141 RO:4000:168496141", 
			    "list":[                                                    
			        "RT:3000:168496141",                                                
			        "RO:4000:168496141"                                               
			    ]                                     
			}                                                                                 
		    }
                   ] 
		},
            "5.5.5.5\/32": {
		"prefix":"5.5.5.5\/32",
		"advertisedTo":{
		    "10.10.10.1":{
		    }
		},
		"paths":[
		    {
                        "pathId":0,
			"aspath":{                                           
			    "string":"100 {300,400,1600,1700}",                
			    "segments":[                                       
			    {                                                
				"type":"as-sequence",                          
				"list":[                                       
			 	  100                                          
				]                                              
			    },                                               
			    {                                                
				"type":"as-set",                               
				"list":[                                       
                                    300,                                         
				    400,                                         
			   	    1600,                                        
			     	    1700                                         
				]                                              
			    }                                                
			    ],                                                 
			    "length":2                                         
			},

			"as4path":{                                           
			    "string":"100000 {300000,170000}",                
			    "segments":[                                       
			    {                                                
				"type":"as-sequence",                          
				"list":[                                       
		  		100000                                         
				]                                              
			    },                                               
			    {                                                
				"type":"as-set",                               
				"list":[                                       
				300000,                                                                                 
				170000                                         
				]                                              
			    }                                                
			    ],                                                 
			    "length":2                                         
			},  
			"origin":"incomplete",  
			"localPref":200,
			"originatorId":"1.1.1.1",
			"med":0,
			"metric":0,
			"weight":32768,
			"aggregatorAs":600,
			"aggregatorAs4":75535,                                            
			"aggregatorId":"10.20.30.40",                                
			"atomicAggregate":true,
			"valid":true,
			"sourced":true,
			"bestpath":{
			    "overall":false
			},
			"lastUpdate":{
			    "epoch":1494011680,
			    "string":"Fri May  5 19:14:40 2017\n"
			},

			"nexthops":[
			{
			    "ip":"2.2.2.2",
			    "afi":"ipv4",
			    "metric":0,
			    "accessible":true,
			    "used":true
			}
			],

			"peer":{                        
			    "peerId":"10.10.10.1",                             
			    "routerId":"210.135.0.1",                          
			    "type":"external"
			}, 

			"cluster":{
                          "list":[                                       
			    "1.1.1.1",                                                                                 
		            "2.2.2.2"                                         
			   ]
                        },

			"community":{                                                 
			    "string":"local-AS 800:900 1000:2000",                               
			    "list":[
 		               "local-AS",                                                    
			       "800:900",                                                
			       "1000:2000"                                               
			    ]                                                           
			},

			"extendedCommunity":{                                         
			    "string":"RT:2000:168496141 RO:2000:168496141", 
			    "list":[                                                    
			        "RT:2000:168496141",                                                
			        "RO:2000:168496141"                                               
			    ]                                     
			}                                                                                 
		    }
		]
	    }
        }    
    }`

    if err = json.Unmarshal([]byte(outJsonBlob), &outputJson) ; err != nil {
        return nil, err
    }

    return outputJson, err
}

func fake_rib_nbrs_in_pre_exec_vtysh_cmd (vtysh_cmd string) (map[string]interface{}, error) {
    var err error
    var outputJson map[string]interface{}

    outJsonBlob := `{
	"vrfId": 0,
	"vrfName": "default",
	"bgpTableVersion":20,                                             
	"bgpLocalRouterId":"30.30.30.1",                                  
	"defaultLocPrf":100,             						                              
	"localAS":200,
	"routes": {
	    "6.6.6.6\/32": {
		"prefix":"6.6.6.6\/32",
		"paths":{
		    "1" : {     
			"weight":0,
			"bgpOriginCode":"i", 
			"origin":"IGP",                                                     
			"aggregatorAs":600,                                           
			"aggregatorId":"10.20.30.40",                                
			"atomicAggregate":true,
			"med":0,
			"metric":0,                                                   
			"aspath":{                                           
			    "string":"100 {300,400,1600,1700}",                
			    "segments":[                                       
			    {                                                
				"type":"as-sequence",                          
				"list":[                                       
				100                                          
				]                                              
			    },                                               
			    {                                                
				"type":"as-set",                               
				"list":[                                       
				300,                                         
				400,                                         
				1600,                                        
				1700                                         
				]                                              
			    }                                                
			    ],                                                 
			    "length":2                                         
			},           
 			"as4path":{                                           
			    "string":"1000000 {3000000,4000000}",                
			    "segments":[                                       
			    {                                                
				"type":"as-sequence",                          
				"list":[                                       
				  1000000                                          
				]                                              
			    },                                               
			    {                                                
				"type":"as-set",                               
				"list":[                                       
				   3000000,                                         
			           4000000                                         
				]                                              
			    }                                                
			    ],                                                 
			    "length":2                                         
			},

			"community":{                                                 
			    "string":"local-AS, 800:900 1000:2000",                               
			    "list":[
		 	    "local-AS",                                                    
			    "800:900",                                                
			    "1000:2000"                                               
			    ]                                                           
			},

			"extendedCommunity":{                                         
			    "string":"RT:2000:168496141 RO:2000:168496141", 
			    "list":[                                                    
			    "RT:2000:168496141",                                                
			    "RO:2000:168496141"                                               
			    ]                                     
			},                                                            

			"lastUpdate":{
			    "epoch":1494011770,
			    "string":"Fri May  5 19:16:10 2017\n"
			},

			"nextHop":"10.10.10.1",

			"valid":true,

			"bestpath":{
			    "overall":true
			}
		    }
		}
	    }     	                                                             
	},                                                                 
	"totalPrefixCounter":20,                                          
	"filteredPrefixCounter":0                                         
    }`

    if err = json.Unmarshal([]byte(outJsonBlob), &outputJson) ; err != nil {
        return nil, err
    }

    return outputJson, err
}

func init () {
    XlateFuncBind("YangToDb_bgp_gbl_tbl_key_xfmr", YangToDb_bgp_gbl_tbl_key_xfmr)
    XlateFuncBind("DbToYang_bgp_gbl_tbl_key_xfmr", DbToYang_bgp_gbl_tbl_key_xfmr)
    XlateFuncBind("YangToDb_bgp_gbl_afi_safi_field_xfmr", YangToDb_bgp_gbl_afi_safi_field_xfmr)
    XlateFuncBind("DbToYang_bgp_gbl_afi_safi_field_xfmr", DbToYang_bgp_gbl_afi_safi_field_xfmr)
	XlateFuncBind("YangToDb_bgp_dyn_neigh_listen_key_xfmr", YangToDb_bgp_dyn_neigh_listen_key_xfmr)
	XlateFuncBind("DbToYang_bgp_dyn_neigh_listen_key_xfmr", DbToYang_bgp_dyn_neigh_listen_key_xfmr) 
	XlateFuncBind("YangToDb_bgp_gbl_afi_safi_key_xfmr", YangToDb_bgp_gbl_afi_safi_key_xfmr)
	XlateFuncBind("DbToYang_bgp_gbl_afi_safi_key_xfmr", DbToYang_bgp_gbl_afi_safi_key_xfmr) 
	XlateFuncBind("YangToDb_bgp_dyn_neigh_listen_field_xfmr", YangToDb_bgp_dyn_neigh_listen_field_xfmr)
	XlateFuncBind("DbToYang_bgp_dyn_neigh_listen_field_xfmr", DbToYang_bgp_dyn_neigh_listen_field_xfmr) 
}

var YangToDb_bgp_gbl_afi_safi_field_xfmr FieldXfmrYangToDb = func(inParams XfmrParams) (map[string]string, error) {
    rmap := make(map[string]string)
    var err error

    log.Info("YangToDb_bgp_gbl_afi_safi_field_xfmr")
    rmap["NULL"] = "NULL"
    
    return rmap, err
}

var DbToYang_bgp_gbl_afi_safi_field_xfmr FieldXfmrDbtoYang = func(inParams XfmrParams) (map[string]interface{}, error) {
    rmap := make(map[string]interface{})
    var err error
    entry_key := inParams.key
    log.Info("DbToYang_bgp_gbl_afi_safi_field_xfmr: ", entry_key)

    mpathKey := strings.Split(entry_key, "|")
	afi := ""

	switch mpathKey[1] {
	case "ipv4_unicast":
		afi = "IPV4_UNICAST"
	case "ipv6_unicast":
		afi = "IPV6_UNICAST"
	case "l2vpn_evpn":
		afi = "L2VPN_EVPN"
	}

    rmap["afi-safi-name"] = afi

    return rmap, err
}

var YangToDb_bgp_dyn_neigh_listen_field_xfmr FieldXfmrYangToDb = func(inParams XfmrParams) (map[string]string, error) {
    rmap := make(map[string]string)
    var err error

    log.Info("YangToDb_bgp_dyn_neigh_listen_field_xfmr")
    rmap["NULL"] = "NULL"
    
    return rmap, err
}

var DbToYang_bgp_dyn_neigh_listen_field_xfmr FieldXfmrDbtoYang = func(inParams XfmrParams) (map[string]interface{}, error) {
    rmap := make(map[string]interface{})
    var err error
    
    entry_key := inParams.key
    log.Info("DbToYang_bgp_dyn_neigh_listen_key_xfmr: ", entry_key)

    dynKey := strings.Split(entry_key, "|")

    rmap["prefix"] = dynKey[1]

    return rmap, err
}

var YangToDb_bgp_gbl_tbl_key_xfmr KeyXfmrYangToDb = func(inParams XfmrParams) (string, error) {
    var err error

    pathInfo := NewPathInfo(inParams.uri)

    niName := pathInfo.Var("name")
    bgpId := pathInfo.Var("identifier")
    protoName := pathInfo.Var("name#2")

    if len(pathInfo.Vars) <  3 {
        return niName, errors.New("Invalid Key length")
    }

    if len(niName) == 0 {
        return niName, errors.New("vrf name is missing")
    }

    if strings.Contains(bgpId,"BGP") == false {
        return niName, errors.New("BGP ID is missing")
    }
    
    if len(protoName) == 0 {
        return niName, errors.New("Protocol Name is missing")
    }

    log.Info("URI VRF ", niName)

    return niName, err
}

var DbToYang_bgp_gbl_tbl_key_xfmr KeyXfmrDbToYang = func(inParams XfmrParams) (map[string]interface{}, error) {
    rmap := make(map[string]interface{})
    var err error
    entry_key := inParams.key
    log.Info("DbToYang_bgp_gbl_tbl_key: ", entry_key)

    rmap["name"] = entry_key
    return rmap, err
}

var YangToDb_bgp_dyn_neigh_listen_key_xfmr KeyXfmrYangToDb = func(inParams XfmrParams) (string, error) {
	log.Info("YangToDb_bgp_dyn_neigh_listen_key_xfmr key: ", inParams.uri)

    pathInfo := NewPathInfo(inParams.uri)

    niName := pathInfo.Var("name")
    bgpId := pathInfo.Var("identifier")
    protoName := pathInfo.Var("name#2")
	prefix := pathInfo.Var("prefix")

    if len(pathInfo.Vars) < 4 {
        return "", errors.New("Invalid Key length")
    }

    if len(niName) == 0 {
        return "", errors.New("vrf name is missing")
    }

    if strings.Contains(bgpId,"BGP") == false {
        return "", errors.New("BGP ID is missing")
    }
    
    if len(protoName) == 0 {
        return "", errors.New("Protocol Name is missing")
    }

	key := niName + "|" + prefix
	
	log.Info("YangToDb_bgp_dyn_neigh_listen_key_xfmr key: ", key)

    return key, nil
}

var DbToYang_bgp_dyn_neigh_listen_key_xfmr KeyXfmrDbToYang = func(inParams XfmrParams) (map[string]interface{}, error) {
    rmap := make(map[string]interface{})
    entry_key := inParams.key
    log.Info("DbToYang_bgp_dyn_neigh_listen_key_xfmr: ", entry_key)

    dynKey := strings.Split(entry_key, "|")

    rmap["prefix"] = dynKey[1]

	log.Info("DbToYang_bgp_dyn_neigh_listen_key_xfmr: rmap:", rmap)
    return rmap, nil
}

var YangToDb_bgp_gbl_afi_safi_key_xfmr KeyXfmrYangToDb = func(inParams XfmrParams) (string, error) {

    pathInfo := NewPathInfo(inParams.uri)

    niName := pathInfo.Var("name")
    bgpId := pathInfo.Var("identifier")
    protoName := pathInfo.Var("name#2")
	afName := pathInfo.Var("afi-safi-name")
	afi := ""
    var err error

    if len(pathInfo.Vars) < 4 {
        return afi, errors.New("Invalid Key length")
    }

    if len(niName) == 0 {
        return afi, errors.New("vrf name is missing")
    }

    if strings.Contains(bgpId,"BGP") == false {
        return afi, errors.New("BGP ID is missing")
    }
    
    if len(protoName) == 0 {
        return afi, errors.New("Protocol Name is missing")
    }

	if strings.Contains(afName, "IPV4_UNICAST") {
		afi = "ipv4_unicast"
	} else if strings.Contains(afName, "IPV6_UNICAST") {
		afi = "ipv6_unicast"
	} else if strings.Contains(afName, "L2VPN_EVPN") {
		afi = "l2vpn_evpn"
	} else {
		log.Info("Unsupported AFI type " + afName)
        return afi, errors.New("Unsupported AFI type " + afName)
	}

    if strings.Contains(afName, "IPV4_UNICAST") {
        afName = "IPV4_UNICAST"
        if strings.Contains(inParams.uri, "ipv6-unicast") ||
           strings.Contains(inParams.uri, "l2vpn-evpn") {
		    err = errors.New("IPV4_UNICAST supported only on ipv4-config container")
		    log.Info("IPV4_UNICAST supported only on ipv4-config container: ", afName);
		    return afName, err
        }
    } else if strings.Contains(afName, "IPV6_UNICAST") {
        afName = "IPV6_UNICAST"
        if strings.Contains(inParams.uri, "ipv4-unicast") ||
           strings.Contains(inParams.uri, "l2vpn-evpn") {
		    err = errors.New("IPV6_UNICAST supported only on ipv6-config container")
		    log.Info("IPV6_UNICAST supported only on ipv6-config container: ", afName);
		    return afName, err
        }
    } else if strings.Contains(afName, "L2VPN_EVPN") {
        afName = "L2VPN_EVPN"
        if strings.Contains(inParams.uri, "ipv6-unicast") ||
           strings.Contains(inParams.uri, "ipv4-unicast") {
		    err = errors.New("L2VPN_EVPN supported only on l2vpn-evpn container")
		    log.Info("L2VPN_EVPN supported only on l2vpn-evpn container: ", afName);
		    return afName, err
        }
    } else  {
	    err = errors.New("Unsupported AFI SAFI")
	    log.Info("Unsupported AFI SAFI ", afName);
	    return afName, err
    }

	key := niName + "|" + afi
	
	log.Info("AFI key: ", key)

    return key, nil
}

var DbToYang_bgp_gbl_afi_safi_key_xfmr KeyXfmrDbToYang = func(inParams XfmrParams) (map[string]interface{}, error) {
    rmap := make(map[string]interface{})
    entry_key := inParams.key
    log.Info("DbToYang_bgp_gbl_afi_safi_key_xfmr: ", entry_key)

    mpathKey := strings.Split(entry_key, "|")
	afi := ""

	switch mpathKey[1] {
	case "ipv4_unicast":
		afi = "IPV4_UNICAST"
	case "ipv6_unicast":
		afi = "IPV6_UNICAST"
	case "l2vpn_evpn":
		afi = "L2VPN_EVPN"
	}

    rmap["afi-safi-name"] = afi

	log.Info("DbToYang_bgp_gbl_afi_safi_key_xfmr: rmap:", rmap)
    return rmap, nil
}
