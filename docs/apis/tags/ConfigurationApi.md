<a name="__pageTop"></a>
# fireflyiii_client.apis.tags.configuration_api.ConfigurationApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_configuration**](#get_configuration) | **get** /api/v1/configuration | Get Firefly III system configuration values.
[**get_single_configuration**](#get_single_configuration) | **get** /api/v1/configuration/{name} | Get a single Firefly III system configuration value
[**set_configuration**](#set_configuration) | **put** /api/v1/configuration/{name} | Update configuration value

# **get_configuration**
<a name="get_configuration"></a>
> ConfigurationArray get_configuration()

Get Firefly III system configuration values.

Returns all editable and not-editable configuration values for this Firefly III installation

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import fireflyiii_client
from fireflyiii_client.apis.tags import configuration_api
from fireflyiii_client.model.configuration_array import ConfigurationArray
from pprint import pprint
# Defining the host is optional and defaults to https://demo.firefly-iii.org
# See configuration.py for a list of all supported configuration parameters.
configuration = fireflyiii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = fireflyiii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with fireflyiii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Firefly III system configuration values.
        api_response = api_instance.get_configuration()
        pprint(api_response)
    except fireflyiii_client.ApiException as e:
        print("Exception when calling ConfigurationApi->get_configuration: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_configuration.ApiResponseFor200) | System configuration values

#### get_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConfigurationArray**](../../models/ConfigurationArray.md) |  | 


### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_single_configuration**
<a name="get_single_configuration"></a>
> ConfigurationSingle get_single_configuration(name)

Get a single Firefly III system configuration value

Returns one configuration variable for this Firefly III installation

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import fireflyiii_client
from fireflyiii_client.apis.tags import configuration_api
from fireflyiii_client.model.config_value_filter import ConfigValueFilter
from fireflyiii_client.model.configuration_single import ConfigurationSingle
from pprint import pprint
# Defining the host is optional and defaults to https://demo.firefly-iii.org
# See configuration.py for a list of all supported configuration parameters.
configuration = fireflyiii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = fireflyiii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with fireflyiii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': ConfigValueFilter("configuration.is_demo_site"),
    }
    try:
        # Get a single Firefly III system configuration value
        api_response = api_instance.get_single_configuration(
            path_params=path_params,
        )
        pprint(api_response)
    except fireflyiii_client.ApiException as e:
        print("Exception when calling ConfigurationApi->get_single_configuration: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 

# NameSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ConfigValueFilter**](../../models/ConfigValueFilter.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_single_configuration.ApiResponseFor200) | One system configuration value

#### get_single_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConfigurationSingle**](../../models/ConfigurationSingle.md) |  | 


### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_configuration**
<a name="set_configuration"></a>
> ConfigurationSingle set_configuration(name)

Update configuration value

Set a single configuration value. Not all configuration values can be updated so the list of accepted configuration variables is small.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import fireflyiii_client
from fireflyiii_client.apis.tags import configuration_api
from fireflyiii_client.model.configuration_update import ConfigurationUpdate
from fireflyiii_client.model.config_value_update_filter import ConfigValueUpdateFilter
from fireflyiii_client.model.validation_error import ValidationError
from fireflyiii_client.model.configuration_single import ConfigurationSingle
from pprint import pprint
# Defining the host is optional and defaults to https://demo.firefly-iii.org
# See configuration.py for a list of all supported configuration parameters.
configuration = fireflyiii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = fireflyiii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with fireflyiii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': ConfigValueUpdateFilter("configuration.is_demo_site"),
    }
    try:
        # Update configuration value
        api_response = api_instance.set_configuration(
            path_params=path_params,
        )
        pprint(api_response)
    except fireflyiii_client.ApiException as e:
        print("Exception when calling ConfigurationApi->set_configuration: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': ConfigValueUpdateFilter("configuration.is_demo_site"),
    }
    body = dict(
        value=PolymorphicProperty(None),
    )
    try:
        # Update configuration value
        api_response = api_instance.set_configuration(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except fireflyiii_client.ApiException as e:
        print("Exception when calling ConfigurationApi->set_configuration: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/x-www-form-urlencoded' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ConfigurationUpdate**](../../models/ConfigurationUpdate.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConfigurationUpdate**](../../models/ConfigurationUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 

# NameSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ConfigValueUpdateFilter**](../../models/ConfigValueUpdateFilter.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_configuration.ApiResponseFor200) | New configuration value stored, result in response.
422 | [ApiResponseFor422](#set_configuration.ApiResponseFor422) | Validation errors (see body)

#### set_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConfigurationSingle**](../../models/ConfigurationSingle.md) |  | 


#### set_configuration.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

