////////////////////////////////////////////////////////////////////////////////
//                                                                            //
//  Copyright 2019 Dell, Inc.                                                 //
//                                                                            //
//  Licensed under the Apache License, Version 2.0 (the "License");           //
//  you may not use this file except in compliance with the License.          //
//  You may obtain a copy of the License at                                   //
//                                                                            //
//  http://www.apache.org/licenses/LICENSE-2.0                                //
//                                                                            //
//  Unless required by applicable law or agreed to in writing, software       //
//  distributed under the License is distributed on an "AS IS" BASIS,         //
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  //
//  See the License for the specific language governing permissions and       //
//  limitations under the License.                                            //
//                                                                            //
////////////////////////////////////////////////////////////////////////////////

package transformer

import (
    "fmt"
    "os"
    "strings"
    log "github.com/golang/glog"
    "cvl"
    "translib/db"

    "github.com/openconfig/goyang/pkg/yang"
)

/* Data needed to construct lookup table from yang */
type yangXpathInfo  struct {
    yangDataType   string
    tableName      *string
    xfmrTbl        *string
    childTable      []string
    dbEntry        *yang.Entry
    yangEntry      *yang.Entry
    keyXpath       map[int]*[]string
    delim          string
    fieldName      string
    xfmrFunc       string
    xfmrField      string
    xfmrPost       string
    validateFunc   string
    rpcFunc        string
    xfmrKey        string
    keyName        *string
    dbIndex        db.DBNum
    keyLevel       int
    isKey          bool
    defVal         string
	hasChildSubTree bool
}

type dbInfo  struct {
    dbIndex      db.DBNum
    keyName      *string
    fieldType    string
    rpcFunc      string
    dbEntry      *yang.Entry
    yangXpath    []string
    module       string
    delim        string
}

type sonicTblSeqnInfo struct {
       OrdTbl []string
       DepTbl map[string][]string
}

type mdlInfo struct {
       Org string
       Ver string
}

var xYangSpecMap  map[string]*yangXpathInfo
var xDbSpecMap    map[string]*dbInfo
var xDbSpecOrdTblMap map[string][]string //map of module-name to ordered list of db tables { "sonic-acl" : ["ACL_TABLE", "ACL_RULE"] }
var xDbSpecTblSeqnMap  map[string]*sonicTblSeqnInfo
var xMdlCpbltMap  map[string]*mdlInfo

/* Add module name to map storing model info for model capabilities */
func addMdlCpbltEntry(yangMdlNm string) {
       log.Info("Received yang model name to be added to model info map for gnmi ", yangMdlNm)
       if xMdlCpbltMap == nil {
               xMdlCpbltMap = make(map[string]*mdlInfo)
       }
       mdlInfoEntry := new(mdlInfo)
       if mdlInfoEntry == nil {
               log.Warningf("Memory allocation failure for storing model info for gnmi - module %v", yangMdlNm)
               return
       }
       mdlInfoEntry.Org = ""
       mdlInfoEntry.Ver = ""
       xMdlCpbltMap[yangMdlNm] = mdlInfoEntry
       return
}

/* Add version and organization info for model capabilities into map */
func addMdlCpbltData(yangMdlNm string, version string, organization string) {
	log.Infof("Adding version %v and organization %v for yang module %v", version, organization, yangMdlNm)
	if xMdlCpbltMap == nil {
               xMdlCpbltMap = make(map[string]*mdlInfo)
        }
	mdlInfoEntry, ok := xMdlCpbltMap[yangMdlNm]
	if ((!ok) || (mdlInfoEntry == nil)) {
		mdlInfoEntry = new(mdlInfo)
		if mdlInfoEntry == nil {
			log.Warningf("Memory allocation failure for storing model info for gnmi - module %v", yangMdlNm)
			return
		}
       }
       mdlInfoEntry.Ver = version
       mdlInfoEntry.Org = organization
       xMdlCpbltMap[yangMdlNm] = mdlInfoEntry
       return
}

