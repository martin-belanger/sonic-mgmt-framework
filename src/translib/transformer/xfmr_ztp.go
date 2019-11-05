package transformer

import (
    "strconv"
    "reflect"
    //"translib"
    //"strings"
    "github.com/openconfig/ygot/ygot"
    log "github.com/golang/glog"
    "translib/ocbinds"
    "encoding/json"
    "fmt"
)
/*App specific constants */
const (
    ZTP_STATUS_ADMIN_MODE            = "admin_mode"
    ZTP_STATUS_SERVICE               = "service"
    ZTP_STATUS_STATUS                = "status"
    ZTP_STATUS_SOURCE                = "source"
    ZTP_STATUS_RUNTIME               = "runtime"
    ZTP_STATUS_TIMESTAMP             = "timestamp"
    ZTP_STATUS_JSON_VERSION          = "json_version"
    ZTP_STATUS_ACTIVITY_STRING       = "activity_string"
    ZTP_CONFIG_SECTION_LIST          = "config_section_list"
    ZTP_CONFIG_SECTION_STATUS        = "cfg_status"
    ZTP_CONFIG_SECTION_NAME          = "cfg_sectionname"
    ZTP_CONFIG_SECTION_RUNTIME       = "cfg_runtime"
    ZTP_CONFIG_SECTION_TIMESTAMP     = "cfg_timestamp"
    ZTP_CONFIG_SECTION_EXITCODE      = "cfg_exitcode"
    ZTP_CONFIG_SECTION_IGNORE_RESULT = "cfg_ignoreresult"
    ZTP_STATUS_ERROR                 = "error"
)

/* App specific type definitions */

type ztpStatusCache struct {
    ztpStatusMap map[string]string
    ztpConfigSectionMap map[string]map[string]string
}

/* App specific utilities */

/* Initialise ZTP cache Data structure */

func ztpCacheInit(statusCache *ztpStatusCache) {
    statusCache.ztpStatusMap = make(map[string]string)
    statusCache.ztpConfigSectionMap= make(map[string]map[string]string)
}

/* Get ygot root object */

func getZtpRoot (s *ygot.GoStruct) (*ocbinds.OpenconfigZtp_Ztp) {
    deviceObj := (*s).(*ocbinds.Device)
    return deviceObj.Ztp
}

/* Wrapper to call host service to perform ZTP operations */

func ztpAction(action string) (string, error) {
	var output string
	// result.Body is of type []interface{}, since any data may be returned by
	// the host server. The application is responsible for performing
	// type assertions to get the correct data.
	result := hostQuery("ztp." + action)
	if result.Err != nil {
		return output, result.Err
	}
	if action == "status" {
		// ztp.status returns an exit code and the stdout of the command
		// We only care about the stdout (which is at [1] in the slice)
		output, _ = result.Body[1].(string)
	}
	return output, nil
}

/* Function to populate ztp status data structure with the status info from host service */

func getZtpStatusFromHost(statusCache * ztpStatusCache, hostData map[string] interface{}) {

    temp := hostData
    for attr,val := range temp {
	switch attr {
	    case ZTP_STATUS_ADMIN_MODE:
		statusCache.ztpStatusMap[ZTP_STATUS_ADMIN_MODE] = fmt.Sprintf("%t",val)
	    case ZTP_STATUS_SERVICE:
    		statusCache.ztpStatusMap[ZTP_STATUS_SERVICE] = fmt.Sprintf("%v",val)
	    case ZTP_STATUS_STATUS:
    		statusCache.ztpStatusMap[ZTP_STATUS_STATUS] = fmt.Sprintf("%v",val)
	    case ZTP_STATUS_SOURCE:
    		statusCache.ztpStatusMap[ZTP_STATUS_SOURCE] = fmt.Sprintf("%v",val)
	    case ZTP_STATUS_RUNTIME:
    		statusCache.ztpStatusMap[ZTP_STATUS_RUNTIME] = fmt.Sprintf("%v",val)
	    case ZTP_STATUS_TIMESTAMP:
    		statusCache.ztpStatusMap[ZTP_STATUS_TIMESTAMP] = fmt.Sprintf("%v",val)
	    case ZTP_STATUS_JSON_VERSION:
    		statusCache.ztpStatusMap[ZTP_STATUS_JSON_VERSION]= fmt.Sprintf("%v",val)
	    case ZTP_STATUS_ACTIVITY_STRING:
    		statusCache.ztpStatusMap[ZTP_STATUS_ACTIVITY_STRING] = fmt.Sprintf("%v",val)
	    case ZTP_STATUS_ERROR:
    		statusCache.ztpStatusMap[ZTP_STATUS_ERROR] = fmt.Sprintf("%v",val)
	    default:
		log.Info("Invalid attr:",attr)
	}
   }

}

/* Function to populate ztp status config section data structure with status info from host service */

