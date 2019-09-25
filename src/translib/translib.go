////////////////////////////////////////////////////////////////////////////////
//                                                                            //
//  Copyright 2019 Broadcom. The term Broadcom refers to Broadcom Inc. and/or //
//  its subsidiaries.                                                         //
//                                                                            //
//  Licensed under the Apache License, Version 2.0 (the "License");           //
//  you may not use this file except in compliance with the License.          //
//  You may obtain a copy of the License at                                   //
//                                                                            //
//     http://www.apache.org/licenses/LICENSE-2.0                             //
//                                                                            //
//  Unless required by applicable law or agreed to in writing, software       //
//  distributed under the License is distributed on an "AS IS" BASIS,         //
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  //  
//  See the License for the specific language governing permissions and       //
//  limitations under the License.                                            //
//                                                                            //
////////////////////////////////////////////////////////////////////////////////

/*
Package translib implements APIs like Create, Get, Subscribe etc.

to be consumed by the north bound management server implementations

This package take care of translating the incoming requests to 

Redis ABNF format and persisting them in the Redis DB.

It can also translate the ABNF format to YANG specific JSON IETF format

This package can also talk to non-DB clients.
*/

package translib

import (
		//"errors"
		"sync"
		"translib/db"
        "github.com/Workiva/go-datastructures/queue"
        log "github.com/golang/glog"
		"translib/tlerr"
)

//Write lock for all write operations to be synchronized
var writeMutex = &sync.Mutex{}

//minimum global interval for subscribe in secs
var minSubsInterval = 20
var maxSubsInterval = 60

type ErrSource int

const(
	ProtoErr ErrSource = iota
	AppErr
)

type SetRequest struct{
    Path       string
    Payload    []byte
}

type SetResponse struct{
	ErrSrc     ErrSource
}

type GetRequest struct{
    Path       string
}

type GetResponse struct{
    Payload    []byte
	ErrSrc     ErrSource
}

type SubscribeResponse struct{
	Path		 string
	Payload      []byte
	Timestamp	 int64
	SyncComplete bool
	IsTerminated bool
}

type NotificationType int

const(
    Sample	NotificationType = iota
    OnChange
)

type IsSubscribeResponse struct{
	Path					string
	IsOnChangeSupported		bool
	MinInterval				int
	Err						error
	PreferredType			NotificationType
}

type ModelData struct{
	Name      string
	Org		  string
	Ver		  string
}

type notificationOpts struct {
    mInterval		int
    pType			NotificationType  // for TARGET_DEFINED
}

//initializes logging and app modules
func init() {
    log.Flush()
}

//Creates entries in the redis DB pertaining to the path and payload
func Create(req SetRequest) (SetResponse, error){
	var keys []db.WatchKeys
	var resp SetResponse

	path	:= req.Path
    payload := req.Payload

    log.Info("Create request received with path =", path)
    log.Info("Create request received with payload =", string(payload))

	app, appInfo, err := getAppModule(path)

	if err != nil {
		resp.ErrSrc = ProtoErr
        return resp, err
	}

    err = appInitialize(app, appInfo, path, &payload, CREATE)

    if  err != nil {
		resp.ErrSrc = AppErr
		return resp, err
    }

	writeMutex.Lock()
	defer writeMutex.Unlock()

	d, err := db.NewDB(getDBOptions(db.ConfigDB))

	if err != nil {
		resp.ErrSrc = ProtoErr
		return resp, err
	}

	defer d.DeleteDB()

    keys, err = (*app).translateCreate(d)

	if err != nil {
		resp.ErrSrc = AppErr
        return resp, err
	}

	err = d.StartTx(keys, appInfo.tablesToWatch)

	if err != nil {
		resp.ErrSrc = AppErr
        return resp, err
	}

    resp, err = (*app).processCreate (d)

    if err != nil {
		d.AbortTx()
		resp.ErrSrc = AppErr
        return resp, err
    }

	err = d.CommitTx()

    if err != nil {
        resp.ErrSrc = AppErr
    }

    return resp, err
}

