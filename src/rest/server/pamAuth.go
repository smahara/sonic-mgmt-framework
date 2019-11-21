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

package server

import (
	"net/http"
	"os/user"
	"github.com/golang/glog"
	"github.com/msteinert/pam"
	"errors"
)


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


func PopulateAuthStruct(username string, auth *AuthInfo) error {
	usr, err := user.Lookup(username)
	if err != nil {
		return err
	}

	auth.User = username

	// Get primary group
	group, err := user.LookupGroupId(usr.Gid)
	if err != nil {
		return err
	}
	auth.Group = group.Name

	// Lookup remaining groups
	gids, err := usr.GroupIds()
	if err != nil {
		return err
	}
	auth.Groups = make([]string, len(gids))
	for idx, gid := range gids {
		group, err := user.LookupGroupId(gid)
		if err != nil {
			return err
		}
		auth.Groups[idx] = group.Name
	}

	// TODO: Populate roles list
	return nil
}


func DoesUserExist(username string) bool {
	_, err := user.Lookup(username)
	if err != nil {
		return false
	}
	return true
}

func UserPwAuth(username string, passwd string) (bool, error) {
	/*
	 * mgmt-framework container does not have access to /etc/passwd, /etc/group,
	 * /etc/shadow and /etc/tacplus_conf files of host. One option is to share
	 * /etc of host with /etc of container. For now disable this and use ssh
	 * for authentication.
	 */
	err := PAMAuthUser(username, passwd)
    if err != nil {
		glog.Infof("Authentication failed. user=%s, error:%s", username, err.Error())
        return false, err
    }

	return true, nil
}

// isWriteOperation checks if the HTTP request is a write operation
func isWriteOperation(r *http.Request) bool {
	m := r.Method
	return m == "POST" || m == "PUT" || m == "PATCH" || m == "DELETE"
}

