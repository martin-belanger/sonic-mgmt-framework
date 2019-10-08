package translib

import (
	"errors"
	log "github.com/golang/glog"
	"translib/db"
	"translib/tlerr"
	"translib/ocbinds"
        "strconv"
)

/******** CONFIG FUNCTIONS ********/

func (app *IntfApp) translateUpdateLagIntfConfig(d *db.DB, lagName *string, lag *ocbinds.OpenconfigInterfaces_Interfaces_Interface ) error {
    var err error
    m := make(map[string]string)
    entryVal := db.Value{Field: m}
    curr, _ := d.GetEntry(app.lagD.lagTs, db.Key{Comp: []string{*lagName}})
    //Create new PortChannel entry
    if !curr.IsPopulated() {
        log.Info("LAG-" + *lagName + " not present in DB, need to create it!!")
        entryVal.Field["admin_status"]= "up"
        entryVal.Field["mtu"]= "9100"
        app.ifTableMap[*lagName] = dbEntry{op: opCreate, entry: entryVal}
        return nil
    }
    // PortChannel already exists, update entries
    if (lag.Aggregation) != nil{
        if (lag.Aggregation.Config) == nil{
            return err
        }
        if lag.Aggregation.Config.MinLinks != nil {
                curr.Field["min_links"]= strconv.Itoa(int(*lag.Aggregation.Config.MinLinks))
        }
        if lag.Aggregation.Config.Fallback != nil {
                curr.Field["fallback"]=  strconv.FormatBool(*lag.Aggregation.Config.Fallback)
        }
    }
    app.translateUpdateIntfConfig(lagName, lag, &curr)
    return err
}

func (app *IntfApp) translateUpdateLagIntf(d *db.DB, lagName *string, inpOp reqType) ([]db.WatchKeys, error) {

    var err error
    var keys []db.WatchKeys

    intfObj := app.getAppRootObject()
    intf := intfObj.Interface[*lagName]

    /* Handling Interface attrbutes config updates */
    app.translateUpdateLagIntfConfig(d, lagName, intf)
    if err != nil {
            return keys, err
    }

    /* Handling Interface IP address updates */
    err = app.translateUpdateIntfSubInterfaces(d, lagName, intf)
    if err != nil {
        return keys, err
    }
    return keys, err
}

func (app *IntfApp) processUpdateLagIntfConfig(d *db.DB) error {
	var err error
	for lagName, lagEntry := range app.ifTableMap {
		switch lagEntry.op {
		case opCreate:
			err = d.CreateEntry(app.lagD.lagTs, db.Key{Comp: []string{lagName}}, lagEntry.entry)
			if err != nil {
				errStr := "Creating LAG entry for LAG : " + lagName + " failed"
				return errors.New(errStr)
			}
		case opUpdate:
			err = d.SetEntry(app.lagD.lagTs, db.Key{Comp: []string{lagName}}, lagEntry.entry)
			if err != nil {
				errStr := "Updating LAG entry for LAG : " + lagName + " failed"
				return errors.New(errStr)
			}
		}
	}
	return err
}

/* Handling IP address configuration for given PortChannel */
func (app *IntfApp) processUpdateLagIntfSubInterfaces(d *db.DB) error {
	var err error
	/* Updating the PORTCANNEL_INTERFACE table */
	for ifName, ipEntries := range app.ifIPTableMap {
                ts := app.lagD.lagIPTs
		m := make(map[string]string)
		m["NULL"] = "NULL"
                for ip, ipEntry := range ipEntries {
                    if ipEntry.op == opCreate {
                            log.Info("Creating entry for ", ifName, ":", ip)
                            err = d.CreateEntry(ts, db.Key{Comp: []string{ifName, ip}}, ipEntry.entry)
                            if err != nil {
                                    errStr := "Creating entry for " + ifName + ":" + ip + " failed"
                                    return errors.New(errStr)
                            }
                    } else if ipEntry.op == opDelete {
                            log.Info("Deleting entry for ", ifName, ":", ip)
                            err = d.DeleteEntry(ts, db.Key{Comp: []string{ifName, ip}})
                            if err != nil {
                                    errStr := "Deleting entry for " + ifName + ":" + ip + " failed"
                                    return errors.New(errStr)
                            }
                    }
		}
	}
	return err
}

