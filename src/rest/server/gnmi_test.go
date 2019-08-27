///////////////////////////////////////////////////////////////////////
//
// Copyright 2019 Broadcom. All rights reserved.
// The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.
//
///////////////////////////////////////////////////////////////////////

package server

import (
    "fmt"
    "time"
    "crypto/tls"
    "golang.org/x/net/context"
    "google.golang.org/grpc"
    "google.golang.org/grpc/credentials"
    "testing"
    "encoding/json"
    // "log"
    pb "github.com/openconfig/gnmi/proto/gnmi"

)
func init() {
	fmt.Println("+++++ init gnmi_test +++++")
}


func TestCapabilities(t *testing.T) {
    tlsConfig := &tls.Config{InsecureSkipVerify: true}
    opts := []grpc.DialOption{grpc.WithTransportCredentials(credentials.NewTLS(tlsConfig))}

    conn, err := grpc.Dial("127.0.0.1:8080", opts...)
    if err != nil {
        t.Fatalf("Failed to connect to gNMI")
    }
    defer conn.Close()
    cli := pb.NewGNMIClient(conn)
    ctx, cancel := context.WithTimeout(context.Background(), 500*time.Millisecond)
    defer cancel()

    var req pb.CapabilityRequest
    resp,err := cli.Capabilities(ctx, &req)
    if err != nil {
        t.Fatalf("Failed to get Capabilities")
    }
    if len(resp.SupportedModels) == 0 {
    	t.Fatalf("No Supported Models found!")
    }

}

func TestGetIfaces(t *testing.T) {
    tlsConfig := &tls.Config{InsecureSkipVerify: true}
    opts := []grpc.DialOption{grpc.WithTransportCredentials(credentials.NewTLS(tlsConfig))}

    conn, err := grpc.Dial("127.0.0.1:8080", opts...)
    if err != nil {
        t.Fatalf("Failed to connect to gNMI")
    }
    defer conn.Close()
    cli := pb.NewGNMIClient(conn)
    ctx, cancel := context.WithTimeout(context.Background(), 500*time.Millisecond)
    defer cancel()

    req2 := &pb.GetRequest{
        Path: []*pb.Path{&pb.Path{Elem: []*pb.PathElem{&pb.PathElem{
            Name: "openconfig-interfaces:interfaces",
        }}}},
    }

    resp2, err := cli.Get(ctx, req2)
    if err != nil {
        t.Fatalf("Failed to get interfaces")
    }
    var jresp interface{}
    switch x := resp2.Notification[0].Update[0].Val.Value.(type) {
    case *pb.TypedValue_JsonIetfVal:
    	err := json.Unmarshal(x.JsonIetfVal, &jresp)
    	if err != nil {
    		t.Fatalf("Failed to Unmarshal json: %v", err)
    	}
    	
    	if ifaces, ok := jresp.(map[string]interface{})["openconfig-interfaces:interfaces"]; ok {
    		if iface, ok := ifaces.(map[string]interface{})["interface"]; ok {
    			if len(iface.([]interface{})) == 0  {
    				t.Fatalf("No interfaces found!")
    			}
    			//We could compare to expected json here
    		}
    	}
    default:
    	t.Fatalf("Return datatype is not json_ietf!")
	}

    
}