/* update transformer spec with db-node */
func updateDbTableData (xpath string, xpathData *yangXpathInfo, tableName string) {
	if len(tableName) == 0 {
		return
	}
	_, ok := xDbSpecMap[tableName]
	if ok {
		xDbSpecMap[tableName].yangXpath = append(xDbSpecMap[tableName].yangXpath, xpath)
		xpathData.dbEntry = xDbSpecMap[tableName].dbEntry
	}
}

func childSubTreePresenceFlagSet(xpath string) {
		parXpath := parentXpathGet(xpath)
	for {
		if parXpath == "" {
			break
		}
		if parXpathData, ok := xYangSpecMap[parXpath]; ok {
			parXpathData.hasChildSubTree = true
		}
		parXpath = parentXpathGet(parXpath)
	}
	return
}

/* Recursive api to fill the map with yang details */
func yangToDbMapFill (keyLevel int, xYangSpecMap map[string]*yangXpathInfo, entry *yang.Entry, xpathPrefix string, xpathFull string) {
	xpath := ""
	curKeyLevel  := 0
	curXpathFull := ""

	if entry != nil && (entry.Kind == yang.CaseEntry || entry.Kind == yang.ChoiceEntry) {
		curXpathFull = xpathFull + "/" + entry.Name
		if _, ok := xYangSpecMap[xpathPrefix]; ok {
			curKeyLevel = xYangSpecMap[xpathPrefix].keyLevel
		}
		curXpathData, ok := xYangSpecMap[curXpathFull]
		if !ok {
			curXpathData = new(yangXpathInfo)
			xYangSpecMap[curXpathFull] = curXpathData
			curXpathData.dbIndex = db.ConfigDB // default value
		}
		curXpathData.yangDataType = strings.ToLower(yang.EntryKindToName[entry.Kind])
		curXpathData.yangEntry    = entry
		xpath = xpathPrefix
	} else {
	/* create the yang xpath */
	if xYangSpecMap[xpathPrefix] != nil  && xYangSpecMap[xpathPrefix].yangDataType == "module" {
		/* module name is separated from the rest of xpath with ":" */
		xpath = xpathPrefix + ":" + entry.Name
	} else {
		xpath = xpathPrefix + "/" + entry.Name
	}

	updateChoiceCaseXpath := false
	curXpathFull = xpath
	if xpathPrefix != xpathFull {
		curXpathFull = xpathFull + "/" + entry.Name
		if annotNode, ok := xYangSpecMap[curXpathFull]; ok {
			xpathData := new(yangXpathInfo)
			xYangSpecMap[xpath] = xpathData
			copyYangXpathSpecData(xYangSpecMap[xpath], annotNode)
			updateChoiceCaseXpath = true
		}
	}

	xpathData, ok := xYangSpecMap[xpath]
	if !ok {
		xpathData = new(yangXpathInfo)
		xYangSpecMap[xpath] = xpathData
		xpathData.dbIndex = db.ConfigDB // default value
	} else {
		xpathData = xYangSpecMap[xpath]
		if len(xpathData.xfmrFunc) > 0 {
			childSubTreePresenceFlagSet(xpath)
		}
	}

	xpathData.yangDataType = entry.Node.Statement().Keyword
	if (xpathData.tableName != nil && *xpathData.tableName != "") {
		childToUpdateParent(xpath, *xpathData.tableName)
	}

	parentXpathData, ok := xYangSpecMap[xpathPrefix]
	/* init current xpath table data with its parent data, change only if needed. */
	if ok && xpathData.tableName == nil {
		if xpathData.tableName == nil && parentXpathData.tableName != nil && xpathData.xfmrTbl == nil {
			xpathData.tableName = parentXpathData.tableName
		} else if xpathData.xfmrTbl == nil && parentXpathData.xfmrTbl != nil {
			xpathData.xfmrTbl = parentXpathData.xfmrTbl
		}
	}

	if ok && xpathData.dbIndex == db.ConfigDB && parentXpathData.dbIndex != db.ConfigDB {
		// If DB Index is not annotated and parent DB index is annotated inherit the DB Index of the parent
		xpathData.dbIndex = parentXpathData.dbIndex
	}

	if ok && len(parentXpathData.validateFunc) > 0 {
		xpathData.validateFunc = parentXpathData.validateFunc
	}

	if ok && len(parentXpathData.xfmrFunc) > 0 && len(xpathData.xfmrFunc) == 0 {
		xpathData.xfmrFunc = parentXpathData.xfmrFunc
	}

	if ((xpathData.yangDataType ==  YANG_LEAF || xpathData.yangDataType == YANG_LEAF_LIST) && (len(xpathData.fieldName) == 0)) {

		if len(xpathData.xfmrField) != 0 {
			xpathData.xfmrFunc = ""
		}
		if xpathData.tableName != nil && xDbSpecMap[*xpathData.tableName] != nil {
			if _, ok := xDbSpecMap[*xpathData.tableName + "/" + entry.Name]; ok {
				xpathData.fieldName = entry.Name
			} else {
				if _, ok := xDbSpecMap[*xpathData.tableName + "/" + strings.ToUpper(entry.Name)]; ok {
					xpathData.fieldName = strings.ToUpper(entry.Name)
				}
				if _, ok := xDbSpecMap[*xpathData.tableName + "/" + entry.Name]; ok {
					xpathData.fieldName = entry.Name
				}
			}
		} else if xpathData.xfmrTbl != nil {
			/* table transformer present */
			xpathData.fieldName = entry.Name
		}
	}
	if xpathData.yangDataType == YANG_LEAF && len(entry.Default) > 0 {
		xpathData.defVal = entry.Default
	}

	if (xpathData.yangDataType == YANG_LEAF || xpathData.yangDataType == YANG_LEAF_LIST) && len(xpathData.fieldName) > 0 && xpathData.tableName != nil {
		dbPath := *xpathData.tableName + "/" + xpathData.fieldName
		if xDbSpecMap[dbPath] != nil {
			xDbSpecMap[dbPath].yangXpath = append(xDbSpecMap[dbPath].yangXpath, xpath)
		}
	}

	/* fill table with key data. */
	curKeyLevel := keyLevel
	if len(entry.Key) != 0 {
		parentKeyLen := 0

		/* create list with current keys */
		keyXpath        := make([]string, len(strings.Split(entry.Key, " ")))
		for id, keyName := range(strings.Split(entry.Key, " ")) {
			keyXpath[id] = xpath + "/" + keyName
			if _, ok := xYangSpecMap[xpath + "/" + keyName]; !ok {
				keyXpathData := new(yangXpathInfo)
				xYangSpecMap[xpath + "/" + keyName] = keyXpathData
			}
			xYangSpecMap[xpath + "/" + keyName].isKey = true
		}

		xpathData.keyXpath = make(map[int]*[]string, (parentKeyLen + 1))
		k := 0
		for ; k < parentKeyLen; k++ {
			/* copy parent key-list to child key-list*/
			xpathData.keyXpath[k] = parentXpathData.keyXpath[k]
		}
		xpathData.keyXpath[k] = &keyXpath
		xpathData.keyLevel    = curKeyLevel
		curKeyLevel++
	} else if parentXpathData != nil && parentXpathData.keyXpath != nil {
		xpathData.keyXpath = parentXpathData.keyXpath
	}
	xpathData.yangEntry = entry
	if updateChoiceCaseXpath == true {
		copyYangXpathSpecData(xYangSpecMap[curXpathFull], xYangSpecMap[xpath])
	}
	}

	/* get current obj's children */
	var childList []string
	for k := range entry.Dir {
		childList = append(childList, k)
	}

	/* now recurse, filling the map with current node's children info */
	for _, child := range childList {
		yangToDbMapFill(curKeyLevel, xYangSpecMap, entry.Dir[child], xpath, curXpathFull)
	}
}

