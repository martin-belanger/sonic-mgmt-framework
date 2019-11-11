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

package translib

import (
     "errors"
     "fmt"
    "strings"
	"encoding/json"
	"translib/db"
	log "github.com/golang/glog"
    "translib/transformer"
)

func init() {
	transformer.XlateFuncBind("rpc_config_copy", rpc_config_copy)
}


var rpc_config_copy transformer.RpcCallpoint = func(body []byte, dbs [db.MaxDB]*db.DB) ([]byte, error) {
    return cfg_copy_action(body)
}

type Config struct {
    source  string
    destination string
    overwrite bool
}

var m map[Config]string


func init() {

    m = make(map[Config]string)

    m[Config{"running-configuration", "startup-configuration", false}] = "cfg_mgmt.save"
    m[Config{"running-configuration", "filename", false}]= "cfg_mgmt.save"
    m[Config{"filename", "running-configuration", false}] ="cfg_mgmt.load"
    m[Config{"startup-configuration", "running-configuration", false}] ="cfg_mgmt.load"
    m[Config{"filename", "running-configuration", true}] ="cfg_mgmt.reload"
    m[Config{"startup-configuration", "running-configuration", true}] ="cfg_mgmt.reload"
}


func validate_filename(filename string) (fname string, err error ) {
   
    if  (strings.HasPrefix(filename, "file://etc/sonic/") == false)  ||
        (strings.Contains(filename, "/..") == true)  {
            return filename, errors.New("ERROR:Invalid filename " + filename)
    }

    filename = strings.TrimPrefix(filename, "file:/")
    return filename, nil
}

func cfg_copy_action(body []byte) ([]byte, error) {
    var err error
    var result []byte
    var options []string
    var query_result  hostResult
    var source,destination,filename string

    var operand struct {
		Input struct {
			Source string `json:"source"`
            Destination string `json:"destination"`
            Overwrite bool `json:"overwrite"`
		} `json:"sonic-config-mgmt:input"`
	}

    var sum struct {
		Output struct {
			Result string `json:"status"`
		} `json:"sonic-config-mgmt:output"`
	}

    err = json.Unmarshal(body, &operand)
	if err != nil {
        /* Unmarshall failed, no input provided.
         * set to default */
       log.Fatal("Config input not provided.")
       err = errors.New("Input parameters missing.")
	} else {
       source = operand.Input.Source
       destination = operand.Input.Destination

       if (source != "running-configuration") &&
          (source != "startup-configuration") {
             filename, err = validate_filename(source)
             source = "filename"
       }

       if destination != "running-configuration" &&
          destination != "startup-configuration" {
             filename, err = validate_filename(destination)
             destination = "filename"
       }

       if (err == nil ) {
            config := Config{source, destination, operand.Input.Overwrite}
            cfg_cmd, ok := m[config]
            if ok == true {
               if (source == "filename")  ||
                   (destination == "filename") {
                       options = append(options, filename)
                       log.Info("filename", filename)
               }
               query_result = hostQuery(cfg_cmd, options)
            } else {
               err = errors.New("Invalid command.")
            }
       }
    }

    if err != nil {
        sum.Output.Result  =  err.Error()
    } else if query_result.Err != nil {
        sum.Output.Result = "ERROR:Internal SONiC Hostservice communication failure."
    } else if query_result.Body[0].(int32) ==2 {
            sum.Output.Result = fmt.Sprintf("ERROR:Invalid filename %s.", filename)
    } else if query_result.Body[0].(int32) != 0 {
            sum.Output.Result = "ERROR:Command Failed."
    } else {
            sum.Output.Result = "SUCCESS."
    }
    result, err = json.Marshal(&sum)

	return result, err
}
