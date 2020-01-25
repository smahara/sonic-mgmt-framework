package custom_validation

import (
	"net"
	util "cvl/internal/util"
 )


//Validate ip address of sflow collector ip 
func (t *CustomValidation) ValidateProperIp(vc *CustValidationCtxt) CVLErrorInfo {
	ip := net.ParseIP(vc.YNodeVal)
	if ip == nil {
	         util.CVL_LEVEL_LOG(0,"%s","IP IS NIL")
                 return CVLErrorInfo{
			            ErrCode: CVL_SYNTAX_INVALID_INPUT_DATA,
				    TableName: "SFLOW_COLLECTOR",
				    CVLErrDetails : "IP address is not valid",
			    }
	}

	if ip.IsLoopback() || ip.IsUnspecified() || ip.Equal(net.IPv4bcast)|| ip.IsMulticast(){
	        util.CVL_LEVEL_LOG(0,"%s","IP IS UNSPECIFIED OR LOOPBACK OR MULTICAST OR RESERVED")
		return CVLErrorInfo{
			            ErrCode: CVL_SYNTAX_INVALID_INPUT_DATA,
				    TableName: "SFLOW_COLLECTOR",
				    CVLErrDetails : "IP address is not valid",
			    }
	}
	return CVLErrorInfo{ErrCode: CVL_SUCCESS}
}