/* Build lookup table based of yang xpath */
func yangToDbMapBuild(entries map[string]*yang.Entry) {
    if entries == nil {
        return
    }

    if xYangSpecMap == nil {
        xYangSpecMap = make(map[string]*yangXpathInfo)
    }

    for module, e := range entries {
        if e == nil || len(e.Dir) == 0 {
            continue
        }

	/* Start to fill xpath based map with yang data */
    keyLevel := 0
    yangToDbMapFill(keyLevel, xYangSpecMap, e, "", "")

	// Fill the ordered map of child tables list for oc yangs
	updateSchemaOrderedMap(module, e)
    }
    mapPrint(xYangSpecMap, "/tmp/fullSpec.txt")
    dbMapPrint("/tmp/dbSpecMap.txt")
}

/* Fill the map with db details */
func dbMapFill(tableName string, curPath string, moduleNm string, xDbSpecMap map[string]*dbInfo, entry *yang.Entry) {
	entryType := entry.Node.Statement().Keyword

	if entry.Name != moduleNm {
		if entryType == "container" || entryType == "rpc" {
			tableName = entry.Name
		}

		if !isYangResType(entryType) {
			dbXpath := tableName
			if entryType != "container" && entryType != "rpc" {
				dbXpath = tableName + "/" + entry.Name
			}
			xDbSpecMap[dbXpath] = new(dbInfo)
			xDbSpecMap[dbXpath].dbIndex   = db.MaxDB
			xDbSpecMap[dbXpath].dbEntry   = entry
			xDbSpecMap[dbXpath].fieldType = entryType
			xDbSpecMap[dbXpath].module = moduleNm
			if entryType == "container" {
				xDbSpecMap[dbXpath].dbIndex = db.ConfigDB
				if entry.Exts != nil && len(entry.Exts) > 0 {
					for _, ext := range entry.Exts {
						dataTagArr := strings.Split(ext.Keyword, ":")
						tagType := dataTagArr[len(dataTagArr)-1]
						switch tagType {
						case "key-name" :
							if xDbSpecMap[dbXpath].keyName == nil {
								xDbSpecMap[dbXpath].keyName = new(string)
							}
							*xDbSpecMap[dbXpath].keyName = ext.NName()
						case "rpc-callback" :
							xDbSpecMap[dbXpath].rpcFunc = ext.NName()
						case "db-name" :
							xDbSpecMap[dbXpath].dbIndex = dbNameToIndex(ext.NName())
						case "key-delim" :
							xDbSpecMap[dbXpath].delim   = ext.NName()
						default :
							log.Infof("Unsupported ext type(%v) for xpath(%v).", tagType, dbXpath)
						}
					}
				}
			}
		}
	} else {
		moduleXpath := "/" + moduleNm + ":" + entry.Name
		xDbSpecMap[moduleXpath] = new(dbInfo)
		xDbSpecMap[moduleXpath].dbEntry   = entry
		xDbSpecMap[moduleXpath].fieldType = entryType
		xDbSpecMap[moduleXpath].module = moduleNm
                for {
			sncTblInfo := new(sonicTblSeqnInfo)
			if sncTblInfo == nil {
				log.Warningf("Memory allocation failure for storing Tbl order and dependency info for sonic module %v", moduleNm)
				break
			}
			cvlSess, cvlRetSess := cvl.ValidationSessOpen()
			if cvlRetSess != cvl.CVL_SUCCESS {
				log.Warningf("Failure in creating CVL validation session object required to use CVl API to get Tbl info for module %v - %v", moduleNm, cvlRetSess)
				break
			}
			var cvlRetOrdTbl cvl.CVLRetCode
			sncTblInfo.OrdTbl, cvlRetOrdTbl = cvlSess.GetOrderedTables(moduleNm)
			if cvlRetOrdTbl != cvl.CVL_SUCCESS {
				log.Warningf("Failure in cvlSess.GetOrderedTables(%v) - %v", moduleNm, cvlRetOrdTbl)

			}
			sncTblInfo.DepTbl = make(map[string][]string)
			if sncTblInfo.DepTbl == nil {
				log.Warningf("sncTblInfo.DepTbl is nill , no space to store dependency table list for sonic module %v", moduleNm)
				cvl.ValidationSessClose(cvlSess)
				break
			}
			for _, tbl := range(sncTblInfo.OrdTbl) {
				var cvlRetDepTbl cvl.CVLRetCode
				sncTblInfo.DepTbl[tbl], cvlRetDepTbl = cvlSess.GetDepTables(moduleNm, tbl)
				if cvlRetDepTbl != cvl.CVL_SUCCESS {
					log.Warningf("Failure in cvlSess.GetDepTables(%v, %v) - %v", moduleNm, tbl, cvlRetDepTbl)
				}


			}
			xDbSpecTblSeqnMap[moduleNm] = sncTblInfo
			cvl.ValidationSessClose(cvlSess)
			break
		}

	}

	var childList []string
	for _, k := range entry.DirOKeys {
		childList = append(childList, k)
	}


	for _, child := range childList {
		childPath := tableName + "/" + entry.Dir[child].Name
		dbMapFill(tableName, childPath, moduleNm, xDbSpecMap, entry.Dir[child])
	}
}