//Updates entries in the redis DB pertaining to the path and payload
func Update(req SetRequest) (SetResponse, error){
    var keys []db.WatchKeys
	var resp SetResponse

    path    := req.Path
    payload := req.Payload

    log.Info("Update request received with path =", path)
    log.Info("Update request received with payload =", string(payload))

	app, appInfo, err := getAppModule(path)

    if err != nil {
		resp.ErrSrc = ProtoErr
        return resp, err
    }

    err = appInitialize(app, appInfo, path, &payload, UPDATE)

    if  err != nil {
        resp.ErrSrc = AppErr
        return resp, err
    }

    writeMutex.Lock()
	defer writeMutex.Unlock()

    d, err := db.NewDB(getDBOptions(db.ConfigDB))

    if err != nil {
        resp.ErrSrc = ProtoErr
        return resp, err
    }

	defer d.DeleteDB()

    keys, err = (*app).translateUpdate(d)

    if err != nil {
		resp.ErrSrc = AppErr
        return resp, err
    }

    err = d.StartTx(keys, appInfo.tablesToWatch)

    if err != nil {
		resp.ErrSrc = AppErr
        return resp, err
    }

    resp, err = (*app).processUpdate (d)

    if err != nil {
        d.AbortTx()
		resp.ErrSrc = AppErr
        return resp, err
    }

    err = d.CommitTx()

    if err != nil {
        resp.ErrSrc = AppErr
    }

    return resp, err
}

//Replaces entries in the redis DB pertaining to the path and payload
func Replace(req SetRequest) (SetResponse, error){
    var err error
    var keys []db.WatchKeys
	var resp SetResponse

    path    := req.Path
    payload := req.Payload

    log.Info("Replace request received with path =", path)
    log.Info("Replace request received with payload =", string(payload))

	app, appInfo, err := getAppModule(path)

    if err != nil {
		resp.ErrSrc = ProtoErr
        return resp, err
    }

    err = appInitialize(app, appInfo, path, &payload, REPLACE)

    if  err != nil {
        resp.ErrSrc = AppErr
        return resp, err
    }

    writeMutex.Lock()
	defer writeMutex.Unlock()

    d, err := db.NewDB(getDBOptions(db.ConfigDB))

    if err != nil {
        resp.ErrSrc = ProtoErr
        return resp, err
    }

	defer d.DeleteDB()

    keys, err = (*app).translateReplace(d)

    if err != nil {
		resp.ErrSrc = AppErr
        return resp, err
    }

    err = d.StartTx(keys, appInfo.tablesToWatch)

    if err != nil {
		resp.ErrSrc = AppErr
        return resp, err
    }

    resp, err = (*app).processReplace (d)

    if err != nil {
        d.AbortTx()
		resp.ErrSrc = AppErr
        return resp, err
    }

    err = d.CommitTx()

	if err != nil {
		resp.ErrSrc = AppErr
    }

    return resp, err
}

//Deletes entries in the redis DB pertaining to the path
func Delete(req SetRequest) (SetResponse, error){
    var err error
    var keys []db.WatchKeys
	var resp SetResponse

    path    := req.Path

    log.Info("Delete request received with path =", path)

	app, appInfo, err := getAppModule(path)

    if err != nil {
		resp.ErrSrc = ProtoErr
        return resp, err
    }

    err = appInitialize(app, appInfo, path, nil, DELETE)

    if  err != nil {
        resp.ErrSrc = AppErr
        return resp, err
    }

    writeMutex.Lock()
	defer writeMutex.Unlock()

    d, err := db.NewDB(getDBOptions(db.ConfigDB))

    if err != nil {
        resp.ErrSrc = ProtoErr
        return resp, err
    }

	defer d.DeleteDB()

    keys, err = (*app).translateDelete(d)

    if err != nil {
		resp.ErrSrc = AppErr
        return resp, err
    }

    err = d.StartTx(keys, appInfo.tablesToWatch)

    if err != nil {
		resp.ErrSrc = AppErr
        return resp, err
    }

    resp, err = (*app).processDelete(d)

    if err != nil {
        d.AbortTx()
		resp.ErrSrc = AppErr
        return resp, err
    }

    err = d.CommitTx()

    if err != nil {
        resp.ErrSrc = AppErr
    }

	return resp, err
}

