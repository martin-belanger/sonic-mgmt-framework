package transformer

import (
    "errors"
    "strings"
    "strconv"
    "regexp"
    "net"
    "github.com/openconfig/ygot/ygot"
    "translib/db"
    log "github.com/golang/glog"
    "translib/ocbinds"
    "translib/tlerr"
    "bufio"
    "os"
)

func init () {
    XlateFuncBind("intf_table_xfmr", intf_table_xfmr)
    XlateFuncBind("YangToDb_intf_name_xfmr", YangToDb_intf_name_xfmr)
    XlateFuncBind("DbToYang_intf_name_xfmr", DbToYang_intf_name_xfmr)
    XlateFuncBind("YangToDb_intf_enabled_xfmr", YangToDb_intf_enabled_xfmr)
    XlateFuncBind("DbToYang_intf_enabled_xfmr", DbToYang_intf_enabled_xfmr)
    XlateFuncBind("DbToYang_intf_admin_status_xfmr", DbToYang_intf_admin_status_xfmr)
    XlateFuncBind("DbToYang_intf_oper_status_xfmr", DbToYang_intf_oper_status_xfmr)
    XlateFuncBind("YangToDb_intf_eth_auto_neg_xfmr", YangToDb_intf_eth_auto_neg_xfmr)
    XlateFuncBind("DbToYang_intf_eth_auto_neg_xfmr", DbToYang_intf_eth_auto_neg_xfmr)
    XlateFuncBind("YangToDb_intf_eth_port_speed_xfmr", YangToDb_intf_eth_port_speed_xfmr)
    XlateFuncBind("DbToYang_intf_eth_port_speed_xfmr", DbToYang_intf_eth_port_speed_xfmr)
    XlateFuncBind("YangToDb_intf_eth_port_aggregate_xfmr", YangToDb_intf_eth_port_aggregate_xfmr)
   // XlateFuncBind("DbToYang_intf_eth_port_aggregate_xfmr", DbToYang_intf_eth_port_aggregate_xfmr)
    XlateFuncBind("YangToDb_intf_ip_addr_xfmr", YangToDb_intf_ip_addr_xfmr)
    XlateFuncBind("DbToYang_intf_ip_addr_xfmr", DbToYang_intf_ip_addr_xfmr)
    XlateFuncBind("YangToDb_intf_subintfs_xfmr", YangToDb_intf_subintfs_xfmr)
    XlateFuncBind("DbToYang_intf_subintfs_xfmr", DbToYang_intf_subintfs_xfmr)
    XlateFuncBind("DbToYang_intf_get_counters_xfmr", DbToYang_intf_get_counters_xfmr)
	XlateFuncBind("YangToDb_intf_tbl_key_xfmr", YangToDb_intf_tbl_key_xfmr)
}
const (
    PORT_INDEX         = "index"
    PORT_MTU           = "mtu"
    PORT_ADMIN_STATUS  = "admin_status"
    PORT_SPEED         = "speed"
    PORT_DESC          = "description"
    PORT_OPER_STATUS   = "oper_status"
    PORT_AUTONEG       = "autoneg"
    VLAN_TN            = "VLAN"
    VLAN_MEMBER_TN     = "VLAN_MEMBER"
)

const (
    PIPE                     =  "|"
    COLON                    =  ":"

    ETHERNET                 = "Ethernet"
    MGMT                     = "eth"
    VLAN                     = "Vlan"
    PORTCHANNEL              = "PortChannel"
)

type TblData  struct  {
    portTN           string
    memberTN         string
    intfTN           string
    memTN            string
    keySep           string
}

type PopulateIntfCounters func (inParams XfmrParams, counters *ocbinds.OpenconfigInterfaces_Interfaces_Interface_State_Counters) (error)
type CounterData struct {
    OIDTN             string
    CountersTN        string
    PopulateCounters  PopulateIntfCounters
}

type IntfTblData struct {
    intfPrefix          string
    cfgDb               TblData
    appDb               TblData
    stateDb             TblData
    CountersHdl         CounterData
}

var IntfTypeTblMap = map[E_InterfaceType]IntfTblData {
    IntfTypeEthernet: IntfTblData{
        cfgDb:TblData{portTN:"PORT", intfTN: "INTERFACE", keySep:PIPE},
        appDb:TblData{portTN:"PORT_TABLE", intfTN: "INTF_TABLE", keySep: COLON},
        stateDb:TblData{portTN: "PORT_TABLE", intfTN: "INTERFACE_TABLE", keySep: PIPE},
        CountersHdl:CounterData{OIDTN: "COUNTERS_PORT_NAME_MAP", CountersTN: "COUNTERS", PopulateCounters: populatePortCounters},
    },
    IntfTypeMgmt : IntfTblData{
        cfgDb:TblData{portTN:"MGMT_PORT", intfTN:"MGMT_INTERFACE", keySep: PIPE},
        appDb:TblData{portTN:"MGMT_PORT_TABLE", intfTN:"MGMT_INTF_TABLE", keySep: COLON},
        stateDb:TblData{portTN:"MGMT_PORT_TABLE", intfTN:"MGMT_INTERFACE_TABLE", keySep: PIPE},
        CountersHdl:CounterData{OIDTN: "", CountersTN:"", PopulateCounters: populateMGMTPortCounters},
    },
    IntfTypePortChannel : IntfTblData{
        cfgDb:TblData{portTN:"PORTCHANNEL", intfTN:"PORTCHANNEL_INTERFACE", memTN:"PORTCHANNEL_MEMBER", keySep: PIPE},
        appDb:TblData{portTN:"LAG_TABLE", intfTN:"INTF_TABLE", keySep: COLON},
        stateDb:TblData{portTN:"LAG_TABLE", intfTN:"INTERFACE_TABLE", keySep: PIPE},
        CountersHdl:CounterData{OIDTN: "COUNTERS_PORT_NAME_MAP", CountersTN:"COUNTERS", PopulateCounters: populatePortCounters},
    },
    IntfTypeVlan : IntfTblData{
        cfgDb:TblData{portTN:"VLAN", memberTN: "VLAN_MEMBER", intfTN:"VLAN_INTERFACE", keySep: PIPE},
        appDb:TblData{portTN:"VLAN_TABLE", memberTN: "VLAN_MEMBER_TABLE", intfTN:"INTF_TABLE", keySep: COLON},
    },
}

var dbIdToTblMap = map[db.DBNum][]string {
    db.ConfigDB: {"PORT", "INTERFACE", "MGMT_PORT", "MGMT_INTERFACE","VLAN", "VLAN_MEMBER", "VLAN_INTERFACE", "PORTCHANNEL", "PORTCHANNEL_INTERFACE", "PORTCHANNEL_MEMBER"},
    db.ApplDB  : {"PORT_TABLE", "INTF_TABLE", "MGMT_PORT_TABLE", "MGMT_INTF_TABLE", "VLAN_TABLE", "VLAN_MEMBER_TABLE", "LAG_TABLE"},
    db.StateDB : {"PORT_TABLE", "INTERFACE_TABLE", "MGMT_PORT_TABLE", "MGMT_INTERFACE_TABLE", "LAG_TABLE"},
}

var intfOCToSpeedMap = map[ocbinds.E_OpenconfigIfEthernet_ETHERNET_SPEED] string {
    ocbinds.OpenconfigIfEthernet_ETHERNET_SPEED_SPEED_10MB: "10",
    ocbinds.OpenconfigIfEthernet_ETHERNET_SPEED_SPEED_100MB: "100",
    ocbinds.OpenconfigIfEthernet_ETHERNET_SPEED_SPEED_1GB: "1000",
    ocbinds.OpenconfigIfEthernet_ETHERNET_SPEED_SPEED_2500MB: "2500",
    ocbinds.OpenconfigIfEthernet_ETHERNET_SPEED_SPEED_5GB: "5000",
    ocbinds.OpenconfigIfEthernet_ETHERNET_SPEED_SPEED_10GB: "10000",
    ocbinds.OpenconfigIfEthernet_ETHERNET_SPEED_SPEED_25GB: "25000",
    ocbinds.OpenconfigIfEthernet_ETHERNET_SPEED_SPEED_40GB: "40000",
    ocbinds.OpenconfigIfEthernet_ETHERNET_SPEED_SPEED_50GB: "50000",
    ocbinds.OpenconfigIfEthernet_ETHERNET_SPEED_SPEED_100GB: "100000",

}


