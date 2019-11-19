package transformer

import (
    "errors"
    "strconv"
    "strings"
    "github.com/openconfig/ygot/ygot"
    "translib/db"
    log "github.com/golang/glog"
    "translib/ocbinds"
)

var queueCntList [] string = []string {/* Unsupported: "max-queue-len", "avg-queue-len",*/ "transmit-pkts", "transmit-octets", "dropped-pkts", "dropped-octets"}


func init () {
    XlateFuncBind("DbToYang_qos_get_one_intf_one_q_counters_xfmr", DbToYang_qos_get_one_intf_one_q_counters_xfmr)
    XlateFuncBind("DbToYang_qos_get_one_intf_all_q_counters_xfmr", DbToYang_qos_get_one_intf_all_q_counters_xfmr)
    XlateFuncBind("DbToYang_qos_get_all_intf_all_q_counters_xfmr", DbToYang_qos_get_all_intf_all_q_counters_xfmr)
}


type PopulateQueueCounters func (inParams XfmrParams, uri string, oid string, counters *ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Output_Queues_Queue_State) (error)

func getQosRoot (s *ygot.GoStruct) *ocbinds.OpenconfigQos_Qos {
    deviceObj := (*s).(*ocbinds.Device)
    return deviceObj.Qos
}

func getQosIntfRoot (s *ygot.GoStruct) *ocbinds.OpenconfigQos_Qos_Interfaces {
    deviceObj := (*s).(*ocbinds.Device)
    return deviceObj.Qos.Interfaces
}

var YangToDb_qos_name_xfmr FieldXfmrYangToDb = func(inParams XfmrParams) (map[string]string, error) {
    res_map := make(map[string]string)
    var err error
    return res_map, err
}

var DbToYang_qos_name_xfmr FieldXfmrDbtoYang = func(inParams XfmrParams) (map[string]interface{}, error) {
    var err error
    res_map := make(map[string]interface{})
    res_map["name"] =  inParams.key
    return res_map, err
}

func doGetAllQueueOidMap(d *db.DB) (db.Value, error) {

    // COUNTERS_QUEUE_NAME_MAP
    dbSpec := &db.TableSpec{Name: "COUNTERS_QUEUE_NAME_MAP"}
    queueOidMap, err := d.GetMapAll(dbSpec)
    if err != nil {
        log.Info("queueOidMap get failed")
    }

    log.Info("queueOidMap: ", queueOidMap)
    return queueOidMap, err
}


func getIntfQCountersTblKey (d *db.DB, ifQKey string) (string, error) {
    var oid string
    var err error

    queueOidMap, _ := doGetAllQueueOidMap(d);

    if queueOidMap.IsPopulated() {
        _, ok := queueOidMap.Field[ifQKey]
        if !ok {
            err = errors.New("OID info not found from Counters DB for interface queue: " + ifQKey)
        } else {
            oid = queueOidMap.Field[ifQKey]
        }
    } else {
        err = errors.New("Get for OID info from all the interfaces queues from Counters DB failed!")
    }

    return oid, err
}


func getCounters(entry *db.Value, attr string, counter_val **uint64 ) error {

    var ok bool = false
    var val string
    var err error

    val, ok = entry.Field[attr]
    if !ok {
        return errors.New("Attr " + attr + "doesn't exist in Queue table Map!")
    }

    if len(val) > -1 {
        v, e := strconv.ParseUint(val, 10, 64)
        if err == nil {
            *counter_val = &v
            return nil
        }
        err = e
    }
    return err
}


func getQueueSpecificCounterAttr(targetUriPath string, entry *db.Value, counters *ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Output_Queues_Queue_State) (bool, error) {

    var e error

    switch targetUriPath {
    /* Not supported in SONIC
    case "/openconfig-qos:qos/interfaces/interface/output/queues/queue/state/max-queue-len":
        e = getCounters(entry, "SAI_QUEUE_STAT_PACKETS", &counters.MaxQueueLen)
        return true, e

    case "/openconfig-qos:qos/interfaces/interface/output/queues/queue/state/avg-queue-len":
        e = getCounters(entry, "SAI_QUEUE_STAT_PACKETS", &counters.AvgQueueLen)
        return true, e
    */

    case "/openconfig-qos:qos/interfaces/interface/output/queues/queue/state/transmit-pkts":
        e = getCounters(entry, "SAI_QUEUE_STAT_PACKETS", &counters.TransmitPkts)
        return true, e

    case "/openconfig-qos:qos/interfaces/interface/output/queues/queue/state/transmit-octets":
        e = getCounters(entry, "SAI_QUEUE_STAT_BYTES", &counters.TransmitOctets)
        return true, e

    case "/openconfig-qos:qos/interfaces/interface/output/queues/queue/state/dropped-pkts":
        e = getCounters(entry, "SAI_QUEUE_STAT_DROPPED_PACKETS", &counters.DroppedPkts)
        return true, e

    case "/openconfig-qos:qos/interfaces/interface/output/queues/queue/state/dropped-octets":
        e = getCounters(entry, "SAI_QUEUE_STAT_DROPPED_BYTES", &counters.DroppedOctets)
        return true, e

    default:
        log.Infof(targetUriPath + " - Not an interface state counter attribute or unsupported")
    }
    return false, nil
}

