<a name="__pageTop"></a>
# fireflyiii_client.apis.tags.attachments_api.AttachmentsApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_attachment**](#delete_attachment) | **delete** /api/v1/attachments/{id} | Delete an attachment.
[**download_attachment**](#download_attachment) | **get** /api/v1/attachments/{id}/download | Download a single attachment.
[**get_attachment**](#get_attachment) | **get** /api/v1/attachments/{id} | Get a single attachment.
[**list_attachment**](#list_attachment) | **get** /api/v1/attachments | List all attachments.
[**store_attachment**](#store_attachment) | **post** /api/v1/attachments | Store a new attachment.
[**update_attachment**](#update_attachment) | **put** /api/v1/attachments/{id} | Update existing attachment.
[**upload_attachment**](#upload_attachment) | **post** /api/v1/attachments/{id}/upload | Upload an attachment.

# **delete_attachment**
<a name="delete_attachment"></a>
> delete_attachment(id)

Delete an attachment.

With this endpoint you delete an attachment, including any stored file data. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import fireflyiii_client
from fireflyiii_client.apis.tags import attachments_api
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
    api_instance = attachments_api.AttachmentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    try:
        # Delete an attachment.
        api_response = api_instance.delete_attachment(
            path_params=path_params,
        )
    except fireflyiii_client.ApiException as e:
        print("Exception when calling AttachmentsApi->delete_attachment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_attachment.ApiResponseFor204) | Attachment deleted.
404 | [ApiResponseFor404](#delete_attachment.ApiResponseFor404) | No such attachment

#### delete_attachment.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_attachment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **download_attachment**
<a name="download_attachment"></a>
> file_type download_attachment(id)

Download a single attachment.

This endpoint allows you to download the binary content of a transaction. It will be sent to you as a download, using the content type \"application/octet-stream\" and content disposition \"attachment; filename=example.pdf\". 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import fireflyiii_client
from fireflyiii_client.apis.tags import attachments_api
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
    api_instance = attachments_api.AttachmentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    try:
        # Download a single attachment.
        api_response = api_instance.download_attachment(
            path_params=path_params,
        )
        pprint(api_response)
    except fireflyiii_client.ApiException as e:
        print("Exception when calling AttachmentsApi->download_attachment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/octet-stream', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#download_attachment.ApiResponseFor200) | The requested attachment
404 | [ApiResponseFor404](#download_attachment.ApiResponseFor404) | File not found

#### download_attachment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationOctetStream, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationOctetStream

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

#### download_attachment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_attachment**
<a name="get_attachment"></a>
> AttachmentSingle get_attachment(id)

Get a single attachment.

Get a single attachment. This endpoint only returns the available metadata for the attachment. Actual file data is handled in two other endpoints (see below). 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import fireflyiii_client
from fireflyiii_client.apis.tags import attachments_api
from fireflyiii_client.model.attachment_single import AttachmentSingle
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
    api_instance = attachments_api.AttachmentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    try:
        # Get a single attachment.
        api_response = api_instance.get_attachment(
            path_params=path_params,
        )
        pprint(api_response)
    except fireflyiii_client.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_attachment.ApiResponseFor200) | The requested attachment
404 | [ApiResponseFor404](#get_attachment.ApiResponseFor404) | Attachment not found

#### get_attachment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**AttachmentSingle**](../../models/AttachmentSingle.md) |  | 


#### get_attachment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_attachment**
<a name="list_attachment"></a>
> AttachmentArray list_attachment()

List all attachments.

This endpoint lists all attachments. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import fireflyiii_client
from fireflyiii_client.apis.tags import attachments_api
from fireflyiii_client.model.attachment_array import AttachmentArray
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
    api_instance = attachments_api.AttachmentsApi(api_client)

    # example passing only optional values
    query_params = {
        'page': 1,
    }
    try:
        # List all attachments.
        api_response = api_instance.list_attachment(
            query_params=query_params,
        )
        pprint(api_response)
    except fireflyiii_client.ApiException as e:
        print("Exception when calling AttachmentsApi->list_attachment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional


# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_attachment.ApiResponseFor200) | A list of attachments.

#### list_attachment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**AttachmentArray**](../../models/AttachmentArray.md) |  | 


### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **store_attachment**
<a name="store_attachment"></a>
> AttachmentSingle store_attachment(attachment_store)

Store a new attachment.

Creates a new attachment. The data required can be submitted as a JSON body or as a list of parameters. You cannot use this endpoint to upload the actual file data (see below). This endpoint only creates the attachment object. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import fireflyiii_client
from fireflyiii_client.apis.tags import attachments_api
from fireflyiii_client.model.attachment_store import AttachmentStore
from fireflyiii_client.model.attachment_single import AttachmentSingle
from fireflyiii_client.model.validation_error import ValidationError
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
    api_instance = attachments_api.AttachmentsApi(api_client)

    # example passing only required values which don't have defaults set
    body = AttachmentStore(
        filename="file.pdf",
        attachable_type=AttachableType("Bill"),
        attachable_id="134",
        title="Some PDF file",
        notes="Some notes",
    )
    try:
        # Store a new attachment.
        api_response = api_instance.store_attachment(
            body=body,
        )
        pprint(api_response)
    except fireflyiii_client.ApiException as e:
        print("Exception when calling AttachmentsApi->store_attachment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AttachmentStore**](../../models/AttachmentStore.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**AttachmentStore**](../../models/AttachmentStore.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#store_attachment.ApiResponseFor200) | New attachment stored, result in response.
422 | [ApiResponseFor422](#store_attachment.ApiResponseFor422) | Validation errors (see body)

#### store_attachment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**AttachmentSingle**](../../models/AttachmentSingle.md) |  | 


#### store_attachment.ApiResponseFor422
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

# **update_attachment**
<a name="update_attachment"></a>
> AttachmentSingle update_attachment(idattachment_update)

Update existing attachment.

Update the meta data for an existing attachment. This endpoint does not allow you to upload or download data. For that, see below. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import fireflyiii_client
from fireflyiii_client.apis.tags import attachments_api
from fireflyiii_client.model.attachment_single import AttachmentSingle
from fireflyiii_client.model.validation_error import ValidationError
from fireflyiii_client.model.attachment_update import AttachmentUpdate
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
    api_instance = attachments_api.AttachmentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    body = AttachmentUpdate(
        filename="file.pdf",
        title="Some PDF file",
        notes="Some notes",
    )
    try:
        # Update existing attachment.
        api_response = api_instance.update_attachment(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except fireflyiii_client.ApiException as e:
        print("Exception when calling AttachmentsApi->update_attachment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AttachmentUpdate**](../../models/AttachmentUpdate.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**AttachmentUpdate**](../../models/AttachmentUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_attachment.ApiResponseFor200) | Updated attachment stored, result in response
422 | [ApiResponseFor422](#update_attachment.ApiResponseFor422) | Validation errors (see body)

#### update_attachment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**AttachmentSingle**](../../models/AttachmentSingle.md) |  | 


#### update_attachment.ApiResponseFor422
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

# **upload_attachment**
<a name="upload_attachment"></a>
> upload_attachment(id)

Upload an attachment.

Use this endpoint to upload (and possible overwrite) the file contents of an attachment. Simply put the entire file in the body as binary data. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import fireflyiii_client
from fireflyiii_client.apis.tags import attachments_api
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
    api_instance = attachments_api.AttachmentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    try:
        # Upload an attachment.
        api_response = api_instance.upload_attachment(
            path_params=path_params,
        )
    except fireflyiii_client.ApiException as e:
        print("Exception when calling AttachmentsApi->upload_attachment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "123",
    }
    body = open('/path/to/file', 'rb')
    try:
        # Upload an attachment.
        api_response = api_instance.upload_attachment(
            path_params=path_params,
            body=body,
        )
    except fireflyiii_client.ApiException as e:
        print("Exception when calling AttachmentsApi->upload_attachment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationOctetStream, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/octet-stream' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationOctetStream

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#upload_attachment.ApiResponseFor204) | Upload was a success
404 | [ApiResponseFor404](#upload_attachment.ApiResponseFor404) | File not found
422 | [ApiResponseFor422](#upload_attachment.ApiResponseFor422) | Upload invalid or empty file.

#### upload_attachment.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### upload_attachment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### upload_attachment.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