type E_InterfaceType  int64
const (
    IntfTypeUnset           E_InterfaceType = 0
    IntfTypeEthernet        E_InterfaceType = 1
    IntfTypeMgmt            E_InterfaceType = 2
    IntfTypeVlan            E_InterfaceType = 3
    IntfTypePortChannel     E_InterfaceType = 4

)
type E_InterfaceSubType int64
const (
    IntfSubTypeUnset        E_InterfaceSubType = 0
    IntfSubTypeVlanL2  E_InterfaceSubType = 1
    InterfaceSubTypeVlanL3  E_InterfaceSubType = 2
)

func getIntfTypeByName (name string) (E_InterfaceType, E_InterfaceSubType, error) {

    var err error
    if strings.HasPrefix(name, ETHERNET) == true {
        return IntfTypeEthernet, IntfSubTypeUnset, err
    } else if strings.HasPrefix(name, MGMT) == true {
        return IntfTypeMgmt, IntfSubTypeUnset, err
    } else if strings.HasPrefix(name, VLAN) == true {
        return IntfTypeVlan, IntfSubTypeUnset, err
    } else if strings.HasPrefix(name, PORTCHANNEL) == true {
        return IntfTypePortChannel, IntfSubTypeUnset, err
    } else {
        err = errors.New("Interface name prefix not matched with supported types")
        return IntfTypeUnset, IntfSubTypeUnset, err
    }
}

func getIntfsRoot (s *ygot.GoStruct) *ocbinds.OpenconfigInterfaces_Interfaces {
    deviceObj := (*s).(*ocbinds.Device)
    return deviceObj.Interfaces
}

var YangToDb_intf_tbl_key_xfmr KeyXfmrYangToDb = func(inParams XfmrParams) (string, error) {
	log.Info("Entering YangToDb_intf_tbl_key_xfmr")
    var err error

    pathInfo := NewPathInfo(inParams.uri)
    ifName := pathInfo.Var("name")

    log.Info("Intf name ", ifName)
	log.Info("Exiting YangToDb_intf_tbl_key_xfmr")

    return ifName, err
}

var intf_table_xfmr TableXfmrFunc = func (inParams XfmrParams) ([]string, error) {

    var tblList []string
    var err error

    log.Info("TableXfmrFunc - Uri: ", inParams.uri);
    pathInfo := NewPathInfo(inParams.uri)

    targetUriPath, err := getYangPathFromUri(pathInfo.Path)

    ifName := pathInfo.Var("name");
    if ifName == "" {
        log.Info("TableXfmrFunc - intf_table_xfmr Intf key is not present")

        if _, ok := dbIdToTblMap[inParams.curDb]; !ok {
            log.Info("TableXfmrFunc - intf_table_xfmr db id entry not present")
            return tblList, errors.New("Key not present")
        } else {
            return dbIdToTblMap[inParams.curDb], nil
        }
    }

    intfType, _, ierr := getIntfTypeByName(ifName)
    if intfType == IntfTypeUnset || ierr != nil {
        log.Info("TableXfmrFunc - Invalid interface type IntfTypeUnset");
        return tblList, errors.New("Invalid interface type IntfTypeUnset");
    }
    intTbl := IntfTypeTblMap[intfType]
    log.Info("-----------------intTbl : ", intTbl)
    log.Info("TableXfmrFunc - targetUriPath : ", targetUriPath)

    if strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/config"){ //||
      //  strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/ethernet/config") ||
     //   strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/openconfig-if-ethernet:ethernet/config") 
 
        log.Info("....I am here 1")
        tblList = append(tblList, intTbl.cfgDb.portTN)
    } else if  strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/state/counters") {
        tblList = append(tblList, intTbl.CountersHdl.CountersTN)
    } else if strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/state") ||
        strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/ethernet/state") ||
        strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/openconfig-if-ethernet:ethernet/state") {
        tblList = append(tblList, intTbl.appDb.portTN)
    } else if strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/config") ||
        strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/config") ||
        strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/config") ||
        strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/ipv6/addresses/address/config") {
        tblList = append(tblList, intTbl.cfgDb.intfTN)
    } else if strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/state") ||
        strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/state") ||
        strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/state") ||
        strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/ipv6/addresses/address/state") {
        tblList = append(tblList, intTbl.appDb.intfTN)
    } else if strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/ipv4/addresses") ||
        strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses") ||
        strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses") ||
        strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/ipv6/addresses") {
        tblList = append(tblList, intTbl.cfgDb.intfTN)
    } else if strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/ethernet") ||
        strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/openconfig-if-ethernet:ethernet") {
        log.Info("....I am here 2")
        tblList = append(tblList, intTbl.cfgDb.portTN)
/*    } else if strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/openconfig-if-ethernet:ethernet/config/openconfig-if-aggregate:aggregate-id") {
        log.Info("....I am here 4-----")
        tblList = append(tblList, intTbl.cfgDb.memTN)
*/    } else if strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface") { //To be used for creation/deletion of interface
        log.Info("....I am here 3---", targetUriPath)
        tblList = append(tblList, intTbl.cfgDb.portTN)
    } else {       err = errors.New("Invalid URI")
    }

    log.Infof("TableXfmrFunc - uri(%v), tblList(%v)\r\n", inParams.uri, tblList);
    return tblList, err
}

var YangToDb_intf_name_xfmr FieldXfmrYangToDb = func(inParams XfmrParams) (map[string]string, error) {
    res_map := make(map[string]string)
    var err error

    pathInfo := NewPathInfo(inParams.uri)
    ifName := pathInfo.Var("name")

    if strings.HasPrefix(ifName, VLAN) == true {
        vlanId := ifName[len("Vlan"):len(ifName)]
        res_map["vlanid"] = vlanId
    }

    log.Info("YangToDb_intf_name_xfm: rres_map:", res_map)
    return res_map, err
}


var DbToYang_intf_name_xfmr FieldXfmrDbtoYang = func(inParams XfmrParams) (map[string]interface{}, error) {
    var err error
    res_map := make(map[string]interface{})
    res_map["name"] =  inParams.key
    return res_map, err
}

var YangToDb_intf_enabled_xfmr FieldXfmrYangToDb = func(inParams XfmrParams) (map[string]string, error) {
    res_map := make(map[string]string)

    enabled, _ := inParams.param.(*bool)
    var enStr string
    if *enabled == true {
        enStr = "up"
    } else {
        enStr = "down"
    }
    res_map[PORT_ADMIN_STATUS] = enStr

    return res_map, nil
}

func getPortTableNameByDBId (intftbl IntfTblData, curDb db.DBNum) (string, error) {

    var tblName string

    switch (curDb) {
    case db.ConfigDB:
        tblName = intftbl.cfgDb.portTN
    case db.ApplDB:
        tblName = intftbl.appDb.portTN
    case db.StateDB:
        tblName = intftbl.stateDb.portTN
    default:
        tblName = intftbl.cfgDb.portTN
    }

    return tblName, nil
}

