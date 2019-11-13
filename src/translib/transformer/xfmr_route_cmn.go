package transformer

import (
    "errors"
    "strings"
    log "github.com/golang/glog"
)


func init () {
    XlateFuncBind("YangToDb_route_table_conn_key_xfmr", YangToDb_route_table_conn_key_xfmr)
    XlateFuncBind("DbToYang_route_table_conn_key_xfmr", DbToYang_route_table_conn_key_xfmr)
    XlateFuncBind("YangToDb_route_table_addr_family_xfmr", YangToDb_route_table_addr_family_xfmr)
    XlateFuncBind("DbToYang_route_table_addr_family_xfmr", DbToYang_route_table_addr_family_xfmr)
}

var YangToDb_route_table_addr_family_xfmr FieldXfmrYangToDb = func(inParams XfmrParams) (map[string]string, error) {
    res_map := make(map[string]string)

    res_map["NULL"] = "NULL"
    return res_map, nil
}

var DbToYang_route_table_addr_family_xfmr FieldXfmrDbtoYang = func(inParams XfmrParams) (map[string]interface{}, error) {

    var err error
    result := make(map[string]interface{})

    entry_key := inParams.key
    key := strings.Split(entry_key, "|")
    family := key[3]

    result["address-family"] = family 

    return result, err
}


var YangToDb_route_table_conn_key_xfmr KeyXfmrYangToDb = func(inParams XfmrParams) (string, error) {
    var err error
    log.Info("YangToDb_route_table_conn_key_xfmr***", inParams.uri)
    pathInfo := NewPathInfo(inParams.uri)

    niName     :=  pathInfo.Var("name")
    srcProto   := pathInfo.Var("src-protocol")
    dstProto   := pathInfo.Var("dst-protocol")
    afName     := pathInfo.Var("address-family")

    if len(pathInfo.Vars) < 3 {
        err = errors.New("Invalid Key length");
        log.Info("Invalid Key length", len(pathInfo.Vars))
        return niName, err
    }

    if len(niName) == 0 {
        err = errors.New("vrf name is missing");
        log.Info("VRF Name is Missing")
        return niName, err
    }

    var family string
    var source string
    var destination string

    if strings.Contains(afName, "IPV4") {
        family = "ipv4"
    } else if strings.Contains(afName, "IPV6") {
        family = "ipv6"
    } else {
		log.Info("Unsupported address-family " + afName)
		return family, errors.New("Unsupported address-family " + afName)
    }

    if strings.Contains(srcProto, "DIRECTLY_CONNECTED") {
        source = "connected"
    } else if strings.Contains(srcProto, "OSPF") {
        source = "ospf"
    } else if strings.Contains(srcProto, "OSPF3") {
        source = "ospf3"
    } else if strings.Contains(srcProto, "STATIC") {
        source = "static"
    } else {
		log.Info("Unsupported protocol " + srcProto)
		return family, errors.New("Unsupported protocol " + srcProto)
    }

    if strings.Contains(dstProto, "BGP") {
        destination = "bgp"
    } else {
		log.Info("Unsupported protocol " + dstProto)
		return family, errors.New("Unsupported protocol " + dstProto)
    }

    key := niName + "|" + source + "|" + destination + "|" + family 

    log.Info("TableConnection key: ", key)

    return key, nil
}

var DbToYang_route_table_conn_key_xfmr KeyXfmrDbToYang = func(inParams XfmrParams) (map[string]interface{}, error) {
    rmap := make(map[string]interface{})
    entry_key := inParams.key
    log.Info("DbToYang_route_table_conn_key_xfmr: ", entry_key)

    key := strings.Split(entry_key, "|")
    source := key[1]
    destination := key[2]
    family := key[3]

    rmap["src-protocol"] = source
    rmap["dst-protocol"] = destination
    rmap["address-family"] = family 

    return rmap, nil
}