func (app *IntfApp) processUpdateLagIntf(d *db.DB) error {
	var err error
	err = app.processUpdateLagIntfConfig(d)
	if err != nil {
		return err
	}

        err = app.processUpdateLagIntfSubInterfaces(d)
        if err != nil {
            return err
        }

	return err
}

/********* DELETE FUNCTIONS ********/
func (app *IntfApp) translateDeleteLagIntface(d *db.DB, intf *ocbinds.OpenconfigInterfaces_Interfaces_Interface, lagName *string) error {
	var err error
	curr, err := d.GetEntry(app.lagD.lagTs, db.Key{Comp: []string{*lagName}})
	if err != nil {
		errStr := "Invalid Lag: " + *lagName
		return tlerr.InvalidArgsError{Format: errStr}
	}
	app.ifTableMap[*lagName] = dbEntry{entry: curr, op: opDelete}
	return  err
}

func (app *IntfApp) translateDeleteLagIntf(d *db.DB, ifName *string) ([]db.WatchKeys, error) {
	var err error
	var keys []db.WatchKeys

	intfObj := app.getAppRootObject()
	intf := intfObj.Interface[*ifName]

	if intf.Subinterfaces != nil { //Only remove IP entry
	    err = app.translateDeleteIntfSubInterfaces(d, intf, ifName)
	    if err != nil {
		return keys, err
	    }
	    return keys, err
        }

        /* Handling PortChannel Deletion */
	err = app.translateDeleteLagIntface(d, intf, ifName)
	if err != nil {
		return keys, err
	}

	return keys, err
}

/* Delete will require updating both PORTCHANNEL, PORTCHANNEL_MEMBER TABLE, PORTCHANNEL_INTERFACE TABLE */
func (app *IntfApp) processDeleteLagIntfAndMembers(d *db.DB) error {
	var err error

	for lagKey, _ := range app.ifTableMap {
            log.Info("lagKey is", lagKey)
            lagKeys, err1 := d.GetKeys(app.lagD.lagMemberTs)
            lagIPKeys, err2 := d.GetKeys(app.lagD.lagIPTs)
            /* Delete entries in PORTCHANNEL_MEMBER TABLE */
            if err1 == nil {
                for i, _ := range lagKeys {
                    if lagKey == lagKeys[i].Get(0) {
                        log.Info("Removing member port", lagKeys[i].Get(1))
                        err = d.DeleteEntry(app.lagD.lagMemberTs, lagKeys[i])
                        if err != nil {
                            log.Info("Deleting member port entry failed")
                            return err
                        }
                    }
                }
            }
            /* Delete entry in PORTCHANNEL_INTERFACE TABLE */
            if err2 == nil {
                for i, _ := range lagIPKeys {
                    if lagKey == lagIPKeys[i].Get(0) {
                        log.Info("Removing IP entry", lagKeys[i].Get(1))
                        err = d.DeleteEntry(app.lagD.lagIPTs, lagKeys[i])
                        if err != nil {
                            log.Info("Deleting IP address entry failed")
                            return err
                        }
                    }
                }
            }
            /* Delete entry in PORTCHANNEL TABLE */
            err = d.DeleteEntry(app.lagD.lagTs, db.Key{Comp: []string{lagKey}})
            if err != nil {
                    return err
            }
            log.Info("Success- PortChannel deletion complete")
        }
	return err
}

/* Delete entry from PORTCHANNEL_INTERFACE TABLE */
func (app *IntfApp) processDeleteLagIntfSubInterfaces(d *db.DB) error {
	var err error
	for ifName, ipEntries := range app.ifIPTableMap {
            for ip, _ := range ipEntries {
                log.Info("Deleting entry for ", ifName, ":", ip)
                err = d.DeleteEntry(app.lagD.lagIPTs, db.Key{Comp: []string{ifName, ip}})
                if err != nil {
                    return err
                }
            }
            log.Info("Success- IP adddress entry removed")
	}
	return err
}

func (app *IntfApp) processDeleteLagIntf(d *db.DB) error {
	var err error

        err = app.processDeleteLagIntfSubInterfaces(d)
	if err != nil {
		return err
	}

	err = app.processDeleteLagIntfAndMembers(d)
	if err != nil {
		return err
	}

	return err
}