var DbToYang_intf_enabled_xfmr FieldXfmrDbtoYang = func(inParams XfmrParams) (map[string]interface{}, error) {
    var err error
    result := make(map[string]interface{})

    data := (*inParams.dbDataMap)[inParams.curDb]

    intfType, _, ierr := getIntfTypeByName(inParams.key)
    if intfType == IntfTypeUnset || ierr != nil {
        log.Info("DbToYang_intf_enabled_xfmr - Invalid interface type IntfTypeUnset");
        return result, errors.New("Invalid interface type IntfTypeUnset");
    }
    intTbl := IntfTypeTblMap[intfType]

    tblName, _ := getPortTableNameByDBId(intTbl, inParams.curDb)
    if _, ok := data[tblName]; !ok {
        log.Info("DbToYang_intf_enabled_xfmr table not found : ", tblName)
        return result, errors.New("table not found : " + tblName)
    }

    pTbl := data[tblName]
    if _, ok := pTbl[inParams.key]; !ok {
        log.Info("DbToYang_intf_enabled_xfmr Interface not found : ", inParams.key)
        return result, errors.New("Interface not found : " + inParams.key)
    }
    prtInst := pTbl[inParams.key]
    adminStatus, ok := prtInst.Field[PORT_ADMIN_STATUS]
    if ok {
        if adminStatus == "up" {
            result["enabled"] = true
        } else {
            result["enabled"] = false
        }
    } else {
        log.Info("Admin status field not found in DB")
    }
    return result, err
}

var DbToYang_intf_admin_status_xfmr FieldXfmrDbtoYang = func(inParams XfmrParams) (map[string]interface{}, error) {
    var err error
    result := make(map[string]interface{})

    data := (*inParams.dbDataMap)[inParams.curDb]

    intfType, _, ierr := getIntfTypeByName(inParams.key)
    if intfType == IntfTypeUnset || ierr != nil {
        log.Info("DbToYang_intf_admin_status_xfmr - Invalid interface type IntfTypeUnset");
        return result, errors.New("Invalid interface type IntfTypeUnset");
    }
    intTbl := IntfTypeTblMap[intfType]

    tblName, _ := getPortTableNameByDBId(intTbl, inParams.curDb)
    if _, ok := data[tblName]; !ok {
        log.Info("DbToYang_intf_admin_status_xfmr table not found : ", tblName)
        return result, errors.New("table not found : " + tblName)
    }
    pTbl := data[tblName]
    if _, ok := pTbl[inParams.key]; !ok {
        log.Info("DbToYang_intf_admin_status_xfmr Interface not found : ", inParams.key)
        return result, errors.New("Interface not found : " + inParams.key)
    }
    prtInst := pTbl[inParams.key]
    adminStatus, ok := prtInst.Field[PORT_ADMIN_STATUS]
    var status ocbinds.E_OpenconfigInterfaces_Interfaces_Interface_State_AdminStatus
    if ok {
        if adminStatus == "up" {
            status = ocbinds.OpenconfigInterfaces_Interfaces_Interface_State_AdminStatus_UP
        } else {
            status = ocbinds.OpenconfigInterfaces_Interfaces_Interface_State_AdminStatus_DOWN
        }
        result["admin-status"] = ocbinds.E_OpenconfigInterfaces_Interfaces_Interface_State_AdminStatus.ΛMap(status)["E_OpenconfigInterfaces_Interfaces_Interface_State_AdminStatus"][int64(status)].Name
    } else {
        log.Info("Admin status field not found in DB")
    }

    return result, err
}

var DbToYang_intf_oper_status_xfmr FieldXfmrDbtoYang = func(inParams XfmrParams) (map[string]interface{}, error) {
    var err error
    result := make(map[string]interface{})
    var prtInst db.Value

    data := (*inParams.dbDataMap)[inParams.curDb]
    intfType, _, ierr := getIntfTypeByName(inParams.key)
    if intfType == IntfTypeUnset || ierr != nil {
        log.Info("DbToYang_intf_oper_status_xfmr - Invalid interface type IntfTypeUnset");
        return result, errors.New("Invalid interface type IntfTypeUnset");
    }
    intTbl := IntfTypeTblMap[intfType]
    if intfType == IntfTypeMgmt {
        pathInfo := NewPathInfo(inParams.uri)
        ifName := pathInfo.Var("name");
        entry, dbErr := inParams.dbs[db.StateDB].GetEntry(&db.TableSpec{Name:intTbl.stateDb.portTN}, db.Key{Comp: []string{ifName}})
        if dbErr != nil {
            log.Info("Failed to read mgmt port status from state DB, " + intTbl.stateDb.portTN + " " + ifName)
            return result, dbErr
        }
        prtInst = entry
    } else {
        tblName, _ := getPortTableNameByDBId(intTbl, inParams.curDb)
        pTbl := data[tblName]
        prtInst = pTbl[inParams.key]
    }

    operStatus, ok := prtInst.Field[PORT_OPER_STATUS]
    var status ocbinds.E_OpenconfigInterfaces_Interfaces_Interface_State_OperStatus
    if ok {
        if operStatus == "up" {
            status = ocbinds.OpenconfigInterfaces_Interfaces_Interface_State_OperStatus_UP
        } else {
            status = ocbinds.OpenconfigInterfaces_Interfaces_Interface_State_OperStatus_DOWN
        }
        result["oper-status"] = ocbinds.E_OpenconfigInterfaces_Interfaces_Interface_State_OperStatus.ΛMap(status)["E_OpenconfigInterfaces_Interfaces_Interface_State_OperStatus"][int64(status)].Name
    } else {
        log.Info("Oper status field not found in DB")
    }

    return result, err
}


var YangToDb_intf_eth_auto_neg_xfmr FieldXfmrYangToDb = func(inParams XfmrParams) (map[string]string, error) {
    res_map := make(map[string]string)

    autoNeg, _ := inParams.param.(*bool)
    var enStr string
    if *autoNeg == true {
        enStr = "true"
    } else {
        enStr = "false"
    }
    res_map[PORT_AUTONEG] = enStr

    return res_map, nil
}

var DbToYang_intf_eth_auto_neg_xfmr FieldXfmrDbtoYang = func(inParams XfmrParams) (map[string]interface{}, error) {
    var err error
    result := make(map[string]interface{})

    data := (*inParams.dbDataMap)[inParams.curDb]
    intfType, _, ierr := getIntfTypeByName(inParams.key)
    if intfType == IntfTypeUnset || ierr != nil {
        log.Info("DbToYang_intf_eth_auto_neg_xfmr - Invalid interface type IntfTypeUnset");
        return result, errors.New("Invalid interface type IntfTypeUnset");
    }
    intTbl := IntfTypeTblMap[intfType]

    tblName, _ := getPortTableNameByDBId(intTbl, inParams.curDb)
    pTbl := data[tblName]
    prtInst := pTbl[inParams.key]
    autoNeg, ok := prtInst.Field[PORT_AUTONEG]
    if ok {
        if autoNeg == "true" {
            result["auto-negotiate"] = true
        } else {
            result["auto-negotiate"] = false
        }
    } else {
        log.Info("auto-negotiate field not found in DB")
    }
    return result, err
}


var YangToDb_intf_eth_port_speed_xfmr FieldXfmrYangToDb = func(inParams XfmrParams) (map[string]string, error) {
    res_map := make(map[string]string)
    var err error

    portSpeed, _ := inParams.param.(ocbinds.E_OpenconfigIfEthernet_ETHERNET_SPEED)
    val, ok := intfOCToSpeedMap[portSpeed]
    if ok {
        res_map[PORT_SPEED] = val
    } else {
        err = errors.New("Invalid/Unsupported speed.")
    }

    return res_map, err
}

