package transformer

import (
    "errors"
    "fmt"
    "strconv"
    "translib/ocbinds"
    log "github.com/golang/glog"
)

func init () {
    XlateFuncBind("DbToYang_bgp_routes_get_xfmr", DbToYang_bgp_routes_get_xfmr)
}

type _xfmr_bgp_rib_key struct {
    niName string
    afiSafiName string
    prefix string
    origin string
    pathId int
    nbrAddr string
}

func print_rib_keys (rib_key *_xfmr_bgp_rib_key) string {
    return fmt.Sprintf("niName:%s ; afiSafiName:%s ; prefix:%s ; origin:%s ; pathId:%d ; nbrAddr:%s",
                       rib_key.niName, rib_key.afiSafiName, rib_key.prefix, rib_key.origin, rib_key.pathId, rib_key.nbrAddr)
}

func fill_ipv4_specific_pfx_path_loc_rib_data (ipv4LocRibRoutes_obj *ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib_AfiSafis_AfiSafi_Ipv4Unicast_LocRib_Routes,
                                               prefix string, pathId uint32, pathData map[string]interface{}) bool {
    peer, ok := pathData["peer"].(map[string]interface{})
    if !ok {return false}

    peerId, ok := peer["peerId"].(string)
    if !ok {return false}

    _route_origin := &ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib_AfiSafis_AfiSafi_Ipv4Unicast_LocRib_Routes_Route_State_Origin_Union_String{peerId}
    ipv4LocRibRoute_obj, err := ipv4LocRibRoutes_obj.NewRoute (prefix, _route_origin, pathId)
    if err != nil {return false}

    var _state ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib_AfiSafis_AfiSafi_Ipv4Unicast_LocRib_Routes_Route_State
    ipv4LocRibRoute_obj.State = &_state
    ipv4LocRibRouteState := ipv4LocRibRoute_obj.State

    ipv4LocRibRouteState.Prefix = &prefix
    ipv4LocRibRouteState.Origin = _route_origin
    ipv4LocRibRouteState.PathId = &pathId

    if value, ok := pathData["valid"].(bool) ; ok {
        ipv4LocRibRouteState.ValidRoute = &value
    }

    lastUpdate, ok := pathData["lastUpdate"].(map[string]interface{})
    if ok {
        if value, ok := lastUpdate["epoch"] ; ok {
            _lastUpdateEpoch := uint64(value.(float64))
            ipv4LocRibRouteState.LastModified = &_lastUpdateEpoch
        }
    }

    return true
}


func hdl_get_bgp_ipv4_local_rib (ribAfiSafi_obj *ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib_AfiSafis_AfiSafi,
                                 rib_key *_xfmr_bgp_rib_key, bgpRibOutputJson map[string]interface{}, dbg_log *string) (error) {
    var err error
    var ok bool

    var ipv4Ucast_obj *ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib_AfiSafis_AfiSafi_Ipv4Unicast
    if ipv4Ucast_obj = ribAfiSafi_obj.Ipv4Unicast ; ipv4Ucast_obj == nil {
        var _ipv4Ucast ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib_AfiSafis_AfiSafi_Ipv4Unicast
        ribAfiSafi_obj.Ipv4Unicast = &_ipv4Ucast
        ipv4Ucast_obj = ribAfiSafi_obj.Ipv4Unicast
    }

    var ipv4LocRib_obj *ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib_AfiSafis_AfiSafi_Ipv4Unicast_LocRib
    if ipv4LocRib_obj = ipv4Ucast_obj.LocRib ; ipv4LocRib_obj == nil {
        var _ipv4LocRib ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib_AfiSafis_AfiSafi_Ipv4Unicast_LocRib
        ipv4Ucast_obj.LocRib = &_ipv4LocRib
        ipv4LocRib_obj = ipv4Ucast_obj.LocRib
    }

    var ipv4LocRibRoutes_obj *ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib_AfiSafis_AfiSafi_Ipv4Unicast_LocRib_Routes
    if ipv4LocRibRoutes_obj = ipv4LocRib_obj.Routes ; ipv4LocRibRoutes_obj == nil {
        var _ipv4LocRibRoutes ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib_AfiSafis_AfiSafi_Ipv4Unicast_LocRib_Routes
        ipv4LocRib_obj.Routes = &_ipv4LocRibRoutes
        ipv4LocRibRoutes_obj = ipv4LocRib_obj.Routes
    }

    routes, ok := bgpRibOutputJson["routes"].(map[string]interface{})
    if !ok {return err}

    for prefix, _ := range routes {
        prefixData, ok := routes[prefix].(map[string]interface{}) ; if !ok {continue}
        paths, ok := prefixData["paths"].([]interface {}) ; if !ok {continue}
        for _, _pathData := range paths {
            pathData := _pathData.(map[string]interface {})
            if value, ok := pathData["pathId"] ; ok {
                pathId := uint32(value.(float64))
                if ok := fill_ipv4_specific_pfx_path_loc_rib_data (ipv4LocRibRoutes_obj, prefix, pathId, pathData) ; !ok {continue}
            }
        }
    }

    return err
}