/* Build redis db lookup map */
func dbMapBuild(entries []*yang.Entry) {
	if entries == nil {
		return
	}
	xDbSpecMap = make(map[string]*dbInfo)
	xDbSpecOrdTblMap = make(map[string][]string)
	xDbSpecTblSeqnMap =  make(map[string]*sonicTblSeqnInfo)

	for _, e := range entries {
		if e == nil || len(e.Dir) == 0 {
			continue
		}
		moduleNm := e.Name
		dbMapFill("", "", moduleNm, xDbSpecMap, e)
	}
	xDbSpecTblSeqnMapPrint("/tmp/dbSpecTblSeqnMap.txt")
}

func childToUpdateParent( xpath string, tableName string) {
	var xpathData *yangXpathInfo
	parent := parentXpathGet(xpath)
	if len(parent) == 0  || parent == "/" {
		return
	}

	_, ok := xYangSpecMap[parent]
	if !ok {
		xpathData = new(yangXpathInfo)
		xYangSpecMap[parent] = xpathData
	}

       parentXpathData := xYangSpecMap[parent]
       if !contains(parentXpathData.childTable, tableName) {
               parentXpathData.childTable = append(parentXpathData.childTable, tableName)
       }

       if parentXpathData.yangEntry != nil && parentXpathData.yangEntry.Node.Statement().Keyword == "list" &&
       (parentXpathData.tableName != nil || parentXpathData.xfmrTbl != nil) {
		return
	}
	childToUpdateParent(parent, tableName)
}