var DbToYang_intf_eth_port_speed_xfmr FieldXfmrDbtoYang = func(inParams XfmrParams) (map[string]interface{}, error) {
    var err error
    result := make(map[string]interface{})

    data := (*inParams.dbDataMap)[inParams.curDb]
    intfType, _, ierr := getIntfTypeByName(inParams.key)
    if intfType == IntfTypeUnset || ierr != nil {
        log.Info("DbToYang_intf_eth_port_speed_xfmr - Invalid interface type IntfTypeUnset");
        return result, errors.New("Invalid interface type IntfTypeUnset");
    }
    intTbl := IntfTypeTblMap[intfType]

    tblName, _ := getPortTableNameByDBId(intTbl, inParams.curDb)
    pTbl := data[tblName]
    prtInst := pTbl[inParams.key]
    speed, ok := prtInst.Field[PORT_SPEED]
    portSpeed := ocbinds.OpenconfigIfEthernet_ETHERNET_SPEED_UNSET
    if ok {
        portSpeed, err = getDbToYangSpeed(speed)
        result["port-speed"] = ocbinds.E_OpenconfigIfEthernet_ETHERNET_SPEED.ΛMap(portSpeed)["E_OpenconfigIfEthernet_ETHERNET_SPEED"][int64(portSpeed)].Name
    } else {
        log.Info("Speed field not found in DB")
    }

    return result, err
}



func getDbToYangSpeed (speed string) (ocbinds.E_OpenconfigIfEthernet_ETHERNET_SPEED, error) {
    portSpeed := ocbinds.OpenconfigIfEthernet_ETHERNET_SPEED_SPEED_UNKNOWN
    var err error = errors.New("Not found in port speed map")
    for k, v := range intfOCToSpeedMap {
        if speed == v {
            portSpeed = k
            err = nil
        }
    }
    return portSpeed, err
}

func intf_intf_tbl_key_gen (intfName string, ip string, prefixLen int, keySep string) string {
    return intfName + keySep + ip + "/" + strconv.Itoa(prefixLen)
}

var YangToDb_intf_subintfs_xfmr KeyXfmrYangToDb = func(inParams XfmrParams) (string, error) {
    var subintf_key string
    var err error

    return subintf_key, err
}

var DbToYang_intf_subintfs_xfmr KeyXfmrDbToYang = func(inParams XfmrParams) (map[string]interface{}, error) {
    rmap := make(map[string]interface{})
    var err error
    rmap["index"] = 0
    return rmap, err
}


func intf_ip_addr_del (d *db.DB , ifName string, tblName string, subIntf *ocbinds.OpenconfigInterfaces_Interfaces_Interface_Subinterfaces_Subinterface) (map[string]map[string]db.Value, error) {
    var err error
    subIntfmap := make(map[string]map[string]db.Value)
    intfIpMap := make(map[string]db.Value)

    if subIntf.Ipv4 != nil && subIntf.Ipv4.Addresses != nil {
        if len(subIntf.Ipv4.Addresses.Address) < 1 {
            ipMap, _:= getIntfIpByName(d, tblName, ifName, true, false, "")
            if ipMap != nil && len(ipMap) > 0 {
                for k, v := range ipMap {
                    intfIpMap[k] = v
                }
            }
        } else {
            for ip, _ := range subIntf.Ipv4.Addresses.Address {
                ipMap, _ := getIntfIpByName(d, tblName, ifName, true, false, ip)

                if ipMap != nil && len(ipMap) > 0 {
                    for k, v := range ipMap {
                        intfIpMap[k] = v
                    }
                }
            }
        }
    }

    if subIntf.Ipv6 != nil && subIntf.Ipv6.Addresses != nil {
        if len(subIntf.Ipv6.Addresses.Address) < 1 {
            ipMap, _ := getIntfIpByName(d, tblName, ifName, true, false, "")
            if ipMap != nil && len(ipMap) > 0 {
                for k, v := range ipMap {
                    intfIpMap[k] = v
                }
            }
        } else {
            for ip, _ := range subIntf.Ipv6.Addresses.Address {
                ipMap, _ := getIntfIpByName(d, tblName, ifName, true, false, ip)

                if ipMap != nil && len(ipMap) > 0 {
                    for k, v := range ipMap {
                        intfIpMap[k] = v
                    }
                }
            }
        }
    }
    if len(intfIpMap) > 0 {
        if _, ok := subIntfmap[tblName]; !ok {
            subIntfmap[tblName] = make (map[string]db.Value)
        }

        for k, _ := range intfIpMap {
            ifKey := ifName + "|" + k
            var data db.Value
            subIntfmap[tblName][ifKey] = data
        }
    }
    log.Info("Delete IP address list ", subIntfmap,  " ", err)
    return subIntfmap, err
}


var YangToDb_intf_ip_addr_xfmr SubTreeXfmrYangToDb = func(inParams XfmrParams) (map[string]map[string]db.Value, error) {
    var err error
    subIntfmap := make(map[string]map[string]db.Value)

    intfsObj := getIntfsRoot(inParams.ygRoot)
    if intfsObj == nil || len(intfsObj.Interface) < 1 {
        log.Info("YangToDb_intf_subintf_ip_xfmr : IntfsObj/interface list is empty.")
        return subIntfmap, errors.New("IntfsObj/Interface is not specified")
    }
    pathInfo := NewPathInfo(inParams.uri)
    ifName := pathInfo.Var("name")

    if ifName == "" {
        errStr := "Interface KEY not present"
        log.Info("YangToDb_intf_subintf_ip_xfmr : " + errStr)
        return subIntfmap, errors.New(errStr)
    }

    if _, ok := intfsObj.Interface[ifName]; !ok {
        errStr := "Interface entry not found in Ygot tree, ifname: " + ifName
        log.Info("YangToDb_intf_subintf_ip_xfmr : " + errStr)
        return subIntfmap, errors.New(errStr)
    }

    intfObj := intfsObj.Interface[ifName]

    if intfObj.Subinterfaces == nil || len(intfObj.Subinterfaces.Subinterface) < 1 {
        errStr := "SubInterface node is not set"
        log.Info("YangToDb_intf_subintf_ip_xfmr : " + errStr)
        return subIntfmap, errors.New(errStr)
    }
    if _, ok := intfObj.Subinterfaces.Subinterface[0]; !ok {
        log.Info("YangToDb_intf_subintf_ip_xfmr : No IP address handling required")
        return subIntfmap, err
    }

    intfType, _, ierr := getIntfTypeByName(ifName)
    if intfType == IntfTypeUnset || ierr != nil {
        errStr := "Invalid interface type IntfTypeUnset"
        log.Info("YangToDb_intf_subintf_ip_xfmr : " + errStr)
        return subIntfmap, errors.New(errStr)
    }
    intTbl := IntfTypeTblMap[intfType]
    tblName, _ := getIntfTableNameByDBId(intTbl, inParams.curDb)

    subIntfObj := intfObj.Subinterfaces.Subinterface[0]
    if inParams.oper == DELETE {
        return intf_ip_addr_del(inParams.d, ifName, tblName, subIntfObj)
    }

    if subIntfObj.Ipv4 != nil && subIntfObj.Ipv4.Addresses != nil {
        for ip, _ := range subIntfObj.Ipv4.Addresses.Address {
            addr := subIntfObj.Ipv4.Addresses.Address[ip]
            if addr.Config != nil {
                log.Info("Ip:=", *addr.Config.Ip)
                log.Info("prefix:=", *addr.Config.PrefixLength)
                if !validIPv4(*addr.Config.Ip) {
                    errStr := "Invalid IPv4 address " + *addr.Config.Ip
                    err = tlerr.InvalidArgsError{Format: errStr}
                    return subIntfmap, err
                }
                intf_key := intf_intf_tbl_key_gen(ifName, *addr.Config.Ip, int(*addr.Config.PrefixLength), "|")
                m := make(map[string]string)
                m["NULL"] = "NULL"
                value := db.Value{Field: m}
                if _, ok := subIntfmap[tblName]; !ok {
                    subIntfmap[tblName] = make(map[string]db.Value)
                }
                subIntfmap[tblName][intf_key] = value

            }
        }
    }
    if subIntfObj.Ipv6 != nil && subIntfObj.Ipv6.Addresses != nil {
        for ip, _ := range subIntfObj.Ipv6.Addresses.Address {
            addr := subIntfObj.Ipv6.Addresses.Address[ip]
            if addr.Config != nil {
                log.Info("Ipv6 IP:=", *addr.Config.Ip)
                log.Info("Ipv6 prefix:=", *addr.Config.PrefixLength)
                if !validIPv6(*addr.Config.Ip) {
                    errStr := "Invalid IPv6 address " + *addr.Config.Ip
                    err = tlerr.InvalidArgsError{Format: errStr}
                    return subIntfmap, err
                }
                intf_key := intf_intf_tbl_key_gen(ifName, *addr.Config.Ip, int(*addr.Config.PrefixLength), "|")
                m := make(map[string]string)
                m["NULL"] = "NULL"
                value := db.Value{Field: m}
                if _, ok := subIntfmap[tblName]; !ok {
                    subIntfmap[tblName] = make(map[string]db.Value)
                }
                subIntfmap[tblName][intf_key] = value
            }
        }
    }
    log.Info("YangToDb_intf_subintf_ip_xfmr : subIntfmap : ",  subIntfmap)

    return subIntfmap, err
}