//Gets data from the redis DB and converts it to northbound format
func Get(req GetRequest) (GetResponse, error){
    var payload []byte
	var resp GetResponse

	path := req.Path

    log.Info("Received Get request for path = ",path)

	app, appInfo, err := getAppModule(path)

    if err != nil {
        resp = GetResponse{Payload:payload, ErrSrc:ProtoErr}
        return resp, err
    }

	err = appInitialize(app, appInfo, path, nil, GET)

	if  err != nil {
		resp = GetResponse{Payload:payload, ErrSrc:AppErr}
		return resp, err
	}

	dbs, err := getAllDbs()

	if err != nil {
		resp = GetResponse{Payload:payload, ErrSrc:ProtoErr}
        return resp, err
	}

	defer closeAllDbs(dbs[:])

        err = (*app).translateGet (dbs)

	if err != nil {
		resp = GetResponse{Payload:payload, ErrSrc:AppErr}
        return resp, err
	}

    resp, err = (*app).processGet(dbs)

    return resp, err
}

//Subscribes to the paths requested and sends notifications when the data changes in DB
func Subscribe(paths []string, q *queue.PriorityQueue, stop chan struct{}) ([]*IsSubscribeResponse, error) {
    var err error
	var sErr error
	//err = errors.New("Not implemented")

	dbNotificationMap := make(map[db.DBNum][]*notificationInfo)

	resp := make ([]*IsSubscribeResponse, len(paths))

    for i, _ := range resp {
        resp[i] = &IsSubscribeResponse{Path: paths[i],
                                IsOnChangeSupported: false,
                                MinInterval: minSubsInterval,
								PreferredType:Sample,
								Err:nil}
    }

	dbs, err := getAllDbs()

    if err != nil {
        return resp, err
    }

	//Do NOT close the DBs here as we need to use them during subscribe notification

    for i, path := range paths {

		app, appInfo, err := getAppModule(path)

        if err != nil {

            if sErr == nil {
				sErr = err
			}

			resp[i].Err = err
			continue
        }

        nOpts, nInfo, errApp := (*app).translateSubscribe (dbs, path)

        if errApp != nil {
            resp[i].Err = errApp

			if sErr == nil {
				sErr = errApp
			}

			resp[i].MinInterval = maxSubsInterval

            if nOpts != nil {
                if nOpts.mInterval != 0 {
                    resp[i].MinInterval = nOpts.mInterval
                }

                resp[i].PreferredType = nOpts.pType
            }

            continue
        } else {

			if nOpts != nil {
				if nOpts.mInterval != 0 {
					resp[i].MinInterval = nOpts.mInterval
				}

	            resp[i].PreferredType = nOpts.pType
			}

			if nInfo == nil {
				sErr = tlerr.NotSupportedError{
					Format: "Subscribe not supported", Path: path}
				resp[i].Err = sErr
				continue
			}

            resp[i].IsOnChangeSupported = true

			nInfo.path = path
			nInfo.app = app
			nInfo.appInfo = appInfo
			nInfo.dbs = dbs

			dbNotificationMap[nInfo.dbno] = append(dbNotificationMap[nInfo.dbno], nInfo)
        }

	}

	log.Info("map=", dbNotificationMap)

	if sErr != nil {
		return resp, sErr
	}

	sInfo := &subscribeInfo {syncDone:false,
					q:q,
					stop:stop}

	sErr = startSubscribe(sInfo, dbNotificationMap)

	return resp, sErr
}

//Check if subscribe is supported on the given paths
func IsSubscribeSupported(paths []string) ([]*IsSubscribeResponse, error) {

	resp := make ([]*IsSubscribeResponse, len(paths))

	for i, _ := range resp {
        resp[i] = &IsSubscribeResponse{Path: paths[i],
                                IsOnChangeSupported: false,
                                MinInterval: minSubsInterval,
                                PreferredType:Sample,
                                Err:nil}
	}

	dbs, err := getAllDbs()

    if err != nil {
        return resp, err
    }

	defer closeAllDbs(dbs[:])

	for i, path := range paths {

		app, _, err := getAppModule(path)

		if err != nil {
			resp[i].Err = err
			continue
		}

		nOpts, _, errApp := (*app).translateSubscribe (dbs, path)

		if errApp != nil {
			resp[i].Err = errApp
			err = errApp
            continue
        } else {
			resp[i].IsOnChangeSupported= true

			if nOpts != nil {
				if nOpts.mInterval != 0 {
					resp[i].MinInterval = nOpts.mInterval
				}
				resp[i].PreferredType = nOpts.pType
			}
		}
	}

	return resp, err
}