func hdl_get_bgp_ipv6_local_rib (ribAfiSafi_obj *ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib_AfiSafis_AfiSafi,
                                 rib_key *_xfmr_bgp_rib_key, bgpRibOutputJson map[string]interface{}, dbg_log *string) (error) {
    var err error

    var ipv6Ucast_obj *ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib_AfiSafis_AfiSafi_Ipv6Unicast
    if ipv6Ucast_obj = ribAfiSafi_obj.Ipv6Unicast ; ipv6Ucast_obj == nil {
        var _ipv6Ucast ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib_AfiSafis_AfiSafi_Ipv6Unicast
        ribAfiSafi_obj.Ipv6Unicast = &_ipv6Ucast
        ipv6Ucast_obj = ribAfiSafi_obj.Ipv6Unicast
    }

    var ipv6LocRib_obj *ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib_AfiSafis_AfiSafi_Ipv6Unicast_LocRib
    if ipv6LocRib_obj = ipv6Ucast_obj.LocRib ; ipv6LocRib_obj == nil {
        var _ipv6LocRib ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib_AfiSafis_AfiSafi_Ipv6Unicast_LocRib
        ipv6Ucast_obj.LocRib = &_ipv6LocRib
        ipv6LocRib_obj = ipv6Ucast_obj.LocRib
    }

    var ipv6LocRibRoutes_obj *ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib_AfiSafis_AfiSafi_Ipv6Unicast_LocRib_Routes
    if ipv6LocRibRoutes_obj = ipv6LocRib_obj.Routes ; ipv6LocRibRoutes_obj == nil {
        var _ipv6LocRibRoutes ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib_AfiSafis_AfiSafi_Ipv6Unicast_LocRib_Routes
        ipv6LocRib_obj.Routes = &_ipv6LocRibRoutes
        ipv6LocRibRoutes_obj = ipv6LocRib_obj.Routes
    }

    return err
}

