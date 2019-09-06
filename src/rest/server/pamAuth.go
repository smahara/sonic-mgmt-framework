package server

import (
	"net/http"
	// "os/user"
	"strings"
	"io/ioutil"
	"fmt"
	"github.com/golang/glog"
	//"github.com/msteinert/pam"
	"golang.org/x/crypto/ssh"
	"crypto/rand"
	"encoding/base64"
	"os"
)

/*
type UserCredential struct {
	Username string
	Password string
}

//PAM conversation handler.
func (u UserCredential) PAMConvHandler(s pam.Style, msg string) (string, error) {

	switch s {
	case pam.PromptEchoOff:
		return u.Password, nil
	case pam.PromptEchoOn:
		return u.Password, nil
	case pam.ErrorMsg:
		return "", nil
	case pam.TextInfo:
		return "", nil
	default:
		return "", errors.New("unrecognized conversation message style")
	}
}

// PAMAuthenticate performs PAM authentication for the user credentials provided
func (u UserCredential) PAMAuthenticate() error {
	tx, err := pam.StartFunc("login", u.Username, u.PAMConvHandler)
	if err != nil {
		return err
	}
	return tx.Authenticate(0)
}

func PAMAuthUser(u string, p string) error {

	cred := UserCredential{u, p}
	err := cred.PAMAuthenticate()
	return err
}
*/
const API_KEY_LEN = 10
const API_KEY_DIR = "/etc/rest_api_keys"

func IsAdminGroup(username string, passwd string) bool {

	//This does not work since we are in a container and 
	// /etc/passwd is not the host /etc/passwd

	// usr, err := user.Lookup(username)
	// if err != nil {
	// 	return false
	// }
	// gids, err := usr.GroupIds()
	// if err != nil {
	// 	return false
	// }
	// glog.V(2).Infof("User:%s, groups=%s", username, gids)
	// admin, err := user.Lookup("admin")
	// if err != nil {
	// 	return false
	// }
	// for _, x := range gids {
	// 	if x == admin.Gid {
	// 		return true
	// 	}
	// }
	// return false
	config := &ssh.ClientConfig{
		User: username,
		Auth: []ssh.AuthMethod{
			ssh.Password(passwd),
		},
		HostKeyCallback: ssh.InsecureIgnoreHostKey(),
	}
	client, err := ssh.Dial("tcp", "127.0.0.1:22", config)
	if err != nil {
		
		return false
	}
	session, err := client.NewSession()
	output, err := session.Output(fmt.Sprintf("id -G %v", username))
	if err != nil {
		
		return false
	}
	user_groups := strings.Split(string(output), " ")
	session.Close()
	session, err = client.NewSession()
	output, err = session.Output("id -g admin")
	if err != nil {
		
		return false
	}
	admin_group := strings.TrimSpace(string(output))
	for _,g := range(user_groups) {
		if g == admin_group {
			return true
		}
	}
	return false

}

func PAMAuthenAndAuthor(r *http.Request, rc *RequestContext) error {


	username, passwd, authOK := r.BasicAuth()
	if authOK == false {
		glog.Errorf("[%s] User info not present", rc.ID)
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
		username = api_key_parts[0]
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
	} else {

		glog.Infof("[%s] Received user=%s", rc.ID, username)
		/*
		 * mgmt-framework container does not have access to /etc/passwd, /etc/group,
		 * /etc/shadow and /etc/tacplus_conf files of host. One option is to share
		 * /etc of host with /etc of container. For now disable this and use ssh
		 * for authentication.
		 */
		/* err := PAMAuthUser(username, passwd)
		    if err != nil {
				log.Printf("Authentication failed. user=%s, error:%s", username, err.Error())
		        return err
		    }*/

		//Use ssh for authentication.
		config := &ssh.ClientConfig{
			User: username,
			Auth: []ssh.AuthMethod{
				ssh.Password(passwd),
			},
			HostKeyCallback: ssh.InsecureIgnoreHostKey(),
		}
		_, err := ssh.Dial("tcp", "127.0.0.1:22", config)
		if err != nil {
			glog.Infof("[%s] Failed to authenticate; %v", rc.ID, err)
			return httpError(http.StatusUnauthorized, "")
		}
	}
	glog.Infof("[%s] Authentication passed. user=%s ", rc.ID, username)
	//Allow SET request only if user belong to admin group
	if isWriteOperation(r) && IsAdminGroup(username, passwd) == false {
		glog.Errorf("[%s] Not an admin; cannot allow %s", rc.ID, r.Method)
		return httpError(http.StatusForbidden, "Not an admin user")
	}

	glog.Infof("[%s] Authorization passed", rc.ID)
	return nil
}

// isWriteOperation checks if the HTTP request is a write operation
func isWriteOperation(r *http.Request) bool {
	m := r.Method
	return m == "POST" || m == "PUT" || m == "PATCH" || m == "DELETE"
}

// authMiddleware function creates a middleware for request
// authentication and authorization. This middleware will return
// 401 response if authentication fails and 403 if authorization
// fails.
func authMiddleware(inner http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		rc, r := GetContext(r)
		err := PAMAuthenAndAuthor(r, rc)
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

func GenApiKey(username string) {
	
	b := make([]byte, API_KEY_LEN)
	_, err := rand.Read(b)
	if err != nil {
		fmt.Println("error:", err)
		return
	}
	api_key_file := fmt.Sprintf("%v/%v.key", API_KEY_DIR, username)
	err = ioutil.WriteFile(api_key_file, []byte(base64.StdEncoding.EncodeToString(b)), 0600)
	if err != nil {
	    panic(err)
	}
}

func DoesApiKeyExist(username string) bool {
	api_key_file := fmt.Sprintf("%v/%v.key", API_KEY_DIR, username)
	_, err := os.Stat(api_key_file)
	if os.IsNotExist(err) {
		return false
	}
	return true
}