func dbNameToIndex(dbName string) db.DBNum {
	dbIndex := db.ConfigDB
	switch dbName {
	case "APPL_DB" :
		dbIndex  = db.ApplDB
	case "ASIC_DB" :
		dbIndex  = db.AsicDB
	case "COUNTERS_DB" :
		dbIndex  = db.CountersDB
	case "LOGLEVEL_DB" :
		dbIndex  = db.LogLevelDB
	case "CONFIG_DB" :
		dbIndex  = db.ConfigDB
	case "FLEX_COUNTER_DB" :
		dbIndex  = db.FlexCounterDB
	case "STATE_DB" :
		dbIndex  = db.StateDB
	case "ERROR_DB" :
		dbIndex  = db.ErrorDB
	case "USER_DB" :
		dbIndex  = db.UserDB
	}
	return dbIndex
}

/* Build lookup map based on yang xpath */
func annotEntryFill(xYangSpecMap map[string]*yangXpathInfo, xpath string, entry *yang.Entry) {
	xpathData := new(yangXpathInfo)

	xpathData.dbIndex = db.ConfigDB // default value
	/* fill table with yang extension data. */
	if entry != nil && len(entry.Exts) > 0 {
		for _, ext := range entry.Exts {
			dataTagArr := strings.Split(ext.Keyword, ":")
			tagType := dataTagArr[len(dataTagArr)-1]
			switch tagType {
			case "table-name" :
				if xpathData.tableName == nil {
					xpathData.tableName = new(string)
				}
				*xpathData.tableName = ext.NName()
				updateDbTableData(xpath, xpathData, *xpathData.tableName)
			case "key-name" :
				if xpathData.keyName == nil {
					xpathData.keyName = new(string)
				}
				*xpathData.keyName = ext.NName()
			case "table-transformer" :
				if xpathData.xfmrTbl == nil {
					xpathData.xfmrTbl = new(string)
				}
				*xpathData.xfmrTbl  = ext.NName()
			case "field-name" :
				xpathData.fieldName = ext.NName()
			case "subtree-transformer" :
				xpathData.xfmrFunc  = ext.NName()
			case "key-transformer" :
				xpathData.xfmrKey   = ext.NName()
			case "key-delimiter" :
				xpathData.delim     = ext.NName()
			case "field-transformer" :
				xpathData.xfmrField  = ext.NName()
			case "post-transformer" :
				xpathData.xfmrPost  = ext.NName()
			case "get-validate" :
				xpathData.validateFunc  = ext.NName()
			case "rpc-callback" :
				xpathData.rpcFunc  = ext.NName()
			case "use-self-key" :
				xpathData.keyXpath  = nil
			case "db-name" :
				xpathData.dbIndex = dbNameToIndex(ext.NName())
			}
		}
	}
	xYangSpecMap[xpath] = xpathData
}