var populateQCounters PopulateQueueCounters = func (inParams XfmrParams, targetUriPath string, oid string, counter *ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Output_Queues_Queue_State) (error) {

    log.Info("PopulateQueueCounters : inParams.curDb : ", inParams.curDb, " D: ", inParams.d, "DB index : ", inParams.dbs[inParams.curDb])

    cntTs := &db.TableSpec{Name: "COUNTERS"}
    entry, dbErr := inParams.dbs[inParams.curDb].GetEntry(cntTs, db.Key{Comp: []string{oid}})
    if dbErr != nil {
        log.Info("PopulateQueueCounters : not able to find the oid entry in DB Counters table")
        return dbErr
    }

    log.Info("targetUriPath is : ", targetUriPath)

    var err error

    switch (targetUriPath) {
    case "/openconfig-qos:qos/interfaces/interface/output/queues/queue/state":
        log.Info("Entering queue-state table")
        for _, attr := range queueCntList {
            uri := targetUriPath + "/" + attr
            if ok, err := getQueueSpecificCounterAttr(uri, &entry, counter); !ok || err != nil {
                log.Info("Get Counter URI failed :", uri)
                err = errors.New("Get Counter URI failed")
            }
        }
    default:
        log.Info("Entering default branch")
        _, err = getQueueSpecificCounterAttr(targetUriPath, &entry, counter)
    }

    return err
}

var YangToDb_qos_q_counters_key KeyXfmrYangToDb = func(inParams XfmrParams) (string, error) {
    var entry_key string
    var err error
    pathInfo := NewPathInfo(inParams.uri)
    intfName := pathInfo.Var("interface-id")
    queueName := pathInfo.Var("name")

    intfQName := intfName + ":" + queueName

    oid, oiderr := getIntfQCountersTblKey(inParams.dbs[inParams.curDb], intfQName)

    if oiderr == nil {
        entry_key = oid
    }
    return entry_key, err
}

var DbToYang_qos_q_counters_key KeyXfmrDbToYang = func(inParams XfmrParams) (map[string]interface{}, error) {
    rmap := make(map[string]interface{})
    var err error
    return rmap, err
}


var DbToYang_qos_get_one_intf_one_q_counters_xfmr SubTreeXfmrDbToYang = func(inParams XfmrParams) error {
    var err error

    qosIntfsObj := getQosIntfRoot(inParams.ygRoot)
    pathInfo := NewPathInfo(inParams.uri)
    intfName := pathInfo.Var("interface-id")
    queueName := pathInfo.Var("name")

    targetUriPath, err := getYangPathFromUri(inParams.uri)
    log.Info("targetUriPath is ", targetUriPath)

    if  targetUriPath != "/openconfig-qos:qos/interfaces/interface/output/queues/queue/state" {
        log.Info("%s is redundant", targetUriPath)
        return err
    }

    var state_counters * ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Output_Queues_Queue_State

    if qosIntfsObj != nil && qosIntfsObj.Interface != nil && len(qosIntfsObj.Interface) > 0 {
        var queuesObj *ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Output_Queues
        queuesObj = qosIntfsObj.Interface[intfName].Output.Queues

        var queueObj *ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Output_Queues_Queue
        if queuesObj != nil {
            queueObj = queuesObj.Queue[queueName]
        }
        state_counters = queueObj.State
    }

    if state_counters == nil  {
        log.Info("DbToYang_qos_get_one_intf_one_q_counters_xfmr - state_counters is nil")
        return err
    }

    state_counters.Name = &queueName

    oid, err := getIntfQCountersTblKey(inParams.dbs[inParams.curDb], intfName+":"+queueName)
    if err != nil {
        log.Info(err)
        return err 
    }
    
    err = populateQCounters(inParams, targetUriPath, oid, state_counters)

    log.Info("DbToYang_qos_get_one_intf_one_q_counters_xfmr - finished ")

    return err
}

