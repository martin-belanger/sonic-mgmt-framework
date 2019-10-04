package translib

import (
	"errors"
	log "github.com/golang/glog"
	"translib/db"
	"translib/tlerr"
        "strconv"
)

/******** CONFIG FUNCTIONS ********/

func (app *IntfApp) translateUpdateLagIntf(d *db.DB, lagName *string, inpOp reqType) ([]db.WatchKeys, error) {
	var err error
	var keys []db.WatchKeys

	intfObj := app.getAppRootObject()
	m := make(map[string]string)
	entryVal := db.Value{Field: m}
	lag := intfObj.Interface[*lagName]
	curr, _ := d.GetEntry(app.lagD.lagTs, db.Key{Comp: []string{*lagName}})
        //Create new LAG entry
	if !curr.IsPopulated() {
		log.Info("LAG-" + *lagName + " not present in DB, need to create it!!")
                entryVal.Field["admin_status"]= "up"
                entryVal.Field["mtu"]= "9100"
                //entryVal.Field["min_links"]= "0"
                //entryVal.Field["fallback"]= "false"
		app.ifTableMap[*lagName] = dbEntry{op: opCreate, entry: entryVal}
		return keys, nil
	}
        //Lag already exists
        if (lag.Aggregation) != nil{
            if (lag.Aggregation.Config) == nil{
	        return keys, err
            }
            if lag.Aggregation.Config.MinLinks != nil {
                    curr.Field["min_links"]= strconv.Itoa(int(*lag.Aggregation.Config.MinLinks))
            }
            if lag.Aggregation.Config.Fallback != nil {
                    curr.Field["fallback"]=  strconv.FormatBool(*lag.Aggregation.Config.Fallback)
            }
        }
	app.translateUpdateIntfConfig(lagName, lag, &curr)
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

func (app *IntfApp) processUpdateLagIntf(d *db.DB) error {
	var err error
	err = app.processUpdateLagIntfConfig(d)
	if err != nil {
		return err
	}

	return err
}

/********* DELETE FUNCTIONS ********/
func (app *IntfApp) translateDeleteLagIntf(d *db.DB, lagName *string) ([]db.WatchKeys, error) {
	var err error
	var keys []db.WatchKeys
	curr, err := d.GetEntry(app.lagD.lagTs, db.Key{Comp: []string{*lagName}})
	if err != nil {
		errStr := "Invalid Lag: " + *lagName
		return keys, tlerr.InvalidArgsError{Format: errStr}
	}
	app.ifTableMap[*lagName] = dbEntry{entry: curr, op: opDelete}
	return keys, err
}

// Delete will require updating both PORTCHANNEL and PORTCHANNEL_MEMBER TABLE
func (app *IntfApp) processDeleteLagIntfAndMembers(d *db.DB) error {
	var err error

	for lagKey, _ := range app.ifTableMap {
            lagKeys, err := d.GetKeys(app.lagD.lagMemberTs)
            if err == nil {
                log.Info("PortChannels have members")
                //Delete entries in PORTCHANNEL_MEMBER TABLE
                for i, _ := range lagKeys {
                    log.Info("lagKeys[i].Get(0) is", lagKeys[i].Get(0))
                    if lagKey == lagKeys[i].Get(0) {
                        log.Info("Found lagKey")
                        log.Info("Removing memner", lagKeys[i].Get(1))
                        //delete the entry
                        err = d.DeleteEntry(app.lagD.lagMemberTs, lagKeys[i])
                        if err != nil {
                            log.Info("Deleting entry failed")
                            return err
                        }
                    }
                }
            }
            //Delete entry in PORTCHANNEL TABLE
            err = d.DeleteEntry(app.lagD.lagTs, db.Key{Comp: []string{lagKey}})
            if err != nil {
                    return err
            }
        }
	return err
}

func (app *IntfApp) processDeleteLagIntf(d *db.DB) error {
	var err error

	err = app.processDeleteLagIntfAndMembers(d)
	if err != nil {
		return err
	}
	return err
}
