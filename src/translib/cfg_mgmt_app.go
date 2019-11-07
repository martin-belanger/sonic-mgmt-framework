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
	"encoding/json"
	"translib/db"
	log "github.com/golang/glog"
    "translib/transformer"
)

func init() {
	transformer.XlateFuncBind("rpc_config_save", rpc_config_save)
	transformer.XlateFuncBind("rpc_config_load", rpc_config_load)
	transformer.XlateFuncBind("rpc_config_reload", rpc_config_reload)
}


var rpc_config_reload transformer.RpcCallpoint = func(body []byte, dbs [db.MaxDB]*db.DB) ([]byte, error) {
    return cfg_mgmt_action(body, "reload", true)
}

var rpc_config_load transformer.RpcCallpoint = func(body []byte, dbs [db.MaxDB]*db.DB) ([]byte, error) {
    return cfg_mgmt_action(body, "load", false)
}

var rpc_config_save transformer.RpcCallpoint = func(body []byte, dbs [db.MaxDB]*db.DB) ([]byte, error) {
    return cfg_mgmt_action(body, "save", false)
}

func cfg_mgmt_action(body []byte, command string, async bool) ([]byte, error) {
	
    var err error
    var result []byte
    var options []string
    var query_result  hostResult
	
    var operand struct {
		Input struct {
			Filename string `json:"filename"`
		} `json:"sonic-config-mgmt:input"`
	}
    
    
	err = json.Unmarshal(body, &operand)
	if err != nil {
        /* Unmarshall failed, no input provided.
         * set to default */
       log.Info("Filename not provided, using default")
	} else {
       filename := operand.Input.Filename
       options = append(options, filename)
       log.Info("filename", filename)
    }
	
    if async == true {
        _, err = hostQueryAsync("cfg_mgmt."+ command, options)
    } else {
        query_result = hostQuery("cfg_mgmt." + command, options)
    }
    
    var sum struct {
		Output struct {
			Result string `json:"status"`
		} `json:"sonic-config-mgmt:output"`
	}
    
    if query_result.Err != nil {
        sum.Output.Result = "Fail"
    } else {
	    sum.Output.Result = operand.Input.Filename
    }
	result, err = json.Marshal(&sum)

	return result, err
}
