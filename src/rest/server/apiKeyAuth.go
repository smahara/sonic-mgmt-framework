package server

import (
	"net/http"
	// "os/user"
	"github.com/golang/glog"
	"io/ioutil"
	"strings"
	"fmt"
	// "crypto/rand"
)

func ApiKeyAuthenAndAuthor(r *http.Request, rc *RequestContext) error {
	
	api_key_header := r.Header.Get("X-API-Key")
	if api_key_header == "" {
		glog.Errorf("[%s] Api Key not present", rc.ID)
		return httpError(http.StatusUnauthorized, "")
	}

	api_key_parts := strings.Split(api_key_header, " ")
	if len(api_key_parts) != 2 {
		glog.Errorf("[%s] Invalid Api Key Format", rc.ID)
		return httpError(http.StatusUnauthorized, "")
	}
	username := api_key_parts[0]
	api_key := api_key_parts[1]

	glog.Infof("[%s] Received user=%s", rc.ID, username)
	filename := fmt.Sprintf("/etc/rest_api_keys/%v.key", username)
	user_key_file_cont, err := ioutil.ReadFile(filename)
	user_key := strings.TrimSpace(string(user_key_file_cont))
	if err != nil {
		glog.Errorf("[%s] Invalid Api Key User", rc.ID)
		return httpError(http.StatusUnauthorized, "")
	}

	if api_key != string(user_key) {

		glog.Infof("[%s] Failed to authenticate, invalid API Key", rc.ID)
		return httpError(http.StatusUnauthorized, "")

	}
	
	

	glog.Infof("[%s] Authentication passed. user=%s ", rc.ID, username)

	//Allow SET request only if user belong to admin group
	if isWriteOperation(r) && IsAdminGroup(username) == false {
		glog.Errorf("[%s] Not an admin; cannot allow %s", rc.ID, r.Method)
		return httpError(http.StatusForbidden, "Not an admin user")
	}

	glog.Infof("[%s] Authorization passed", rc.ID)
	return nil
}

// authMiddleware function creates a middleware for request
// authentication and authorization. This middleware will return
// 401 response if authentication fails and 403 if authorization
// fails.
func authApiKeyMiddleware(inner http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		rc, r := GetContext(r)
		err := ApiKeyAuthenAndAuthor(r, rc)
		if err != nil {
			status, data, ctype := prepareErrorResponse(err, r)
			w.Header().Set("Content-Type", ctype)
			w.WriteHeader(status)
			w.Write(data)
		} else {
			inner.ServeHTTP(w, r)
		}
	})
}