func convertIpMapToOC (intfIpMap map[string]db.Value, ifInfo *ocbinds.OpenconfigInterfaces_Interfaces_Interface, isState bool) error {
    var subIntf *ocbinds.OpenconfigInterfaces_Interfaces_Interface_Subinterfaces_Subinterface
    var err error

    if _, ok := ifInfo.Subinterfaces.Subinterface[0]; !ok {
        subIntf, err = ifInfo.Subinterfaces.NewSubinterface(0)
        if err != nil {
            log.Error("Creation of subinterface subtree failed!")
            return err
        }
    }

    subIntf = ifInfo.Subinterfaces.Subinterface[0]
    ygot.BuildEmptyTree(subIntf)

    for ipKey, _:= range intfIpMap {
        log.Info("IP address = ", ipKey)
        ipB, ipNetB, _ := net.ParseCIDR(ipKey)
        v4Flag := false
        v6Flag := false

        var v4Address *ocbinds.OpenconfigInterfaces_Interfaces_Interface_Subinterfaces_Subinterface_Ipv4_Addresses_Address
        var v6Address *ocbinds.OpenconfigInterfaces_Interfaces_Interface_Subinterfaces_Subinterface_Ipv6_Addresses_Address
        if validIPv4(ipB.String()) {
            if _, ok := subIntf.Ipv4.Addresses.Address[ipB.String()]; !ok {
                v4Address, err = subIntf.Ipv4.Addresses.NewAddress(ipB.String())
            }
            v4Address = subIntf.Ipv4.Addresses.Address[ipB.String()]
            v4Flag = true
        } else if validIPv6(ipB.String()) {
            if _, ok := subIntf.Ipv6.Addresses.Address[ipB.String()]; !ok {
                v6Address, err = subIntf.Ipv6.Addresses.NewAddress(ipB.String())
            }
            v6Address =  subIntf.Ipv6.Addresses.Address[ipB.String()]
            v6Flag = true
        } else {
            log.Error("Invalid IP address " + ipB.String())
            continue
        }
        if err != nil {
            log.Error("Creation of address subtree failed!")
            return err
        }
        if v4Flag {
            ygot.BuildEmptyTree(v4Address)
            ipStr := new(string)
            *ipStr = ipB.String()
            v4Address.Ip = ipStr
            ipNetBNum, _ := ipNetB.Mask.Size()
            prfxLen := new(uint8)
            *prfxLen = uint8(ipNetBNum)
            if isState {
                v4Address.State.Ip = ipStr
                v4Address.State.PrefixLength = prfxLen
            } else {
                v4Address.Config.Ip = ipStr
                v4Address.Config.PrefixLength = prfxLen
            }
        }
        if v6Flag {
            ygot.BuildEmptyTree(v6Address)
            ipStr := new(string)
            *ipStr = ipB.String()
            v6Address.Ip = ipStr
            ipNetBNum, _ := ipNetB.Mask.Size()
            prfxLen := new(uint8)
            *prfxLen = uint8(ipNetBNum)
            if isState {
                v6Address.State.Ip = ipStr
                v6Address.State.PrefixLength = prfxLen
            } else {
                v6Address.Config.Ip = ipStr
                v6Address.Config.PrefixLength = prfxLen
            }
        }
    }
    return err
}

func getIntfIpByName(dbCl *db.DB, tblName string, ifName string, ipv4 bool, ipv6 bool, ip string) (map[string]db.Value, error) {
    var err error
    intfIpMap := make(map[string]db.Value)
    all := true
    if ipv4 == false || ipv6 == false {
        all = false
    }
    log.Info("Updating Interface IP Info from DB to Internal DS for Interface Name : ", ifName)

    keys,_ := doGetAllIpKeys(dbCl, &db.TableSpec{Name:tblName})

    for _, key := range keys {
        if len(key.Comp) < 2 {
            continue
        }
        if key.Get(0) != ifName {
            continue
        }
        if all == false {
            ipB, _, _ := net.ParseCIDR(key.Get(1))
            if ((validIPv4(ipB.String()) && (ipv4 == false)) ||
                (validIPv6(ipB.String()) && (ipv6 == false))) {
                continue
            }
            if ip != "" {
                if ipB.String() != ip {
                    continue
                }
            }
        }

        ipInfo, _ := dbCl.GetEntry(&db.TableSpec{Name:tblName}, key)
        intfIpMap[key.Get(1)]= ipInfo
    }
    return intfIpMap, err 
}

func handleIntfIPGetByTargetURI (inParams XfmrParams, targetUriPath string, ifName string, intfObj *ocbinds.OpenconfigInterfaces_Interfaces_Interface) error {
    ipMap := make(map[string]db.Value)
    var err error

    pathInfo := NewPathInfo(inParams.uri)
    ipAddr := pathInfo.Var("ip")
    intfType, _, ierr := getIntfTypeByName(ifName)
    if intfType == IntfTypeUnset || ierr != nil {
        errStr := "Invalid interface type IntfTypeUnset"
        log.Info("YangToDb_intf_subintf_ip_xfmr : " + errStr)
        return errors.New(errStr)
    }
    intTbl := IntfTypeTblMap[intfType]

    if strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/config") ||
       strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/config") {
           ipMap, err = getIntfIpByName(inParams.dbs[db.ConfigDB], intTbl.cfgDb.intfTN, ifName, true, false, ipAddr)
           log.Info("handleIntfIPGetByTargetURI : ipv4 config ipMap - : ", ipMap)
           convertIpMapToOC(ipMap, intfObj, false)
    } else if strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/config") ||
        strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/ipv6/addresses/address/config") {
           ipMap, err = getIntfIpByName(inParams.dbs[db.ConfigDB], intTbl.cfgDb.intfTN, ifName, false, true, ipAddr)
           log.Info("handleIntfIPGetByTargetURI : ipv6 config ipMap - : ", ipMap)
           convertIpMapToOC(ipMap, intfObj, false)
    } else if strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/state") ||
         strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/state") {
           ipMap, err = getIntfIpByName(inParams.dbs[db.ApplDB], intTbl.appDb.intfTN, ifName, true, false, ipAddr)
           log.Info("handleIntfIPGetByTargetURI : ipv4 state ipMap - : ", ipMap)
           convertIpMapToOC(ipMap, intfObj, true)
    } else if strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/state") ||
         strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/ipv6/addresses/address/state") {
           ipMap, err = getIntfIpByName(inParams.dbs[db.ApplDB], intTbl.appDb.intfTN, ifName, false, true, ipAddr)
           log.Info("handleIntfIPGetByTargetURI : ipv6 state ipMap - : ", ipMap)
           convertIpMapToOC(ipMap, intfObj, true)
    } else if strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface") {
        ipMap, err = getIntfIpByName(inParams.dbs[db.ConfigDB], intTbl.cfgDb.intfTN, ifName, true, true, ipAddr)
           log.Info("handleIntfIPGetByTargetURI : ipv4 and ipv6 config ipMap - : ", ipMap)
        convertIpMapToOC(ipMap, intfObj, false)
        ipMap, err = getIntfIpByName(inParams.dbs[db.ApplDB], intTbl.appDb.intfTN, ifName, true, true, ipAddr)
           log.Info("handleIntfIPGetByTargetURI : ipv4 and ipv6 state ipMap - : ", ipMap)
        convertIpMapToOC(ipMap, intfObj, true)
    }
    return err
}

