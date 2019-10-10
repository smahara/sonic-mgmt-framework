# vlan_client.VlanApi

All URIs are relative to *https://localhost/nonyang*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_vlan_members**](VlanApi.md#add_vlan_members) | **POST** /vlan/{id}/member | Add member interfaces
[**create_vlans**](VlanApi.md#create_vlans) | **POST** /vlan | Create vlans
[**delete_vlan_by_id**](VlanApi.md#delete_vlan_by_id) | **DELETE** /vlan/{id} | Delete vlan by id
[**get_vlan_by_id**](VlanApi.md#get_vlan_by_id) | **GET** /vlan/{id} | Finds vlan by id
[**get_vlans**](VlanApi.md#get_vlans) | **GET** /vlan | Get all vlan
[**remove_vlan_members**](VlanApi.md#remove_vlan_members) | **DELETE** /vlan/{id}/member/{port} | Remove member interfaces


# **add_vlan_members**
> add_vlan_members(id, body)

Add member interfaces

Add member interfaces

### Example
```python
from __future__ import print_function
import time
import vlan_client
from vlan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vlan_client.VlanApi()
id = 56 # int | Vlan id
body = [vlan_client.VlanMember()] # list[VlanMember] | Member info

try:
    # Add member interfaces
    api_instance.add_vlan_members(id, body)
except ApiException as e:
    print("Exception when calling VlanApi->add_vlan_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Vlan id | 
 **body** | [**list[VlanMember]**](VlanMember.md)| Member info | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vlans**
> create_vlans(body)

Create vlans

Create vlans by id

### Example
```python
from __future__ import print_function
import time
import vlan_client
from vlan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vlan_client.VlanApi()
body = [vlan_client.list[int]()] # list[int] | Vlans to be configured

try:
    # Create vlans
    api_instance.create_vlans(body)
except ApiException as e:
    print("Exception when calling VlanApi->create_vlans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[int]**| Vlans to be configured | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vlan_by_id**
> delete_vlan_by_id(id)

Delete vlan by id

Delete vlan by id

### Example
```python
from __future__ import print_function
import time
import vlan_client
from vlan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vlan_client.VlanApi()
id = 56 # int | Vlan id

try:
    # Delete vlan by id
    api_instance.delete_vlan_by_id(id)
except ApiException as e:
    print("Exception when calling VlanApi->delete_vlan_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Vlan id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vlan_by_id**
> VlanInfo get_vlan_by_id(id)

Finds vlan by id

Returns vlan by id

### Example
```python
from __future__ import print_function
import time
import vlan_client
from vlan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vlan_client.VlanApi()
id = 56 # int | Vlan id

try:
    # Finds vlan by id
    api_response = api_instance.get_vlan_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VlanApi->get_vlan_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Vlan id | 

### Return type

[**VlanInfo**](VlanInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vlans**
> list[VlanInfo] get_vlans()

Get all vlan

Returns all vlans

### Example
```python
from __future__ import print_function
import time
import vlan_client
from vlan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vlan_client.VlanApi()

try:
    # Get all vlan
    api_response = api_instance.get_vlans()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VlanApi->get_vlans: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VlanInfo]**](VlanInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_vlan_members**
> remove_vlan_members(id, port)

Remove member interfaces

Remove member interfaces

### Example
```python
from __future__ import print_function
import time
import vlan_client
from vlan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vlan_client.VlanApi()
id = 56 # int | Vlan id
port = 'port_example' # str | Member port name

try:
    # Remove member interfaces
    api_instance.remove_vlan_members(id, port)
except ApiException as e:
    print("Exception when calling VlanApi->remove_vlan_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Vlan id | 
 **port** | **str**| Member port name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

