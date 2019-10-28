package transformer

import (
    //"fmt"
    //"bytes"
    //"errors"
    //"strings"
    //"strconv"
    "reflect"
    //"regexp"
    //"net"
    //"translib/tlerr"
    "github.com/openconfig/ygot/ygot"
    //"translib/db"
    log "github.com/golang/glog"
    "translib/ocbinds"
    //"bufio"
    //"os"
    //"github.com/openconfig/ygot/ytypes"
)
const (
    ZTP_STATUS_ADMIN_MODE            = "admin_mode"
    ZTP_STATUS_SERVICE               = "service"
    ZTP_STATUS_STATUS                = "status"
    ZTP_STATUS_SOURCE                = "service"
    ZTP_STATUS_RUNTIME               = "runtime"
    ZTP_STATUS_TIMESTAMP             = "timestamp"
    ZTP_STATUS_JSON_VERSION          = "json_version"
    ZTP_STATUS_ACTIVITY_STRING       = "activity_string"
    ZTP_CONFIG_SECTION_STATUS        = "cfg_status"
    ZTP_CONFIG_SECTION_NAME          = "cfg_sectionname"
    ZTP_CONFIG_SECTION_RUNTIME       = "cfg_runtime"
    ZTP_CONFIG_SECTION_TIMESTAMP     = "cfg_timestamp"
    ZTP_CONFIG_SECTION_EXITCODE      = "cfg_exitcode"
    ZTP_CONFIG_SECTION_IGNORE_RESULT = "cfg_ignoreresult"

)
/* App specific type definitions */

type ztpStatusCache struct {
    ztpStatusMap map[string]string
    ztpConfigSectionMap map[string]map[string]string
}


/* App specific gloabl variables*/



/* App specific utilities */

func ztpCacheInit(statusCache *ztpStatusCache) {
    statusCache.ztpStatusMap = make(map[string]string)
    statusCache.ztpConfigSectionMap= make(map[string]map[string]string)
}

func getZtpRoot (s *ygot.GoStruct) (*ocbinds.OpenconfigZtp_Ztp) {
    deviceObj := (*s).(*ocbinds.Device)
    return deviceObj.Ztp
}

func getZtpStatusFromHost(statusCache * ztpStatusCache) {

    statusCache.ztpStatusMap[ZTP_STATUS_ADMIN_MODE] = "true"
    statusCache.ztpStatusMap[ZTP_STATUS_SERVICE] = "Inactive"
    statusCache.ztpStatusMap[ZTP_STATUS_STATUS] = "SUCCESS"
    statusCache.ztpStatusMap[ZTP_STATUS_SOURCE] = "dhcp-opt67 (eth0)"
    statusCache.ztpStatusMap[ZTP_STATUS_RUNTIME] = "05m 31s"
    statusCache.ztpStatusMap[ZTP_STATUS_TIMESTAMP] = "2019-09-11 19:12:24 UTC"
    statusCache.ztpStatusMap[ZTP_STATUS_JSON_VERSION]= "1.0"
    statusCache.ztpStatusMap[ZTP_STATUS_ACTIVITY_STRING] = "ZTP Service is not running"

}
func getConfigSection(sectionName string, oneCfgSection *ocbinds.OpenconfigZtp_Ztp_ZtpStatus_CONFIG_SECTION_LIST, statusCache *ztpStatusCache) {
    statusCache.ztpConfigSectionMap[sectionName] = make(map[string]string)
    statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_NAME]          = sectionName
    statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_STATUS]        = "SUCCESS"
    statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_RUNTIME]       = "03m 59s"
    statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_TIMESTAMP]     = "2019-09-11 19:12:24 UTC"
    statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_EXITCODE]      = "0"
    statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_IGNORE_RESULT] = "true"
}
func populateStatusYgotTree(statusObj *ocbinds.OpenconfigZtp_Ztp_ZtpStatus, statusCache *ztpStatusCache) {
    act:= statusCache.ztpStatusMap[ZTP_STATUS_ACTIVITY_STRING]
    statusObj.ActivityString = &act
     admin := new(bool)
    *admin =  true
    statusObj.AdminMode =  admin
    jsv := statusCache.ztpStatusMap[ZTP_STATUS_JSON_VERSION]
    statusObj.Jsonversion =& jsv
    rt := statusCache.ztpStatusMap[ZTP_STATUS_RUNTIME]
    statusObj.Runtime =  & rt
    serv := statusCache.ztpStatusMap[ZTP_STATUS_SERVICE]
    statusObj.Service = & serv
    src := statusCache.ztpStatusMap[ZTP_STATUS_SOURCE]
    statusObj.Source =  & src
    sts := statusCache.ztpStatusMap[ZTP_STATUS_STATUS]
    statusObj.Status = & sts
    tst := statusCache.ztpStatusMap[ZTP_STATUS_TIMESTAMP]
    statusObj.Timestamp =& tst
}