var DbToYang_intf_ip_addr_xfmr SubTreeXfmrDbToYang = func (inParams XfmrParams) (error) {
    var err error
    intfsObj := getIntfsRoot(inParams.ygRoot)
    pathInfo := NewPathInfo(inParams.uri)
    intfName := pathInfo.Var("name")
    targetUriPath, err := getYangPathFromUri(inParams.uri)
    log.Info("targetUriPath is ", targetUriPath)
    var intfObj *ocbinds.OpenconfigInterfaces_Interfaces_Interface

    if strings.HasPrefix(targetUriPath, "/openconfig-interfaces:interfaces/interface/subinterfaces") {
        if intfsObj != nil && intfsObj.Interface != nil && len(intfsObj.Interface) > 0 {
            var ok bool = false
            if intfObj, ok = intfsObj.Interface[intfName]; !ok {
                intfObj, _ = intfsObj.NewInterface(intfName)
            }
            ygot.BuildEmptyTree(intfObj)
            if intfObj.Subinterfaces == nil {
                ygot.BuildEmptyTree(intfObj.Subinterfaces)
            }
        } else {
             ygot.BuildEmptyTree(intfsObj)
             intfObj, _ = intfsObj.NewInterface(intfName)
             ygot.BuildEmptyTree(intfObj.Subinterfaces)
        }


    } else {
        err = errors.New("Invalid URI : " + targetUriPath)
    }
    err = handleIntfIPGetByTargetURI(inParams, targetUriPath, intfName, intfObj)

    return err
}

func validIPv4(ipAddress string) bool {
    ipAddress = strings.Trim(ipAddress, " ")

    re, _ := regexp.Compile(`^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$`)
    if re.MatchString(ipAddress) {
        return true
    }
    return false
}

func validIPv6(ip6Address string) bool {
    ip6Address = strings.Trim(ip6Address, " ")
    re, _ := regexp.Compile(`(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))`)
    if re.MatchString(ip6Address) {
        return true
    }
    return false
}

func doGetAllIpKeys(d *db.DB, dbSpec *db.TableSpec) ([]db.Key, error) {

    var keys []db.Key

    intfTable, err := d.GetTable(dbSpec)
    if err != nil {
        return keys, err
    }

    keys, err = intfTable.GetKeys()
    log.Infof("Found %d INTF table keys", len(keys))
    return keys, err
}

func getIntfTableNameByDBId (intftbl IntfTblData, curDb db.DBNum) (string, error) {

    var tblName string

    switch (curDb) {
    case db.ConfigDB:
        tblName = intftbl.cfgDb.intfTN
    case db.ApplDB:
        tblName = intftbl.appDb.intfTN
    case db.StateDB:
        tblName = intftbl.stateDb.intfTN
    default:
        tblName = intftbl.cfgDb.intfTN
    }

    return tblName, nil
}



func getIntfCountersTblKey (d *db.DB, ifKey string) (string, error) {
    var oid string

    portOidCountrTblTs := &db.TableSpec{Name: "COUNTERS_PORT_NAME_MAP"}
    ifCountInfo, err := d.GetMapAll(portOidCountrTblTs)
    if err != nil {
        log.Error("Port-OID (Counters) get for all the interfaces failed!")
        return oid, err
    }

    if ifCountInfo.IsPopulated() {
        _, ok := ifCountInfo.Field[ifKey]
        if !ok {
            err = errors.New("OID info not found from Counters DB for interface " + ifKey)
        } else {
            oid = ifCountInfo.Field[ifKey]
        }
    } else {
        err = errors.New("Get for OID info from all the interfaces from Counters DB failed!")
    }

    return oid, err
}

func getSpecificCounterAttr(targetUriPath string, entry *db.Value, counter_val *ocbinds.OpenconfigInterfaces_Interfaces_Interface_State_Counters) (bool, error) {

    var e error

    switch targetUriPath {
    case "/openconfig-interfaces:interfaces/interface/state/counters/in-octets":
        e = getCounters(entry, "SAI_PORT_STAT_IF_IN_OCTETS", &counter_val.InOctets)
        return true, e

    case "/openconfig-interfaces:interfaces/interface/state/counters/in-unicast-pkts":
        e = getCounters(entry, "SAI_PORT_STAT_IF_IN_UCAST_PKTS", &counter_val.InUnicastPkts)
        return true, e

    case "/openconfig-interfaces:interfaces/interface/state/counters/in-broadcast-pkts":
        e = getCounters(entry, "SAI_PORT_STAT_IF_IN_BROADCAST_PKTS", &counter_val.InBroadcastPkts)
        return true, e

    case "/openconfig-interfaces:interfaces/interface/state/counters/in-multicast-pkts":
        e = getCounters(entry, "SAI_PORT_STAT_IF_IN_MULTICAST_PKTS", &counter_val.InMulticastPkts)
        return true, e

    case "/openconfig-interfaces:interfaces/interface/state/counters/in-errors":
        e = getCounters(entry, "SAI_PORT_STAT_IF_IN_ERRORS", &counter_val.InErrors)
        return true, e

    case "/openconfig-interfaces:interfaces/interface/state/counters/in-discards":
        e = getCounters(entry, "SAI_PORT_STAT_IF_IN_DISCARDS", &counter_val.InDiscards)
        return true, e

    case "/openconfig-interfaces:interfaces/interface/state/counters/in-pkts":
        var inNonUCastPkt, inUCastPkt *uint64
        var in_pkts uint64

        e = getCounters(entry, "SAI_PORT_STAT_IF_IN_NON_UCAST_PKTS", &inNonUCastPkt)
        if e == nil {
            e = getCounters(entry, "SAI_PORT_STAT_IF_IN_UCAST_PKTS", &inUCastPkt)
            if e != nil {
                return true, e
            }
            in_pkts = *inUCastPkt + *inNonUCastPkt
            counter_val.InPkts = &in_pkts
            return true, e
        } else {
            return true, e
        }

    case "/openconfig-interfaces:interfaces/interface/state/counters/out-octets":
        e = getCounters(entry, "SAI_PORT_STAT_IF_OUT_OCTETS", &counter_val.OutOctets)
        return true, e

    case "/openconfig-interfaces:interfaces/interface/state/counters/out-unicast-pkts":
        e = getCounters(entry, "SAI_PORT_STAT_IF_OUT_UCAST_PKTS", &counter_val.OutUnicastPkts)
        return true, e

    case "/openconfig-interfaces:interfaces/interface/state/counters/out-broadcast-pkts":
        e = getCounters(entry, "SAI_PORT_STAT_IF_OUT_BROADCAST_PKTS", &counter_val.OutBroadcastPkts)
        return true, e

    case "/openconfig-interfaces:interfaces/interface/state/counters/out-multicast-pkts":
        e = getCounters(entry, "SAI_PORT_STAT_IF_OUT_MULTICAST_PKTS", &counter_val.OutMulticastPkts)
        return true, e

    case "/openconfig-interfaces:interfaces/interface/state/counters/out-errors":
        e = getCounters(entry, "SAI_PORT_STAT_IF_OUT_ERRORS", &counter_val.OutErrors)
        return true, e

    case "/openconfig-interfaces:interfaces/interface/state/counters/out-discards":
        e = getCounters(entry, "SAI_PORT_STAT_IF_OUT_DISCARDS", &counter_val.OutDiscards)
        return true, e

    case "/openconfig-interfaces:interfaces/interface/state/counters/out-pkts":
        var outNonUCastPkt, outUCastPkt *uint64
        var out_pkts uint64

        e = getCounters(entry, "SAI_PORT_STAT_IF_OUT_NON_UCAST_PKTS", &outNonUCastPkt)
        if e == nil {
            e = getCounters(entry, "SAI_PORT_STAT_IF_OUT_UCAST_PKTS", &outUCastPkt)
            if e != nil {
                return true, e
            }
            out_pkts = *outUCastPkt + *outNonUCastPkt
            counter_val.OutPkts = &out_pkts
            return true, e
        } else {
            return true, e
        }


    default:
        log.Infof(targetUriPath + " - Not an interface state counter attribute")
    }
    return false, nil
}