func getConfigSection(sectionName string, dataMap map[string]interface{}, statusCache *ztpStatusCache) {
    statusCache.ztpConfigSectionMap[sectionName] = make(map[string]string)
    for attr,val := range dataMap {
	switch attr {
	    case ZTP_CONFIG_SECTION_NAME:
    		statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_NAME] = sectionName
	    case ZTP_CONFIG_SECTION_STATUS:
    		statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_STATUS]  = fmt.Sprintf("%v",val)
            case ZTP_CONFIG_SECTION_RUNTIME:
    		statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_RUNTIME] = fmt.Sprintf("%v",val)
	    case ZTP_CONFIG_SECTION_TIMESTAMP:
    		statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_TIMESTAMP] = fmt.Sprintf("%v",val)
	    case ZTP_CONFIG_SECTION_EXITCODE:
    		statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_EXITCODE]  = fmt.Sprintf("%d",val)
	    case ZTP_CONFIG_SECTION_IGNORE_RESULT:
                statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_IGNORE_RESULT] = fmt.Sprintf("%v",val)
	    case ZTP_STATUS_ERROR:
                statusCache.ztpConfigSectionMap[sectionName][ZTP_STATUS_ERROR] = fmt.Sprintf("%v",val)
	    default:
		log.Info("Invalid attr:",attr)
	}
    }
}

/* Populate ztp status ygot tree */

func populateStatusYgotTree(statusObj *ocbinds.OpenconfigZtp_Ztp_ZtpStatus, statusCache *ztpStatusCache) {
    act:= statusCache.ztpStatusMap[ZTP_STATUS_ACTIVITY_STRING]
    statusObj.ActivityString = &act
     admin := new(bool)
    *admin,_ =  strconv.ParseBool(statusCache.ztpStatusMap[ZTP_STATUS_ADMIN_MODE])
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
    er := statusCache.ztpStatusMap[ZTP_STATUS_ERROR]
    statusObj.Error =& er
}

/* Populate config section ygot tree */

func populateConfigSectionYgotTree(sectionName string, configObj *ocbinds.OpenconfigZtp_Ztp_ZtpStatus_CONFIG_SECTION_LIST, statusCache *ztpStatusCache) {
    ignr := true
    configObj.Ignoreresult =  &ignr
    rt := statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_RUNTIME]
    configObj.Runtime = &rt
    var  extc uint64
    extc,_ = strconv.ParseUint(statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_EXITCODE],10,64)
    configObj.Exitcode = &extc
    sec := statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_NAME]
    configObj.Sectionname = &sec
    st := statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_STATUS]
    configObj.Status = &st
    ts := statusCache.ztpConfigSectionMap[sectionName][ZTP_CONFIG_SECTION_TIMESTAMP]
    configObj.Timestamp = &ts
    er := statusCache.ztpConfigSectionMap[sectionName][ZTP_STATUS_ERROR]
    configObj.Error = &er
}

/* Get status info from db */

func getZtpStatusInfofromDb( statusObj *ocbinds.OpenconfigZtp_Ztp_ZtpStatus, statusCache *ztpStatusCache ) (error) {

    log.Info("Entered ztp status info from db")
    act:= "status"
    mess, err:= ztpAction(act)
    log.Info(" message from ztp host service:",mess)
    var empty map[string] interface{}
    err = json.Unmarshal([]byte (mess),&empty)
    if err != nil {
	log.Info("ztp json unmarshal error:",err)
    }
    log.Info("ztp unmarshal ds type:",reflect.TypeOf(empty))
    for k,v := range empty {
	log.Info("key:",k,"**","value:",v,"**typeofval:",reflect.TypeOf(v))
    }
    getZtpStatusFromHost(statusCache,empty)
    log.Info("Done populating cache map")
    populateStatusYgotTree(statusObj, statusCache)
    log.Info("Done populating status object")
    if allCfgList, present := empty[ZTP_CONFIG_SECTION_LIST]; present {
	    for section, dataMap := range allCfgList.(map[string]interface{}) {
                oneCfgList, err :=statusObj.NewCONFIG_SECTION_LIST(section)
	        if err != nil {
                    log.Info("Creation of subsectionlist subtree failed!")
                    return err
                }
                ygot.BuildEmptyTree(oneCfgList)
                getConfigSection(section, dataMap.(map[string]interface{}), statusCache)
	        log.Info("type of data map", reflect.TypeOf(dataMap))
                populateConfigSectionYgotTree(section, oneCfgList, statusCache)
                log.Info("Done populating config object for section:",section)
            }
        }
    return nil;
}

/* Wrapper to ztp status related function calls */

func getZtpStatus(ztpObj *ocbinds.OpenconfigZtp_Ztp) (error) {

    statusObj := ztpObj.ZtpStatus
    ygot.BuildEmptyTree(statusObj)
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
    act:= "enable"
    _, err = ztpAction(act)
    return err;

}
var DbToYang_ztp_disable_xfmr SubTreeXfmrDbToYang = func (inParams XfmrParams) (error) {

    log.Info("TableXfmrFunc - Uri ZTP: ", inParams.uri);
    pathInfo := NewPathInfo(inParams.uri)

    targetUriPath, err := getYangPathFromUri(pathInfo.Path)
    log.Info("TARGET URI PATH ZTP:", targetUriPath)
    act:= "disable"
    _, err = ztpAction(act)
    return err;
}


