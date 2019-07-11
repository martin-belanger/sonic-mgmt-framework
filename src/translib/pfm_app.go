package translib

import (
    "reflect"
    "encoding/json"
    "errors"
    "translib/db"
    "translib/ocbinds"
    "github.com/openconfig/ygot/ygot"
    "os"
    "io/ioutil"
    log "github.com/golang/glog"
)

type PlatformApp struct {
    path        *PathInfo
    reqData     []byte
    ygotRoot    *ygot.GoStruct
    ygotTarget  *interface{}


}

func init() {
    log.Info("Init called for Platform module")
    err := register("/openconfig-platform:components",
    &appInfo{appType: reflect.TypeOf(PlatformApp{}),
    ygotRootType: reflect.TypeOf(ocbinds.OpenconfigPlatform_Components{}),
    isNative:     false})
    if err != nil {
        log.Fatal("Register Platform app module with App Interface failed with error=", err)
    }

    err = addModel(&ModelData{Name: "openconfig-platform",
    Org: "OpenConfig working group",
    Ver:      "1.0.2"})
    if err != nil {
        log.Fatal("Adding model data to appinterface failed with error=", err)
    }
}

func (app *PlatformApp) initialize(data appData) {
    log.Info("initialize:if:path =", data.path)

    app.path = NewPathInfo(data.path)
    app.reqData = data.payload
    app.ygotRoot = data.ygotRoot
    app.ygotTarget = data.ygotTarget

}

func (app *PlatformApp) getAppRootObject() (*ocbinds.OpenconfigPlatform_Components) {
	deviceObj := (*app.ygotRoot).(*ocbinds.Device)
	return deviceObj.Components
}

func (app *PlatformApp) translateCreate(d *db.DB) ([]db.WatchKeys, error)  {
    var err error
    var keys []db.WatchKeys
    log.Info("translateCreate:intf:path =", app.path)

    err = errors.New("PlatformApp Not implemented, translateCreate")
    return keys, err
}

func (app *PlatformApp) translateUpdate(d *db.DB) ([]db.WatchKeys, error)  {
    var err error
    var keys []db.WatchKeys
    log.Info("translateUpdate:intf:path =", app.path)
    err = errors.New("PlatformApp Not implemented, translateUpdate")
    return keys, err
}

func (app *PlatformApp) translateReplace(d *db.DB) ([]db.WatchKeys, error)  {
    var err error
    var keys []db.WatchKeys
    log.Info("translateReplace:intf:path =", app.path)
    err = errors.New("Not implemented PlatformApp translateReplace")
    return keys, err
}

func (app *PlatformApp) translateDelete(d *db.DB) ([]db.WatchKeys, error)  {
    var err error
    var keys []db.WatchKeys
    log.Info("translateDelete:intf:path =", app.path)

    err = errors.New("Not implemented PlatformApp translateDelete")
    return keys, err
}

func (app *PlatformApp) translateGet(dbs [db.MaxDB]*db.DB) error  {
    var err error
    log.Info("translateGet:intf:path =", app.path)
    //err = errors.New("Not implemented PlatformApp translateGet")
    return err
}

func (app *PlatformApp) processCreate(d *db.DB) (SetResponse, error)  {
    var err error
    var resp SetResponse

    log.Info("processCreate:intf:path =", app.path)
    log.Info("ProcessCreate: Target Type is " + reflect.TypeOf(*app.ygotTarget).Elem().Name())

    err = errors.New("Not implemented PlatformApp processCreate")
    return resp, err
}

func (app *PlatformApp) processUpdate(d *db.DB) (SetResponse, error)  {
    var err error
    var resp SetResponse
    pathInfo := app.path

    log.Infof("Received UPDATE for path %s; vars=%v", pathInfo.Template, pathInfo.Vars)
    var intfSubtree bool = false

    pfObj := app.getAppRootObject()

    log.Info("processUpdate: Target Type: " + reflect.TypeOf(*app.ygotTarget).Elem().Name())
    if reflect.TypeOf(*app.ygotTarget).Elem().Name() == "OpenconfigPlatform_Components" {
        intfSubtree = true
	log.Info("subtree request = ",  intfSubtree)
    }

    targetUriPath, err := getYangPathFromUri(app.path.Path)
    log.Info("uripath:=", targetUriPath)
    log.Info("err:=", err)

    if isSubtreeRequest(targetUriPath, "/openconfig-platform:components/component") {
	if pfObj.Component != nil  && len(pfObj.Component) > 0 {
	    log.Info("len:=", len(pfObj.Component))
	} else {
		log.Info("len:= Zero and  empty component")
	}
    } else {
	err = errors.New("Not implemented PlatformApp processUpdate")
    }

    return resp, err
}

func (app *PlatformApp) processReplace(d *db.DB) (SetResponse, error)  {
    var err error
    var resp SetResponse
    log.Info("processReplace:intf:path =", app.path)
    err = errors.New("Not implemented, PlatformApp processReplace")
    return resp, err
}

func (app *PlatformApp) processDelete(d *db.DB) (SetResponse, error)  {
    var err error
    var resp SetResponse
    log.Info("processDelete:intf:path =", app.path)

    err = errors.New("Not implemented PlatformApp processDelete")
    return resp, err
}

func (app *PlatformApp) processGet(dbs [db.MaxDB]*db.DB) (GetResponse, error)  {
    pathInfo := app.path

    log.Infof("Received GET for PlatformApp path %s; vars=%v", pathInfo.Template, pathInfo.Vars)
    return app.doGetSysEeprom()

}

///////////////////////////
func (app *PlatformApp) doGetSysEeprom() (GetResponse, error) {
	log.Infof("in doGetSysEeprom")

	return app.getSysEepromJson()
}


