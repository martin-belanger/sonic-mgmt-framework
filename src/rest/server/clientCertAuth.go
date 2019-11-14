
package server

import (
	"net/http"
	"github.com/golang/glog"
	"strings"
)
func ClientCertAuthenAndAuthor(r *http.Request, rc *RequestContext) error {

	var username string
	if r.TLS != nil && len(r.TLS.PeerCertificates) > 0 {
		username = strings.ToLower(r.TLS.PeerCertificates[0].Subject.CommonName)
	}

	if len(username) == 0 {
		glog.Errorf("[%s] User info not present", rc.ID)
		return httpError(http.StatusUnauthorized, "")
	}

	if DoesUserExist(username) == false {
		glog.Errorf("[%s] Invalid username", rc.ID)
		return httpError(http.StatusUnauthorized, "")
	}

	glog.Infof("[%s] Received user=%s", rc.ID, username)

	glog.Infof("[%s] Authentication passed. user=%s ", rc.ID, username)

	//Allow SET request only if user belong to admin group
	if isWriteOperation(r) && IsAdminGroup(username) == false {
		glog.Errorf("[%s] Not an admin; cannot allow %s", rc.ID, r.Method)
		return httpError(http.StatusForbidden, "Not an admin user")
	}

	glog.Infof("[%s] Authorization passed", rc.ID)
	return nil
}