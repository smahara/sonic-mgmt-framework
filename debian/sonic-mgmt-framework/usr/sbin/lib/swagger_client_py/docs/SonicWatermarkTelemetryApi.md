# sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi

All URIs are relative to *https://localhost/restconf/data*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sonic_watermark_telemetry_watermark_table**](SonicWatermarkTelemetryApi.md#delete_sonic_watermark_telemetry_watermark_table) | **DELETE** /sonic-watermark-telemetry:WATERMARK_TABLE | 
[**delete_sonic_watermark_telemetry_watermark_table_interval**](SonicWatermarkTelemetryApi.md#delete_sonic_watermark_telemetry_watermark_table_interval) | **DELETE** /sonic-watermark-telemetry:WATERMARK_TABLE/interval | 
[**get_sonic_watermark_telemetry_watermark_table**](SonicWatermarkTelemetryApi.md#get_sonic_watermark_telemetry_watermark_table) | **GET** /sonic-watermark-telemetry:WATERMARK_TABLE | 
[**get_sonic_watermark_telemetry_watermark_table_interval**](SonicWatermarkTelemetryApi.md#get_sonic_watermark_telemetry_watermark_table_interval) | **GET** /sonic-watermark-telemetry:WATERMARK_TABLE/interval | 
[**patch_sonic_watermark_telemetry_watermark_table**](SonicWatermarkTelemetryApi.md#patch_sonic_watermark_telemetry_watermark_table) | **PATCH** /sonic-watermark-telemetry:WATERMARK_TABLE | 
[**patch_sonic_watermark_telemetry_watermark_table_interval**](SonicWatermarkTelemetryApi.md#patch_sonic_watermark_telemetry_watermark_table_interval) | **PATCH** /sonic-watermark-telemetry:WATERMARK_TABLE/interval | 
[**post_sonic_watermark_telemetry_watermark_table_interval**](SonicWatermarkTelemetryApi.md#post_sonic_watermark_telemetry_watermark_table_interval) | **POST** /sonic-watermark-telemetry:WATERMARK_TABLE | 
[**put_sonic_watermark_telemetry_watermark_table**](SonicWatermarkTelemetryApi.md#put_sonic_watermark_telemetry_watermark_table) | **PUT** /sonic-watermark-telemetry:WATERMARK_TABLE | 
[**put_sonic_watermark_telemetry_watermark_table_interval**](SonicWatermarkTelemetryApi.md#put_sonic_watermark_telemetry_watermark_table_interval) | **PUT** /sonic-watermark-telemetry:WATERMARK_TABLE/interval | 


# **delete_sonic_watermark_telemetry_watermark_table**
> delete_sonic_watermark_telemetry_watermark_table()



OperationId: delete_sonic_watermark_telemetry_watermark_table 

### Example
```python
from __future__ import print_function
import time
import sonic_watermark_telemetry_client
from sonic_watermark_telemetry_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi()

try:
    api_instance.delete_sonic_watermark_telemetry_watermark_table()
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->delete_sonic_watermark_telemetry_watermark_table: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_watermark_telemetry_watermark_table_interval**
> delete_sonic_watermark_telemetry_watermark_table_interval()



OperationId: delete_sonic_watermark_telemetry_watermark_table_interval 

### Example
```python
from __future__ import print_function
import time
import sonic_watermark_telemetry_client
from sonic_watermark_telemetry_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi()

try:
    api_instance.delete_sonic_watermark_telemetry_watermark_table_interval()
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->delete_sonic_watermark_telemetry_watermark_table_interval: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_watermark_telemetry_watermark_table**
> GetSonicWatermarkTelemetryWatermarkTable get_sonic_watermark_telemetry_watermark_table()



OperationId: get_sonic_watermark_telemetry_watermark_table 

### Example
```python
from __future__ import print_function
import time
import sonic_watermark_telemetry_client
from sonic_watermark_telemetry_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi()

try:
    api_response = api_instance.get_sonic_watermark_telemetry_watermark_table()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->get_sonic_watermark_telemetry_watermark_table: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSonicWatermarkTelemetryWatermarkTable**](GetSonicWatermarkTelemetryWatermarkTable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_watermark_telemetry_watermark_table_interval**
> GetSonicWatermarkTelemetryWatermarkTableInterval get_sonic_watermark_telemetry_watermark_table_interval()



OperationId: get_sonic_watermark_telemetry_watermark_table_interval 

### Example
```python
from __future__ import print_function
import time
import sonic_watermark_telemetry_client
from sonic_watermark_telemetry_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi()

try:
    api_response = api_instance.get_sonic_watermark_telemetry_watermark_table_interval()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->get_sonic_watermark_telemetry_watermark_table_interval: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSonicWatermarkTelemetryWatermarkTableInterval**](GetSonicWatermarkTelemetryWatermarkTableInterval.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_watermark_telemetry_watermark_table**
> patch_sonic_watermark_telemetry_watermark_table(body)



OperationId: patch_sonic_watermark_telemetry_watermark_table 

### Example
```python
from __future__ import print_function
import time
import sonic_watermark_telemetry_client
from sonic_watermark_telemetry_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi()
body = sonic_watermark_telemetry_client.PatchSonicWatermarkTelemetryWatermarkTable() # PatchSonicWatermarkTelemetryWatermarkTable | 

try:
    api_instance.patch_sonic_watermark_telemetry_watermark_table(body)
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->patch_sonic_watermark_telemetry_watermark_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchSonicWatermarkTelemetryWatermarkTable**](PatchSonicWatermarkTelemetryWatermarkTable.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_watermark_telemetry_watermark_table_interval**
> patch_sonic_watermark_telemetry_watermark_table_interval(body)



OperationId: patch_sonic_watermark_telemetry_watermark_table_interval 

### Example
```python
from __future__ import print_function
import time
import sonic_watermark_telemetry_client
from sonic_watermark_telemetry_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi()
body = sonic_watermark_telemetry_client.PatchSonicWatermarkTelemetryWatermarkTableInterval() # PatchSonicWatermarkTelemetryWatermarkTableInterval | 

try:
    api_instance.patch_sonic_watermark_telemetry_watermark_table_interval(body)
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->patch_sonic_watermark_telemetry_watermark_table_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchSonicWatermarkTelemetryWatermarkTableInterval**](PatchSonicWatermarkTelemetryWatermarkTableInterval.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sonic_watermark_telemetry_watermark_table_interval**
> post_sonic_watermark_telemetry_watermark_table_interval(body)



OperationId: post_sonic_watermark_telemetry_watermark_table_interval 

### Example
```python
from __future__ import print_function
import time
import sonic_watermark_telemetry_client
from sonic_watermark_telemetry_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi()
body = sonic_watermark_telemetry_client.PostSonicWatermarkTelemetryWatermarkTableInterval() # PostSonicWatermarkTelemetryWatermarkTableInterval | 

try:
    api_instance.post_sonic_watermark_telemetry_watermark_table_interval(body)
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->post_sonic_watermark_telemetry_watermark_table_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostSonicWatermarkTelemetryWatermarkTableInterval**](PostSonicWatermarkTelemetryWatermarkTableInterval.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_watermark_telemetry_watermark_table**
> put_sonic_watermark_telemetry_watermark_table(body)



OperationId: put_sonic_watermark_telemetry_watermark_table 

### Example
```python
from __future__ import print_function
import time
import sonic_watermark_telemetry_client
from sonic_watermark_telemetry_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi()
body = sonic_watermark_telemetry_client.PutSonicWatermarkTelemetryWatermarkTable() # PutSonicWatermarkTelemetryWatermarkTable | 

try:
    api_instance.put_sonic_watermark_telemetry_watermark_table(body)
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->put_sonic_watermark_telemetry_watermark_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutSonicWatermarkTelemetryWatermarkTable**](PutSonicWatermarkTelemetryWatermarkTable.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_watermark_telemetry_watermark_table_interval**
> put_sonic_watermark_telemetry_watermark_table_interval(body)



OperationId: put_sonic_watermark_telemetry_watermark_table_interval 

### Example
```python
from __future__ import print_function
import time
import sonic_watermark_telemetry_client
from sonic_watermark_telemetry_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi()
body = sonic_watermark_telemetry_client.PutSonicWatermarkTelemetryWatermarkTableInterval() # PutSonicWatermarkTelemetryWatermarkTableInterval | 

try:
    api_instance.put_sonic_watermark_telemetry_watermark_table_interval(body)
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->put_sonic_watermark_telemetry_watermark_table_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutSonicWatermarkTelemetryWatermarkTableInterval**](PutSonicWatermarkTelemetryWatermarkTableInterval.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