/* Build xpath from yang-annotation */
func xpathFromDevCreate(path string) string {
	p := strings.Split(path, "/")
	for i, k := range p {
		if len(k) > 0 { p[i] = strings.Split(k, ":")[1] }
	}
	return strings.Join(p[1:], "/")
}

/* Build lookup map based on yang xpath */
func annotToDbMapBuild(annotEntries []*yang.Entry) {
    if annotEntries == nil {
        return
    }
    if xYangSpecMap == nil {
        xYangSpecMap = make(map[string]*yangXpathInfo)
    }

    for _, e := range annotEntries {
        if e != nil && len(e.Deviations) > 0 {
            for _, d := range e.Deviations {
                xpath := xpathFromDevCreate(d.Name)
                xpath = "/" + strings.Replace(e.Name, "-annot", "", -1) + ":" + xpath
                for i, deviate := range d.Deviate {
                    if i == 2 {
                        for _, ye := range deviate {
                            annotEntryFill(xYangSpecMap, xpath, ye)
                        }
                    }
                }
            }
        }
    }
    mapPrint(xYangSpecMap, "/tmp/annotSpec.txt")
}

func annotDbSpecMapFill(xDbSpecMap map[string]*dbInfo, dbXpath string, entry *yang.Entry) error {
	var err error
	var dbXpathData *dbInfo
	var ok bool

	//Currently sonic-yang annotation is supported for "list" and "rpc" type only
	listName := strings.Split(dbXpath, "/")
	if len(listName) < 3 {
		// check rpc?
		rpcName := strings.Split(listName[1], ":")
		if len(rpcName) < 2 {
			log.Errorf("DB spec-map data not found(%v) \r\n", rpcName)
			return err
		}
		dbXpathData, ok = xDbSpecMap[rpcName[1]]
		if ok && dbXpathData.fieldType == "rpc" {
			log.Infof("Annotate dbSpecMap for (%v)(rpcName:%v)\r\n", dbXpath, listName[1])
			if entry != nil && len(entry.Exts) > 0 {
				for _, ext := range entry.Exts {
					dataTagArr := strings.Split(ext.Keyword, ":")
					tagType := dataTagArr[len(dataTagArr)-1]
					switch tagType {
					case "rpc-callback" :
						dbXpathData.rpcFunc = ext.NName()
					default :
					}
				}
			}
			dbMapPrint("/tmp/dbSpecMapFull.txt")
			return err
		} else {
			log.Errorf("DB spec-map data not found(%v) \r\n", dbXpath)
			return err
		}
	}

	// list
	dbXpathData, ok = xDbSpecMap[listName[2]]
	if !ok {
		log.Errorf("DB spec-map data not found(%v) \r\n", dbXpath)
		return err
	}
	dbXpathData.dbIndex = db.ConfigDB // default value 

	/* fill table with cvl yang extension data. */
	if entry != nil && len(entry.Exts) > 0 {
		for _, ext := range entry.Exts {
			dataTagArr := strings.Split(ext.Keyword, ":")
			tagType := dataTagArr[len(dataTagArr)-1]
			switch tagType {
			case "key-name" :
				if dbXpathData.keyName == nil {
					dbXpathData.keyName = new(string)
				}
				*dbXpathData.keyName = ext.NName()
			case "db-name" :
				dbXpathData.dbIndex  = dbNameToIndex(ext.NName())
			default :
			}
		}
	}

    dbMapPrint("/tmp/dbSpecMapFull.txt")
	return err
}