func getCounters(entry *db.Value, attr string, counter_val **uint64 ) error {

    var ok bool = false
    var val string
    var err error

    val, ok = entry.Field[attr]
    if !ok {
        return errors.New("Attr " + attr + "doesn't exist in IF table Map!")
    }

    if len(val) > 0 {
        v, e := strconv.ParseUint(val, 10, 64)
        if err == nil {
            *counter_val = &v
            return nil
        }
        err = e
    }
    return err
}

var portCntList [] string = []string {"in-octets", "in-unicast-pkts", "in-broadcast-pkts", "in-multicast-pkts",
"in-errors", "in-discards", "in-pkts", "out-octets", "out-unicast-pkts",
"out-broadcast-pkts", "out-multicast-pkts", "out-errors", "out-discards",
"out-pkts"}
var populatePortCounters PopulateIntfCounters = func (inParams XfmrParams, counter *ocbinds.OpenconfigInterfaces_Interfaces_Interface_State_Counters) (error) {

    pathInfo := NewPathInfo(inParams.uri)
    intfName := pathInfo.Var("name")
    targetUriPath, err := getYangPathFromUri(pathInfo.Path)

    log.Info("PopulateIntfCounters : inParams.curDb : ", inParams.curDb, "D: ", inParams.d, "DB index : ", inParams.dbs[inParams.curDb])
    oid, oiderr := getIntfCountersTblKey(inParams.dbs[inParams.curDb], intfName)
    if oiderr != nil {
        log.Info(oiderr)
        return oiderr
    }
    cntTs := &db.TableSpec{Name: "COUNTERS"}
    entry, dbErr := inParams.dbs[inParams.curDb].GetEntry(cntTs, db.Key{Comp: []string{oid}})
    if dbErr != nil {
        log.Info("PopulateIntfCounters : not able find the oid entry in DB Counters table")
        return dbErr
    }
    CounterData := entry

    switch (targetUriPath) {
    case "/openconfig-interfaces:interfaces/interface/state/counters":
        for _, attr := range portCntList {
            uri := targetUriPath + "/" + attr
            if ok, err := getSpecificCounterAttr(uri, &CounterData, counter); !ok || err != nil {
                log.Info("Get Counter URI failed :", uri)
                err = errors.New("Get Counter URI failed")
            }
        }
    default:
        _, err = getSpecificCounterAttr(targetUriPath, &CounterData, counter)
    }

    return err
}

var mgmtCounterIndexMap = map[string]int {
    "in-octets"            : 1,
    "in-pkts"              : 2,
    "in-errors"            : 3,
    "in-discards"          : 4,
    "in-multicast-pkts"    : 8,
    "out-octets"           : 9,
    "out-pkts"             : 10,
    "out-errors"           : 11,
    "out-discards"         : 12,
}

func getMgmtCounters(val string, counter_val **uint64 ) error {

    var err error
    if len(val) > 0 {
        v, e := strconv.ParseUint(val, 10, 64)
        if err == nil {
            *counter_val = &v
            return nil
        }
        err = e
    }
    return err
}
func getMgmtSpecificCounterAttr (uri string, cnt_data []string, counter *ocbinds.OpenconfigInterfaces_Interfaces_Interface_State_Counters) (error) {

    var e error
    switch (uri) {
    case "/openconfig-interfaces:interfaces/interface/state/counters/in-octets":
        e = getMgmtCounters(cnt_data[mgmtCounterIndexMap["in-octets"]], &counter.InOctets)
        return e
    case "/openconfig-interfaces:interfaces/interface/state/counters/in-pkts":
        e = getMgmtCounters(cnt_data[mgmtCounterIndexMap["in-pkts"]], &counter.InPkts)
        return  e
    case "/openconfig-interfaces:interfaces/interface/state/counters/in-errors":
        e = getMgmtCounters(cnt_data[mgmtCounterIndexMap["in-errors"]], &counter.InErrors)
        return  e
    case "/openconfig-interfaces:interfaces/interface/state/counters/in-discards":
        e = getMgmtCounters(cnt_data[mgmtCounterIndexMap["in-discards"]], &counter.InDiscards)
        return e
    case "/openconfig-interfaces:interfaces/interface/state/counters/in-multicast-pkts":
        e = getMgmtCounters(cnt_data[mgmtCounterIndexMap["in-multicast-pkts"]], &counter.InMulticastPkts)
        return e
    case "/openconfig-interfaces:interfaces/interface/state/counters/out-octets":
        e = getMgmtCounters(cnt_data[mgmtCounterIndexMap["out-octets"]], &counter.OutOctets)
        return e
    case "/openconfig-interfaces:interfaces/interface/state/counters/out-pkts":
        e = getMgmtCounters(cnt_data[mgmtCounterIndexMap["out-pkts"]], &counter.OutPkts)
        return e
    case "/openconfig-interfaces:interfaces/interface/state/counters/out-errors":
        e = getMgmtCounters(cnt_data[mgmtCounterIndexMap["out-errors"]], &counter.OutErrors)
        return e
    case "/openconfig-interfaces:interfaces/interface/state/counters/out-discards":
        e = getMgmtCounters(cnt_data[mgmtCounterIndexMap["out-discards"]], &counter.OutDiscards)
        return e
    case "/openconfig-interfaces:interfaces/interface/state/counters":
        for key := range mgmtCounterIndexMap {
            xuri := uri + "/" + key
            e = getMgmtSpecificCounterAttr(xuri, cnt_data, counter)
        }
        return  nil
    }

    log.Info("getMgmtSpecificCounterAttr - Invalid counters URI : ", uri)
    return errors.New("Invalid counters URI")

}

var populateMGMTPortCounters PopulateIntfCounters = func (inParams XfmrParams, counter *ocbinds.OpenconfigInterfaces_Interfaces_Interface_State_Counters) (error) {
    pathInfo := NewPathInfo(inParams.uri)
    intfName := pathInfo.Var("name")
    targetUriPath, err := getYangPathFromUri(pathInfo.Path)

    fileName := "/proc/net/dev"
    file, err := os.Open(fileName)
    if err != nil {
        log.Info("failed opening file: %s", err)
        return err
    }

    scanner := bufio.NewScanner(file)
    scanner.Split(bufio.ScanLines)
    var txtlines []string
    for scanner.Scan() {
        txtlines = append(txtlines, scanner.Text())
    }
    file.Close()
    var entry string
    for _, eachline := range txtlines {
        ln := strings.TrimSpace(eachline)
        if strings.HasPrefix(ln, intfName) {
            entry = ln
            log.Info(" Interface stats : ", entry)
            break
        }
    }

    if entry  == "" {
        log.Info("Counters not found for Interface " + intfName)
        return errors.New("Counters not found for Interface " + intfName)
    }

    stats := strings.Fields(entry)
    log.Info(" Interface filds: ", stats)

    ret := getMgmtSpecificCounterAttr(targetUriPath, stats, counter)
    log.Info(" getMgmtCounters : ", *counter)
    return ret
}