func populateConfigSectionYgotTree(sectionName string, configObj *ocbinds.OpenconfigZtp_Ztp_ZtpStatus_CONFIG_SECTION_LIST, statusCache *ztpStatusCache) {
    ignr := true
    configObj.Ignoreresult =  &ignr
    rt := statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_RUNTIME]
    configObj.Runtime = &rt
    //extc ,_ := strconv.ParseUint(statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_EXITCODE],10,32)
    var  extc uint32 
    extc = 0
    configObj.Exitcode = &extc
    sec := statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_NAME]
    configObj.Sectionname = &sec
    st := statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_STATUS]
    configObj.Status = &st
    //rt := statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_RUNTIME]
    //configObj.Runtime = &rt
    ts := statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_TIMESTAMP]
    configObj.Timestamp = &ts
}


func getZtpStatusInfofromDb( statusObj *ocbinds.OpenconfigZtp_Ztp_ZtpStatus, statusCache *ztpStatusCache ) (error) {

    log.Info("Entered ztp status info from db")
    getZtpStatusFromHost(statusCache)
    log.Info("Done populating cache map")
    populateStatusYgotTree(statusObj, statusCache)
    log.Info("Done populating status object")
    section := []string{"Config-db-json","connectivity-check"}
    log.Info("ZTP",section[0],section[1])
    for i := 0; i < 2; i++ {
        oneCfgList, err :=statusObj.NewCONFIG_SECTION_LIST(section[i])
	if err != nil {
                log.Info("Creation of subsectionlist subtree failed!")
                return err
            }
            ygot.BuildEmptyTree(oneCfgList)
            getConfigSection(section[i], oneCfgList, statusCache)
	    log.Info("Done populating config section cache map")
            populateConfigSectionYgotTree(section[i],oneCfgList, statusCache)
            log.Info("Done populating config object for section:",section[i])
    }
    return nil;
}

func getZtpStatus(ztpObj *ocbinds.OpenconfigZtp_Ztp) (error) {

    statusObj := ztpObj.ZtpStatus
    if  statusObj != nil {
       log.Info("ztp status obj not nil")
    }else  {
        log.Info("ztp status obj is nil")
    }
    ygot.BuildEmptyTree(statusObj)
    log.Info("type of ZTP-status OBJECT:",reflect.TypeOf(statusObj))
    var statusCache ztpStatusCache
    ztpCacheInit(&statusCache)
    log.Info("ZTP cache init done")
    err :=  getZtpStatusInfofromDb(statusObj, &statusCache)
    log.Info("done getztp status info from func() ZTP: ", err);
    return err
}



/* Transformer specific functions */

func init () {
    XlateFuncBind("DbToYang_ztp_status_xfmr", DbToYang_ztp_status_xfmr)
    XlateFuncBind("DbToYang_ztp_enable_xfmr", DbToYang_ztp_enable_xfmr)
    XlateFuncBind("DbToYang_ztp_disable_xfmr",DbToYang_ztp_disable_xfmr)

}


var DbToYang_ztp_status_xfmr SubTreeXfmrDbToYang = func (inParams XfmrParams) (error) {

    ztpObj := getZtpRoot(inParams.ygRoot)
    pathInfo := NewPathInfo(inParams.uri)
    targetUriPath, err := getYangPathFromUri(pathInfo.Path)
    if targetUriPath == "/openconfig-ztp:ztp/ztp-status" {
	log.Info("TARGET URI PATH ZTP:", targetUriPath)
        log.Info("TableXfmrFunc - Uri ZTP: ", inParams.uri);
        log.Info("type of ZTP-ROOT OBJECT:",reflect.TypeOf(ztpObj))
        err =  getZtpStatus(ztpObj)
	return err
    } else {
	return nil
    }
}


var DbToYang_ztp_enable_xfmr SubTreeXfmrDbToYang = func (inParams XfmrParams) (error) {

    log.Info("TableXfmrFunc - Uri ZTP: ", inParams.uri);
    pathInfo := NewPathInfo(inParams.uri)

    targetUriPath, err := getYangPathFromUri(pathInfo.Path)
    log.Info("TARGET URI PATH ZTP:", targetUriPath)
    return err;

}
var DbToYang_ztp_disable_xfmr SubTreeXfmrDbToYang = func (inParams XfmrParams) (error) {

    log.Info("TableXfmrFunc - Uri ZTP: ", inParams.uri);
    pathInfo := NewPathInfo(inParams.uri)

    targetUriPath, err := getYangPathFromUri(pathInfo.Path)
    log.Info("TARGET URI PATH ZTP:", targetUriPath)
    return err;

}