func annotDbSpecMap(annotEntries []*yang.Entry) {
	if annotEntries == nil || xDbSpecMap == nil {
		return
	}
	for _, e := range annotEntries {
		if e != nil && len(e.Deviations) > 0 {
			for _, d := range e.Deviations {
				xpath := xpathFromDevCreate(d.Name)
				xpath = "/" + strings.Replace(e.Name, "-annot", "", -1) + ":" + xpath
				for i, deviate := range d.Deviate {
					if i == 2 {
						for _, ye := range deviate {
							annotDbSpecMapFill(xDbSpecMap, xpath, ye)
						}
					}
				}
			}
		}
	}
}

/* Debug function to print the yang xpath lookup map */
func mapPrint(inMap map[string]*yangXpathInfo, fileName string) {
    fp, err := os.Create(fileName)
    if err != nil {
        return
    }
    defer fp.Close()

    for k, d := range inMap {
        fmt.Fprintf (fp, "-----------------------------------------------------------------\r\n")
        fmt.Fprintf(fp, "%v:\r\n", k)
        fmt.Fprintf(fp, "    yangDataType: %v\r\n", d.yangDataType)
        fmt.Fprintf(fp, "    hasChildSubTree: %v\r\n", d.hasChildSubTree)
        fmt.Fprintf(fp, "    tableName: ")
        if d.tableName != nil {
            fmt.Fprintf(fp, "%v", *d.tableName)
        }
	fmt.Fprintf(fp, "\r\n    postXfmr : %v", d.xfmrPost)
        fmt.Fprintf(fp, "\r\n    xfmrTbl  : ")
        if d.xfmrTbl != nil {
            fmt.Fprintf(fp, "%v", *d.xfmrTbl)
        }
        fmt.Fprintf(fp, "\r\n    keyName  : ")
        if d.keyName != nil {
            fmt.Fprintf(fp, "%v", *d.keyName)
        }
        fmt.Fprintf(fp, "\r\n    childTbl : %v", d.childTable)
        fmt.Fprintf(fp, "\r\n    FieldName: %v", d.fieldName)
        fmt.Fprintf(fp, "\r\n    defVal   : %v", d.defVal)
        fmt.Fprintf(fp, "\r\n    keyLevel : %v", d.keyLevel)
        fmt.Fprintf(fp, "\r\n    xfmrKeyFn: %v", d.xfmrKey)
        fmt.Fprintf(fp, "\r\n    xfmrFunc : %v", d.xfmrFunc)
        fmt.Fprintf(fp, "\r\n    xfmrField :%v", d.xfmrField)
        fmt.Fprintf(fp, "\r\n    dbIndex  : %v", d.dbIndex)
        fmt.Fprintf(fp, "\r\n    validateFunc  : %v", d.validateFunc)
        fmt.Fprintf(fp, "\r\n    rpcFunc  : %v", d.rpcFunc)
        fmt.Fprintf(fp, "\r\n    yangEntry: ")
        if d.yangEntry != nil {
            fmt.Fprintf(fp, "%v", *d.yangEntry)
        }
        fmt.Fprintf(fp, "\r\n    dbEntry: ")
        if d.dbEntry != nil {
            fmt.Fprintf(fp, "%v", *d.dbEntry)
        }
        fmt.Fprintf(fp, "\r\n    keyXpath: %d\r\n", d.keyXpath)
        for i, kd := range d.keyXpath {
            fmt.Fprintf(fp, "        %d. %#v\r\n", i, kd)
        }
        fmt.Fprintf(fp, "\r\n    isKey   : %v\r\n", d.isKey)
    }
    fmt.Fprintf (fp, "-----------------------------------------------------------------\r\n")

}