var YangToDb_intf_counters_key KeyXfmrYangToDb = func(inParams XfmrParams) (string, error) {
    var entry_key string
    var err error
    pathInfo := NewPathInfo(inParams.uri)
    intfName := pathInfo.Var("name")
    oid, oiderr := getIntfCountersTblKey(inParams.dbs[inParams.curDb], intfName)

    if oiderr == nil {
        entry_key = oid
    }
    return entry_key, err
}

var DbToYang_intf_counters_key KeyXfmrDbToYang = func(inParams XfmrParams) (map[string]interface{}, error) {
    rmap := make(map[string]interface{})
    var err error
    return rmap, err
}

var DbToYang_intf_get_counters_xfmr SubTreeXfmrDbToYang = func(inParams XfmrParams) error {
    var err error

    intfsObj := getIntfsRoot(inParams.ygRoot)
    pathInfo := NewPathInfo(inParams.uri)
    intfName := pathInfo.Var("name")

    targetUriPath, err := getYangPathFromUri(inParams.uri)
    log.Info("targetUriPath is ", targetUriPath)

    if  targetUriPath != "/openconfig-interfaces:interfaces/interface/state/counters" {
        log.Info("%s is redundant", targetUriPath)
        return err
    }

    intfType, _, ierr := getIntfTypeByName(intfName)
    if intfType == IntfTypeUnset || ierr != nil {
        log.Info("DbToYang_intf_get_counters_xfmr - Invalid interface type IntfTypeUnset");
        return errors.New("Invalid interface type IntfTypeUnset");
    }
    intTbl := IntfTypeTblMap[intfType]

    var state_counters * ocbinds.OpenconfigInterfaces_Interfaces_Interface_State_Counters

    if intfsObj != nil && intfsObj.Interface != nil && len(intfsObj.Interface) > 0 {
        var ok bool = false
        var intfObj *ocbinds.OpenconfigInterfaces_Interfaces_Interface
        if intfObj, ok = intfsObj.Interface[intfName]; !ok {
            intfObj, _ = intfsObj.NewInterface(intfName)
            ygot.BuildEmptyTree(intfObj)
        }
        ygot.BuildEmptyTree(intfObj)
        if intfObj.State == nil  ||  intfObj.State.Counters == nil {
            ygot.BuildEmptyTree(intfObj.State)
        }
        state_counters = intfObj.State.Counters
    } else {
        ygot.BuildEmptyTree(intfsObj)
        intfObj, _:= intfsObj.NewInterface(intfName)
        ygot.BuildEmptyTree(intfObj)
        state_counters = intfObj.State.Counters
    }

    err = intTbl.CountersHdl.PopulateCounters(inParams, state_counters)
    log.Info("DbToYang_intf_get_counters_xfmr - ", state_counters)

    return err
}

/* Validate whether LAG exists in DB */
func (app *IntfApp) validateLagExists(d *db.DB, lagName *string) error {
    if len(*lagName) == 0 {
        return errors.New("Length of Lag name is zero")
    }
    entry, err := d.GetEntry(app.lagD.lagTs, db.Key{Comp: []string{*lagName}})
    log.Info("Lag Entry found:", entry)
    if err != nil || !entry.IsPopulated() {
        errStr := "Invalid Lag:" + *lagName
        return errors.New(errStr)
    }
    return nil
}

/* For ethernet/config container attributes */
var YangToDb_intf_eth_port_aggregate_xfmr SubTreeXfmrYangToDb = func(inParams XfmrParams) (map[string]map[string]db.Value, error) {

    var err error

    var emptyMap = map[string]int{}

    intfsObj := getIntfsRoot(inParams.ygRoot)
    intfObj := intfsObj.Interface[ifName]

    if intfObj.Ethernet == nil {
        return emptyMap, err
    }

    if intfObj.Ethernet.Config == nil {
        log.Info("intf.Ethernet.Config == nil")
        return emptyMap, err
    }

    if intfObj.Ethernet.Config.AggregateId != nil {
        //return err

        /* Add entry to PORTCHANNEL_MEMBER TABLE */
        memMap := make(map[string]map[string]db.Value)
        var err error
        // Check --- err = app.validateLagExists(d, &lagStr)
        // Check --- if given iface already part of some PortChannel
        pathInfo := NewPathInfo(inParams.uri)
        log.Info("------------pathInfo is", pathInfo)
        ifName := pathInfo.Var("name")
        log.Info("------------ifName is", ifName)
        //lagId, _ := inParams.param.(*string)
        lagId := intfObj.Ethernet.Config.AggregateId
        lagStr := "PortChannel" + (*lagId)

        intfType, _, ierr := getIntfTypeByName(lagStr)
        if ierr != nil {
            errStr := "Invalid interface "
            log.Info("YangToDb_intf_eth_port_aggregate_xfmr : " + errStr)
            return memMap, errors.New(errStr)
        }
        log.Info("------------intfType is", intfType)
    //    intTbl := IntfTypeTblMap[intfType]
        tblName := "PORTCHANNEL_MEMBER" //getIntfTableNameByDBId(intTbl, inParams.curDb) //memTN:"PORTCHANNEL_MEMBER"
        log.Info("------------tblName is", tblName)
    /*
     xfmr_intf.go:1231] ------------pathInfo is&{/openconfig-interfaces:interfaces/interface[name=Ethernet40]/ethernet/config/aggregate-id /openconfig-interfaces:interfaces/interface{name}/ethernet/config/aggregate-id map[name:Ethernet40]}
     xfmr_intf.go:1233] ------------ifName isEthernet40
     xfmr_intf.go:1235] ------------lagId is1
     xfmr_intf.go:1237] ------------lagStr isPortChannel1
     xfmr_intf.go:1248] ------------intfType is4
     xfmr_intf.go:1251] ------------tblName isPORTCHANNEL_INTERFACE
    */

    /*
        memberPortEntryMap := make(map[string]string)
        memberPortEntry := db.Value{Field: memberPortEntryMap}
        memberPortEntry.Field["NULL"] = "NULL"

        if app.lagD.lagMembersTableMap[lagStr] == nil {
            app.lagD.lagMembersTableMap[lagStr] = make(map[string]dbEntry)
        }
        app.lagD.lagMembersTableMap[lagStr][*ifKey] = dbEntry{entry: memberPortEntry, op: opCreate}

    */
        m := make(map[string]string)
        value := db.Value{Field: m}
        m["NULL"] = "NULL"
        intfKey := lagStr + "|" + ifName
        log.Info("------------here---1---intfKey", intfKey)
        if _, ok := memMap[tblName]; !ok {
            memMap[tblName] = make(map[string]db.Value)
        }
        //memMap[tblName] = make(map[string]db.Value)
        log.Info("------------here----2--")
        //memMap[tblName][intfKey] =  db.Value{Field: make(map[string]string)}//value // "PORTCHANNEL_MEMBER|PortChannel2|Ethernet4"
        //memMap[tblName][intfKey] =  make(db.Value)
        memMap[tblName][intfKey] = value
        log.Info("------------here-----3-")
        //memMap[tblName][intfKey].Field["NULL"] = "NULL"
        return memMap, err
    }

    errStr := "Invalid attribute"
    log.Info("Not a supported config attribute")
    return emptyMap, errors.New(errStr)

}
