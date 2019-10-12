package transformer

import (
	//    "errors"
	//    "strings"
	//    "strconv"
	//    "reflect"
	//    "regexp"
	//    "net"
	//    "github.com/openconfig/ygot/ygot"
	//    "translib/db"
	log "github.com/golang/glog"
	//    "translib/ocbinds"
	//    "bufio"
	//    "os"
)

func init() {
	XlateFuncBind("YangToDb_bgp_gbl_tbl_key", YangToDb_bgp_gbl_tbl_key)
	XlateFuncBind("DbToYangbgp_gbl_tbl_key", DbToYang_bgp_gbl_tbl_key)
}

var YangToDb_bgp_gbl_tbl_key KeyXfmrYangToDb = func(inParams XfmrParams) (string, error) {
	//var entry_key string
	var err error

	pathInfo := NewPathInfo(inParams.uri)
	/* @@TODO Make sure name is vrf-name instead of BGP protocol name in the URI */
	vrfName := pathInfo.Var("name")

	/* @@TODO Return error for protocols other than BGP here */
	log.Info("URI VRF", inParams.uri, vrfName)

	return vrfName, err
}

var DbToYang_bgp_gbl_tbl_key KeyXfmrDbToYang = func(inParams XfmrParams) (map[string]interface{}, error) {
	rmap := make(map[string]interface{})
	var err error
	entry_key := inParams.key
	log.Info("DbToYang_bgp_gbl_tbl_key: ", entry_key)

	rmap["name"] = entry_key
	return rmap, err
}