//Gets all the models supported by Translib
func GetModels() ([]ModelData, error) {
	var err error

	return getModels(), err
}

//Creates connection will all the redis DBs. To be used for get request
func getAllDbs() ([db.MaxDB]*db.DB, error) {
	var dbs [db.MaxDB]*db.DB
    var err error

	//Create Application DB connection
    dbs[db.ApplDB], err = db.NewDB(getDBOptions(db.ApplDB))

	if err != nil {
		closeAllDbs(dbs[:])
		return dbs, err
	}

    //Create ASIC DB connection
    dbs[db.AsicDB], err = db.NewDB(getDBOptions(db.AsicDB))

	if err != nil {
		closeAllDbs(dbs[:])
		return dbs, err
	}

	//Create Counter DB connection
    dbs[db.CountersDB], err = db.NewDB(getDBOptions(db.CountersDB))

	if err != nil {
		closeAllDbs(dbs[:])
		return dbs, err
	}

	//Create Log Level DB connection
    dbs[db.LogLevelDB], err = db.NewDB(getDBOptions(db.LogLevelDB))

	if err != nil {
		closeAllDbs(dbs[:])
		return dbs, err
	}

	//Create Config DB connection
    dbs[db.ConfigDB], err = db.NewDB(getDBOptions(db.ConfigDB))

	if err != nil {
		closeAllDbs(dbs[:])
		return dbs, err
	}

	//Create Flex Counter DB connection
    dbs[db.FlexCounterDB], err = db.NewDB(getDBOptions(db.FlexCounterDB))

	if err != nil {
		closeAllDbs(dbs[:])
		return dbs, err
	}

	//Create State DB connection
    dbs[db.StateDB], err = db.NewDB(getDBOptions(db.StateDB))

	if err != nil {
		closeAllDbs(dbs[:])
		return dbs, err
	}

	return dbs, err
}

//Closes the dbs, and nils out the arr.
func closeAllDbs(dbs []*db.DB) {
	for dbsi, d := range dbs {
		if d != nil {
			d.DeleteDB()
			dbs[dbsi] = nil
		}
	}
}

// Implement Compare method for priority queue for SubscribeResponse struct
func (val SubscribeResponse) Compare(other queue.Item) int {
	o := other.(*SubscribeResponse)
	if val.Timestamp > o.Timestamp {
		return 1
	} else if val.Timestamp == o.Timestamp {
		return 0
	}
	return -1
}

func getDBOptions(dbNo db.DBNum) db.Options {
	var opt db.Options

	switch dbNo {
	case db.ApplDB, db.CountersDB:
		opt = getDBOptionsWithSeparator(dbNo, "", ":", ":")
		break
	case db.FlexCounterDB, db.AsicDB, db.LogLevelDB, db.ConfigDB, db.StateDB:
		opt = getDBOptionsWithSeparator(dbNo, "", "|", "|")
		break
	}

	return opt
}

func getDBOptionsWithSeparator(dbNo db.DBNum, initIndicator string, tableSeparator string, keySeparator string) db.Options {
	return(db.Options {
                    DBNo              : dbNo,
                    InitIndicator     : initIndicator,
                    TableNameSeparator: tableSeparator,
                    KeySeparator      : keySeparator,
                      })
}

func getAppModule (path string) (*appInterface, *appInfo, error) {
	var app appInterface

    aInfo, err := getAppModuleInfo(path)

    if err != nil {
        return nil, aInfo, err
    }

    app, err = getAppInterface(aInfo.appType)

    if err != nil {
        return nil, aInfo, err
    }

	return &app, aInfo, err
}

func appInitialize (app *appInterface, appInfo *appInfo, path string, payload *[]byte, opCode int) error {
    var err error
    var input []byte

    if payload != nil {
        input = *payload
    }

    if appInfo.isNative {
        log.Info("Native MSFT format")
        data := appData{path: path, payload: input}
        (*app).initialize(data)
    } else {
       ygotStruct, ygotTarget, err := getRequestBinder (&path, payload, opCode, &(appInfo.ygotRootType)).unMarshall()
        if err != nil {
            log.Info("Error in request binding: ", err)
            return err
        }

        data := appData{path: path, payload: input, ygotRoot: ygotStruct, ygotTarget: ygotTarget}
        (*app).initialize(data)
    }

    return err
}