var DbToYang_qos_get_one_intf_all_q_counters_xfmr SubTreeXfmrDbToYang = func(inParams XfmrParams) error {
    var err error

    log.Info("DbToYang_qos_get_one_intf_all_q_counters_xfmr - started ")


    qosIntfsObj := getQosIntfRoot(inParams.ygRoot)
    pathInfo := NewPathInfo(inParams.uri)
    intfName := pathInfo.Var("interface-id")

    targetUriPath, err := getYangPathFromUri(inParams.uri)
    if  targetUriPath != "/openconfig-qos:qos/interfaces/interface/output/queues" {
        log.Info("unexpected uri path: ", targetUriPath)
        return err
    }
    targetUriPath = targetUriPath + "/queue/state"
    log.Info("targetUriPath is ", targetUriPath)


    var queuesObj *ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Output_Queues
    if qosIntfsObj != nil && qosIntfsObj.Interface != nil && len(qosIntfsObj.Interface) > 0 {
        queuesObj = qosIntfsObj.Interface[intfName].Output.Queues
    }

    queueOidMap, _ := doGetAllQueueOidMap(inParams.dbs[inParams.curDb]);

    queueOidMapFields := queueOidMap.Field

    for keyString, oid := range queueOidMapFields {
        s := strings.Split(keyString, ":")
       
        ifName := s[0]
        queueName := s[1]
        
        if ifName == "" {
            continue
        }
        if queueName == "" {
            continue
        }

        if strings.Compare(ifName, intfName) != 0  {
            continue
        }

        if queuesObj == nil {
            ygot.BuildEmptyTree(queuesObj)
        }

        queueObj, _ := queuesObj.NewQueue(queueName)
        ygot.BuildEmptyTree(queueObj)

        queueObj.Name = &queueName
        if queueObj.State == nil {
            ygot.BuildEmptyTree(queueObj.State)
        }

        var state_counters * ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Output_Queues_Queue_State
        state_counters = queueObj.State

        if state_counters == nil  {
            log.Info("DbToYang_qos_get_intf_all_q_counters_xfmr - state_counters is nil")
	        return err
        }

        state_counters.Name = &queueName

        err = populateQCounters(inParams, targetUriPath, oid, state_counters)

    }

    log.Info("DbToYang_qos_get_intf_all_q_counters_xfmr - finished ")

    return err
}

var DbToYang_qos_get_all_intf_all_q_counters_xfmr SubTreeXfmrDbToYang = func(inParams XfmrParams) error {
    var err error

    log.Info("DbToYang_qos_get_all_intf_all_q_counters_xfmr - started ")


    qosIntfsObj := getQosIntfRoot(inParams.ygRoot)
    //pathInfo := NewPathInfo(inParams.uri)

    targetUriPath, err := getYangPathFromUri(inParams.uri)
    if  targetUriPath != "/openconfig-qos:qos/interfaces" {
        log.Info("unexpected uri path: ", targetUriPath)
        return err
    }
    targetUriPath = targetUriPath + "/interface/output/queues/queue/state"
    log.Info("targetUriPath is ", targetUriPath)


    queueOidMap, _ := doGetAllQueueOidMap(inParams.dbs[inParams.curDb]);

    queueOidMapFields := queueOidMap.Field

    // For faster processing, the result is not sorted here. 
    for keyString, oid := range queueOidMapFields {
        s := strings.Split(keyString, ":")
       
        intfName := s[0]
        queueName := s[1]
        
        if intfName == "" {
            continue
        }
        if queueName == "" {
            continue
        }

        log.Info("Get intf queue info of ", intfName, ":", queueName)

        if qosIntfsObj == nil {
            ygot.BuildEmptyTree(qosIntfsObj)
        }

        intfObj, ok := qosIntfsObj.Interface[intfName]
        if !ok {
            intfObj, _ = qosIntfsObj.NewInterface(intfName)
            ygot.BuildEmptyTree(intfObj)
            intfObj.InterfaceId = &intfName

            if intfObj.Output == nil {
                ygot.BuildEmptyTree(intfObj.Output)
            }
        }

        queuesObj := intfObj.Output.Queues
        if queuesObj == nil {
            ygot.BuildEmptyTree(queuesObj)
        }

        queueObj, _ := queuesObj.NewQueue(queueName)
        ygot.BuildEmptyTree(queueObj)

        log.Info("Get intf/queue info for: ", intfName, ":", queueName)

        queueObj.Name = &queueName
        if queueObj.State == nil {
            ygot.BuildEmptyTree(queueObj.State)
        }

        var state_counters * ocbinds.OpenconfigQos_Qos_Interfaces_Interface_Output_Queues_Queue_State
        state_counters = queueObj.State

        if state_counters == nil  {
            log.Info("DbToYang_qos_get_all_intf_all_q_counters_xfmr - state_counters is nil")
	        return err
        }

        state_counters.Name = &queueName
        log.Info("Get queue info of queueName:III ", queueName)

        
        err = populateQCounters(inParams, targetUriPath, oid, state_counters)
        log.Info("Get queue info of queueName:IV ", queueName)

    }

    log.Info("DbToYang_qos_get_all_intf_all_q_counters_xfmr - finished ")

    return err
}


