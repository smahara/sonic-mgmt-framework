package main

import (
	"crypto/rand"
	"fmt"
	"encoding/base64"
	"os"
	"io/ioutil"
)

func main() {
	if len(os.Args) < 2 {
		panic("Must specify username")
	}
	username := os.Args[1]
	c := 10
	b := make([]byte, c)
	_, err := rand.Read(b)
	if err != nil {
		fmt.Println("error:", err)
		return
	}
	// api_key := fmt.Sprintf("%v:%v\n", username, base64.StdEncoding.EncodeToString(b))
	api_key_file := fmt.Sprintf("/etc/rest_api_keys/%v.key", username)
	err = ioutil.WriteFile(api_key_file, []byte(base64.StdEncoding.EncodeToString(b)), 0600)
	if err != nil {
	    panic(err)
	}

}