/* Debug function to print redis db lookup map */
func dbMapPrint( fname string) {
    fp, err := os.Create(fname)
    if err != nil {
        return
    }
    defer fp.Close()
	fmt.Fprintf (fp, "-----------------------------------------------------------------\r\n")
    for k, v := range xDbSpecMap {
		fmt.Fprintf(fp, " field:%v: \r\n", k)
        fmt.Fprintf(fp, "     type     :%v \r\n", v.fieldType)
        fmt.Fprintf(fp, "     db-type  :%v \r\n", v.dbIndex)
        fmt.Fprintf(fp, "     rpcFunc  :%v \r\n", v.rpcFunc)
        fmt.Fprintf(fp, "     module   :%v \r\n", v.module)
        fmt.Fprintf(fp, "     KeyName: ")
        if v.keyName != nil {
            fmt.Fprintf(fp, "%v\r\n", *v.keyName)
        }
		for _, yxpath := range v.yangXpath {
			fmt.Fprintf(fp, "\r\n     oc-yang  :%v ", yxpath)
		}
        fmt.Fprintf(fp, "\r\n     cvl-yang :%v \r\n", v.dbEntry)
        fmt.Fprintf (fp, "-----------------------------------------------------------------\r\n")

    }
}

func xDbSpecTblSeqnMapPrint(fname string) {
        fp, err := os.Create(fname)
        if err != nil {
                return
        }
        defer fp.Close()
        fmt.Fprintf (fp, "-----------------------------------------------------------------\r\n")
        if xDbSpecTblSeqnMap == nil {
                return
        }
        for mdlNm, mdlTblSeqnDt := range xDbSpecTblSeqnMap {
                fmt.Fprintf(fp, "%v : { \r\n", mdlNm)
                if mdlTblSeqnDt == nil {
                        continue
                }
                fmt.Fprintf(fp, "        OrderedTableList : %v\r\n", mdlTblSeqnDt.OrdTbl)
                fmt.Fprintf(fp, "        Dependent table list  : {\r\n")
                if mdlTblSeqnDt.DepTbl == nil {
                        fmt.Fprintf(fp, "                        }\r\n")
                        fmt.Fprintf(fp, "}\r\n")
                        continue
                }
                for tblNm, DepTblLst := range mdlTblSeqnDt.DepTbl {
                        fmt.Fprintf(fp, "                                        %v : %v\r\n", tblNm, DepTblLst)
                }
                fmt.Fprintf(fp, "                                }\r\n")
                fmt.Fprintf(fp, "}\r\n")
        }
}

func updateSchemaOrderedMap(module string, entry *yang.Entry) {
	var children []string
	if entry.Node.Statement().Keyword == "module" {
		for _, dir := range entry.DirOKeys {
			// Gives the yang xpath for the top level container
			xpath := "/" + module + ":" + dir
			_, ok := xYangSpecMap[xpath]
			if ok {
				yentry := xYangSpecMap[xpath].yangEntry
				if yentry.Node.Statement().Keyword == "container" {
					var keyspec = make([]KeySpec, 0)
					keyspec = FillKeySpecs(xpath, "" , &keyspec)
					children = updateChildTable(keyspec, &children)
				}
			}
		}
	}
	xDbSpecOrdTblMap[module] = children
}

func updateChildTable(keyspec []KeySpec, chlist *[]string) ([]string) {
	for _, ks := range keyspec {
		if (ks.Ts.Name != "") {
			if !contains(*chlist, ks.Ts.Name) {
				*chlist = append(*chlist, ks.Ts.Name)
			}
		}
		*chlist = updateChildTable(ks.Child, chlist)
	}
	return *chlist
}