func hdl_get_bgp_local_rib (bgpRib_obj *ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib,
                            rib_key *_xfmr_bgp_rib_key, afiSafiType ocbinds.E_OpenconfigBgpTypes_AFI_SAFI_TYPE, dbg_log *string) (error) {
    var err error
    oper_err := errors.New("Opertational error")
    var ok bool

    log.Infof("%s ==> Local-RIB invoke with keys {%s} afiSafiType:%d", *dbg_log, print_rib_keys(rib_key), afiSafiType)

    bgpRibOutputJson, cmd_err := fake_rib_exec_vtysh_cmd ("")
    if (cmd_err != nil) {
        log.Errorf ("%s failed !! Error:%s", *dbg_log, cmd_err);
        return oper_err
    }

    if vrfName, ok := bgpRibOutputJson["vrfName"] ; (!ok || vrfName != rib_key.niName) {
        log.Errorf ("%s failed !! GET-req niName:%s not same as JSON-VRFname:%s", *dbg_log, rib_key.niName, vrfName)
        return oper_err
    }

    var ribAfiSafis_obj *ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib_AfiSafis
    if ribAfiSafis_obj = bgpRib_obj.AfiSafis ; ribAfiSafis_obj == nil {
        var _ribAfiSafis ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib_AfiSafis
        bgpRib_obj.AfiSafis = &_ribAfiSafis
        ribAfiSafis_obj = bgpRib_obj.AfiSafis
    }

    var ribAfiSafi_obj *ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib_AfiSafis_AfiSafi
    if ribAfiSafi_obj, ok = ribAfiSafis_obj.AfiSafi[afiSafiType] ; !ok {
        ribAfiSafi_obj, _ = ribAfiSafis_obj.NewAfiSafi (afiSafiType)
    }

    if afiSafiType == ocbinds.OpenconfigBgpTypes_AFI_SAFI_TYPE_IPV4_UNICAST {
        err = hdl_get_bgp_ipv4_local_rib (ribAfiSafi_obj, rib_key, bgpRibOutputJson, dbg_log)
    }

    if afiSafiType == ocbinds.OpenconfigBgpTypes_AFI_SAFI_TYPE_IPV6_UNICAST {
        err = hdl_get_bgp_ipv6_local_rib (ribAfiSafi_obj, rib_key, bgpRibOutputJson, dbg_log)
    }

    return err
}

func hdl_get_bgp_nbrs_adj_rib_in_pre (bgpRib_obj *ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib,
                                      rib_key *_xfmr_bgp_rib_key, afiSafiType ocbinds.E_OpenconfigBgpTypes_AFI_SAFI_TYPE, dbg_log *string) (error) {
    var err error
    return err
}

func hdl_get_bgp_nbrs_adj_rib_in_post (bgpRib_obj *ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib,
                                       rib_key *_xfmr_bgp_rib_key, afiSafiType ocbinds.E_OpenconfigBgpTypes_AFI_SAFI_TYPE, dbg_log *string) (error) {
    var err error
    return err
}

func hdl_get_bgp_nbrs_adj_rib_out_post (bgpRib_obj *ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp_Rib,
                                        rib_key *_xfmr_bgp_rib_key, afiSafiType ocbinds.E_OpenconfigBgpTypes_AFI_SAFI_TYPE, dbg_log *string) (error) {
    var err error
    return err
}

