package custom_validation

import (
	"net"
	log "github.com/golang/glog"
 )



//Validate ip address of sflow collector ip 
func (t *CustomValidation) ValidateProperIp(vc *CustValidationCtxt) CVLErrorInfo {
 	log.Info("Entered custom validation ValidateProperIp")
	/*if (vc.YNodeName != "collector_ip") {
	         log.Info("CVL validatuion, not called for collector ip")
		 return CVLErrorInfo{ErrCode: CVL_FAILURE}
	}
*/	log.Info("Given IP sflow:",vc.YNodeVal)
	ip := net.ParseIP(vc.YNodeVal)
	if ip == nil {
                 return CVLErrorInfo{
			            ErrCode: CVL_SYNTAX_INVALID_INPUT_DATA,
				    TableName: "SFLOW_COLLECTOR",
				    CVLErrDetails : "IP address is not valid",
			    }
	}
	if ip.IsLoopback() || ip.IsUnspecified() || ip.IsMulticast() || ip.IsGlobalUnicast() {
                 return CVLErrorInfo{
			            ErrCode: CVL_SYNTAX_INVALID_INPUT_DATA,
				    TableName: "SFLOW_COLLECTOR",
				    CVLErrDetails : "IP address is not valid",
			    }
	}
	return CVLErrorInfo{ErrCode: CVL_SUCCESS}
}

