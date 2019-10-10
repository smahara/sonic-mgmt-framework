# sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi

All URIs are relative to *https://localhost/restconf/data*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sonic_watermark_telemetry_sonic_watermark_telemetry**](SonicWatermarkTelemetryApi.md#delete_sonic_watermark_telemetry_sonic_watermark_telemetry) | **DELETE** /sonic-watermark-telemetry:sonic-watermark-telemetry | 
[**delete_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table**](SonicWatermarkTelemetryApi.md#delete_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table) | **DELETE** /sonic-watermark-telemetry:sonic-watermark-telemetry/WATERMARK_TABLE | 
[**delete_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval**](SonicWatermarkTelemetryApi.md#delete_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval) | **DELETE** /sonic-watermark-telemetry:sonic-watermark-telemetry/WATERMARK_TABLE/interval | 
[**get_sonic_watermark_telemetry_sonic_watermark_telemetry**](SonicWatermarkTelemetryApi.md#get_sonic_watermark_telemetry_sonic_watermark_telemetry) | **GET** /sonic-watermark-telemetry:sonic-watermark-telemetry | 
[**get_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table**](SonicWatermarkTelemetryApi.md#get_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table) | **GET** /sonic-watermark-telemetry:sonic-watermark-telemetry/WATERMARK_TABLE | 
[**get_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval**](SonicWatermarkTelemetryApi.md#get_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval) | **GET** /sonic-watermark-telemetry:sonic-watermark-telemetry/WATERMARK_TABLE/interval | 
[**patch_sonic_watermark_telemetry_sonic_watermark_telemetry**](SonicWatermarkTelemetryApi.md#patch_sonic_watermark_telemetry_sonic_watermark_telemetry) | **PATCH** /sonic-watermark-telemetry:sonic-watermark-telemetry | 
[**patch_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table**](SonicWatermarkTelemetryApi.md#patch_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table) | **PATCH** /sonic-watermark-telemetry:sonic-watermark-telemetry/WATERMARK_TABLE | 
[**patch_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval**](SonicWatermarkTelemetryApi.md#patch_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval) | **PATCH** /sonic-watermark-telemetry:sonic-watermark-telemetry/WATERMARK_TABLE/interval | 
[**post_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table**](SonicWatermarkTelemetryApi.md#post_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table) | **POST** /sonic-watermark-telemetry:sonic-watermark-telemetry | 
[**post_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval**](SonicWatermarkTelemetryApi.md#post_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval) | **POST** /sonic-watermark-telemetry:sonic-watermark-telemetry/WATERMARK_TABLE | 
[**put_sonic_watermark_telemetry_sonic_watermark_telemetry**](SonicWatermarkTelemetryApi.md#put_sonic_watermark_telemetry_sonic_watermark_telemetry) | **PUT** /sonic-watermark-telemetry:sonic-watermark-telemetry | 
[**put_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table**](SonicWatermarkTelemetryApi.md#put_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table) | **PUT** /sonic-watermark-telemetry:sonic-watermark-telemetry/WATERMARK_TABLE | 
[**put_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval**](SonicWatermarkTelemetryApi.md#put_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval) | **PUT** /sonic-watermark-telemetry:sonic-watermark-telemetry/WATERMARK_TABLE/interval | 


# **delete_sonic_watermark_telemetry_sonic_watermark_telemetry**
> delete_sonic_watermark_telemetry_sonic_watermark_telemetry()



OperationId: delete_sonic_watermark_telemetry_sonic_watermark_telemetry 

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
    api_instance.delete_sonic_watermark_telemetry_sonic_watermark_telemetry()
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->delete_sonic_watermark_telemetry_sonic_watermark_telemetry: %s\n" % e)
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

# **delete_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table**
> delete_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table()



OperationId: delete_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table 

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
    api_instance.delete_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table()
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->delete_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table: %s\n" % e)
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

# **delete_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval**
> delete_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval()



OperationId: delete_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval 

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
    api_instance.delete_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval()
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->delete_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval: %s\n" % e)
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

# **get_sonic_watermark_telemetry_sonic_watermark_telemetry**
> GetSonicWatermarkTelemetrySonicWatermarkTelemetry get_sonic_watermark_telemetry_sonic_watermark_telemetry()



OperationId: get_sonic_watermark_telemetry_sonic_watermark_telemetry 

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
    api_response = api_instance.get_sonic_watermark_telemetry_sonic_watermark_telemetry()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->get_sonic_watermark_telemetry_sonic_watermark_telemetry: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSonicWatermarkTelemetrySonicWatermarkTelemetry**](GetSonicWatermarkTelemetrySonicWatermarkTelemetry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table**
> GetSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTable get_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table()



OperationId: get_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table 

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
    api_response = api_instance.get_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->get_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTable**](GetSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval**
> GetSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTableInterval get_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval()



OperationId: get_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval 

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
    api_response = api_instance.get_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->get_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTableInterval**](GetSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTableInterval.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_watermark_telemetry_sonic_watermark_telemetry**
> patch_sonic_watermark_telemetry_sonic_watermark_telemetry(body)



OperationId: patch_sonic_watermark_telemetry_sonic_watermark_telemetry 

### Example
```python
from __future__ import print_function
import time
import sonic_watermark_telemetry_client
from sonic_watermark_telemetry_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi()
body = sonic_watermark_telemetry_client.PatchSonicWatermarkTelemetrySonicWatermarkTelemetry() # PatchSonicWatermarkTelemetrySonicWatermarkTelemetry | 

try:
    api_instance.patch_sonic_watermark_telemetry_sonic_watermark_telemetry(body)
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->patch_sonic_watermark_telemetry_sonic_watermark_telemetry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchSonicWatermarkTelemetrySonicWatermarkTelemetry**](PatchSonicWatermarkTelemetrySonicWatermarkTelemetry.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table**
> patch_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table(body)



OperationId: patch_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table 

### Example
```python
from __future__ import print_function
import time
import sonic_watermark_telemetry_client
from sonic_watermark_telemetry_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi()
body = sonic_watermark_telemetry_client.PatchSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTable() # PatchSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTable | 

try:
    api_instance.patch_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table(body)
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->patch_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTable**](PatchSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTable.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval**
> patch_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval(body)



OperationId: patch_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval 

### Example
```python
from __future__ import print_function
import time
import sonic_watermark_telemetry_client
from sonic_watermark_telemetry_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi()
body = sonic_watermark_telemetry_client.PatchSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTableInterval() # PatchSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTableInterval | 

try:
    api_instance.patch_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval(body)
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->patch_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTableInterval**](PatchSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTableInterval.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table**
> post_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table(body)



OperationId: post_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table 

### Example
```python
from __future__ import print_function
import time
import sonic_watermark_telemetry_client
from sonic_watermark_telemetry_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi()
body = sonic_watermark_telemetry_client.PostSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTable() # PostSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTable | 

try:
    api_instance.post_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table(body)
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->post_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTable**](PostSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTable.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval**
> post_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval(body)



OperationId: post_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval 

### Example
```python
from __future__ import print_function
import time
import sonic_watermark_telemetry_client
from sonic_watermark_telemetry_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi()
body = sonic_watermark_telemetry_client.PostSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTableInterval() # PostSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTableInterval | 

try:
    api_instance.post_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval(body)
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->post_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTableInterval**](PostSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTableInterval.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_watermark_telemetry_sonic_watermark_telemetry**
> put_sonic_watermark_telemetry_sonic_watermark_telemetry(body)



OperationId: put_sonic_watermark_telemetry_sonic_watermark_telemetry 

### Example
```python
from __future__ import print_function
import time
import sonic_watermark_telemetry_client
from sonic_watermark_telemetry_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi()
body = sonic_watermark_telemetry_client.PutSonicWatermarkTelemetrySonicWatermarkTelemetry() # PutSonicWatermarkTelemetrySonicWatermarkTelemetry | 

try:
    api_instance.put_sonic_watermark_telemetry_sonic_watermark_telemetry(body)
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->put_sonic_watermark_telemetry_sonic_watermark_telemetry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutSonicWatermarkTelemetrySonicWatermarkTelemetry**](PutSonicWatermarkTelemetrySonicWatermarkTelemetry.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table**
> put_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table(body)



OperationId: put_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table 

### Example
```python
from __future__ import print_function
import time
import sonic_watermark_telemetry_client
from sonic_watermark_telemetry_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi()
body = sonic_watermark_telemetry_client.PutSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTable() # PutSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTable | 

try:
    api_instance.put_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table(body)
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->put_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTable**](PutSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTable.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval**
> put_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval(body)



OperationId: put_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval 

### Example
```python
from __future__ import print_function
import time
import sonic_watermark_telemetry_client
from sonic_watermark_telemetry_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_watermark_telemetry_client.SonicWatermarkTelemetryApi()
body = sonic_watermark_telemetry_client.PutSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTableInterval() # PutSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTableInterval | 

try:
    api_instance.put_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval(body)
except ApiException as e:
    print("Exception when calling SonicWatermarkTelemetryApi->put_sonic_watermark_telemetry_sonic_watermark_telemetry_watermark_table_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTableInterval**](PutSonicWatermarkTelemetrySonicWatermarkTelemetryWatermarkTableInterval.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