var DbToYang_bgp_routes_get_xfmr SubTreeXfmrDbToYang = func(inParams XfmrParams) error {
    var err error
    oper_err := errors.New("Opertational error")
    cmn_log := "GET: xfmr for BGP-RIB"

    var bgp_obj *ocbinds.OpenconfigNetworkInstance_NetworkInstances_NetworkInstance_Protocols_Protocol_Bgp
    var rib_key _xfmr_bgp_rib_key

    bgp_obj, rib_key.niName, err = getBgpRoot (inParams)
    if err != nil {
        log.Errorf ("%s failed !! Error:%s", cmn_log, err);
        return oper_err
    }

    bgpRib_obj := bgp_obj.Rib
    if bgpRib_obj == nil {
        log.Errorf("%s failed !! Error: BGP RIB container missing", cmn_log)
        return oper_err
    }

    pathInfo := NewPathInfo(inParams.uri)
    targetUriPath, err := getYangPathFromUri(pathInfo.Path)

    rib_key.afiSafiName = pathInfo.Var("afi-safi-name")
    rib_key.prefix = pathInfo.Var("prefix")
    rib_key.prefix = pathInfo.Var("origin")
    rib_key.pathId, err = strconv.Atoi(pathInfo.Var("path-id"))
    rib_key.nbrAddr = pathInfo.Var("neighbor-address")

    dbg_log := cmn_log + " Path: " + targetUriPath

    switch targetUriPath {
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/loc-rib": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/loc-rib/routes": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/loc-rib/routes/route":
            if (rib_key.afiSafiName == "") || (rib_key.afiSafiName == "IPV4_UNICAST") {
                err = hdl_get_bgp_local_rib (bgpRib_obj, &rib_key, ocbinds.OpenconfigBgpTypes_AFI_SAFI_TYPE_IPV4_UNICAST, &dbg_log)
                if err != nil {return oper_err}
            }
    }

    switch targetUriPath {
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/loc-rib": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/loc-rib/routes": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/loc-rib/routes/route":
            if (rib_key.afiSafiName == "") || (rib_key.afiSafiName == "IPV6_UNICAST") {
                err = hdl_get_bgp_local_rib (bgpRib_obj, &rib_key, ocbinds.OpenconfigBgpTypes_AFI_SAFI_TYPE_IPV6_UNICAST, &dbg_log)
                if err != nil {return oper_err}
            }
    }

    switch targetUriPath {
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-in-pre": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-in-pre/routes": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-in-pre/routes/route":
            if (rib_key.afiSafiName == "") || (rib_key.afiSafiName == "IPV4_UNICAST") {
                err = hdl_get_bgp_nbrs_adj_rib_in_pre (bgpRib_obj, &rib_key, ocbinds.OpenconfigBgpTypes_AFI_SAFI_TYPE_IPV4_UNICAST, &dbg_log)
                if err != nil {return oper_err}
            }
    }

    switch targetUriPath {
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-in-pre": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-in-pre/routes": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-in-pre/routes/route":
            if (rib_key.afiSafiName == "") || (rib_key.afiSafiName == "IPV6_UNICAST") {
                err = hdl_get_bgp_nbrs_adj_rib_in_pre (bgpRib_obj, &rib_key, ocbinds.OpenconfigBgpTypes_AFI_SAFI_TYPE_IPV6_UNICAST, &dbg_log)
                if err != nil {return oper_err}
            }
    }

    switch targetUriPath {
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-in-post": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-in-post/routes": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-in-post/routes/route":
            if (rib_key.afiSafiName == "") || (rib_key.afiSafiName == "IPV4_UNICAST") {
                err = hdl_get_bgp_nbrs_adj_rib_in_post (bgpRib_obj, &rib_key, ocbinds.OpenconfigBgpTypes_AFI_SAFI_TYPE_IPV4_UNICAST, &dbg_log)
                if err != nil {return oper_err}
            }
    }

    switch targetUriPath {
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-in-post": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-in-post/routes": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-in-post/routes/route":
            if (rib_key.afiSafiName == "") || (rib_key.afiSafiName == "IPV6_UNICAST") {
                err = hdl_get_bgp_nbrs_adj_rib_in_post (bgpRib_obj, &rib_key, ocbinds.OpenconfigBgpTypes_AFI_SAFI_TYPE_IPV6_UNICAST, &dbg_log)
                if err != nil {return oper_err}
            }
    }

    switch targetUriPath {
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-post": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-post/routes": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-unicast/neighbors/neighbor/adj-rib-out-post/routes/route":
            if (rib_key.afiSafiName == "") || (rib_key.afiSafiName == "IPV4_UNICAST") {
                err = hdl_get_bgp_nbrs_adj_rib_out_post (bgpRib_obj, &rib_key, ocbinds.OpenconfigBgpTypes_AFI_SAFI_TYPE_IPV4_UNICAST, &dbg_log)
                if err != nil {return oper_err}
            }
    }

    switch targetUriPath {
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-post": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-post/routes": fallthrough
        case "/openconfig-network-instance:network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-unicast/neighbors/neighbor/adj-rib-out-post/routes/route":
            if (rib_key.afiSafiName == "") || (rib_key.afiSafiName == "IPV6_UNICAST") {
                err = hdl_get_bgp_nbrs_adj_rib_out_post (bgpRib_obj, &rib_key, ocbinds.OpenconfigBgpTypes_AFI_SAFI_TYPE_IPV6_UNICAST, &dbg_log)
                if err != nil {return oper_err}
            }
    }

    return err;
}