/**
Structures to read syseeprom from json file
*/
type JSONEeprom  struct {
	Product_Name        string `json:"Product Name"`
	Part_Number         string `json:"Part Number"`
	Serial_Number       string `json:"Serial Number"`
	Base_MAC_Address    string `json:"Base MAC Address"`
	Manufacture_Date    string `json:"Manufacture Date"`
	Device_Version      string `json:"Device Version"`
	Label_Revision      string `json:"Label Revision"`
	Platform_Name       string `json:"Platform Name"`
	ONIE_Version        string `json:"ONIE Version"`
	MAC_Addresses       int    `json:"MAC Addresses"`
	Manufacturer        string `json:"Manufacturer"`
	Manufacture_Country  string `json:"Manufacture Country"`
	Vendor_Name         string `json:"Vendor Name"`
	Diag_Version        string `json:"Diag Version"`
	Service_Tag         string `json:"Service Tag"`
	Vendor_Extension    string `json:"Vendor Extension"`
	Magic_Number        int    `json:"Magic Number"`
	Card_Type           string `json:"Card Type"`
	Hardware_Version    string `json:"Hardware Version"`
	Software_Version    string `json:"Software Version"`
	Model_Name          string `json:"Model Name"`

}

func getSysEepromFromFile (eeprom *ocbinds.OpenconfigPlatform_Components_Component_State) (error) {

	log.Infof("getSysEepromFromFile Enter")
	jsonFile, err := os.Open("/mnt/platform/syseeprom")
	if err != nil {
	    log.Infof("syseeprom.json open failed")
	    return err
        }

	defer jsonFile.Close()

	byteValue, _ := ioutil.ReadAll(jsonFile)
	var jsoneeprom JSONEeprom

	log.Infof("Before syseeprom.json: ", jsoneeprom)
	json.Unmarshal(byteValue, &jsoneeprom)
	log.Infof("syseeprom.json: ", jsoneeprom)
	empty := false
	removable := false
	//operStatus := 0
	name := "System Eeprom"
	location  :=  "Slot 1"
	eeprom.Empty = &empty
	eeprom.Removable = &removable
	eeprom.Name = &name
	//eeprom.OperStatus = (ocbinds.E_OpenconfigPlatformTypes_COMPONENT_OPER_STATUS *) &operStatus
	eeprom.Location = &location

	if jsoneeprom.Product_Name != "" {
	    eeprom.Id = &jsoneeprom.Product_Name
	}
	if jsoneeprom.Part_Number != "" {
	    eeprom.PartNo = &jsoneeprom.Part_Number
	}
	if jsoneeprom.Serial_Number != "" {
	    eeprom.SerialNo = &jsoneeprom.Serial_Number
	}
	if jsoneeprom.Base_MAC_Address != "" {
	}
	if jsoneeprom.Manufacture_Date != "" {
	    eeprom.MfgDate = &jsoneeprom.Manufacture_Date
	}
	if jsoneeprom.Device_Version != "" {
	    //eeprom.HardwareVersion = &jsoneeprom.Device_Version
	}
	if jsoneeprom.Label_Revision != "" {
            eeprom.HardwareVersion = &jsoneeprom.Label_Revision
	    //eeprom.FirmwareVersion = &jsoneeprom.Label_Revision 
	}
	if jsoneeprom.Platform_Name != "" {
	    eeprom.Description = &jsoneeprom.Platform_Name
	}
	if jsoneeprom.ONIE_Version != "" {
	}
	if jsoneeprom.MAC_Addresses != 0 {
	}
	if jsoneeprom.Manufacturer != "" {
	    eeprom.MfgName = &jsoneeprom.Manufacturer
	}
	if jsoneeprom.Manufacture_Country != "" {
	}
	if jsoneeprom.Vendor_Name != "" {
	}
	if jsoneeprom.Diag_Version != "" {
	}
	if jsoneeprom.Service_Tag != "" {
            if eeprom.SerialNo == "" {
                eeprom.SerialNo = &jsoneeprom.Service_Tag
            }
	}
	if jsoneeprom.Vendor_Extension != "" {
	}
	if jsoneeprom.Magic_Number != 0 {
	}
	if jsoneeprom.Card_Type != "" {
	}
	if jsoneeprom.Hardware_Version != "" {
	    eeprom.HardwareVersion = &jsoneeprom.Hardware_Version
	}
	if jsoneeprom.Software_Version != "" {
	    eeprom.SoftwareVersion = &jsoneeprom.Software_Version
	}
	if jsoneeprom.Model_Name != "" {
	}

	log.Infof(" eeprom. info :", eeprom)
	return nil 
}

func (app *PlatformApp) getSysEepromJson () (GetResponse, error) {

	log.Infof("Preparing json for system eeprom");

	var pf_cpts *ocbinds.OpenconfigPlatform_Components = app.getAppRootObject()
	pf_comp,_ := pf_cpts.NewComponent("System Eeprom")
	pf_comp.State =
		&ocbinds.OpenconfigPlatform_Components_Component_State{}

	var payload []byte
	err := getSysEepromFromFile(pf_comp.State)
	if err != nil {
	    log.Infof("getSysEepromFromFile Failed")
	    return GetResponse{Payload: payload}, err
	}
	if reflect.TypeOf(*app.ygotTarget).Elem().Name() == "OpenconfigPlatform_Components" {
	    log.Info("Top level request ...")
	    payload, err = dumpIetfJson((*app.ygotRoot).(*ocbinds.Device), true)
	} else {
	    log.Info("Some other request")
	    payload, err = dumpIetfJson(pf_cpts, false)
	}
	return  GetResponse{Payload: payload}, err
}

