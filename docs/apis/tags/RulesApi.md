<a name="__pageTop"></a>
# fireflyiii_client.apis.tags.rules_api.RulesApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_rule**](#delete_rule) | **delete** /api/v1/rules/{id} | Delete an rule.
[**fire_rule**](#fire_rule) | **post** /api/v1/rules/{id}/trigger | Fire the rule on your transactions.
[**get_rule**](#get_rule) | **get** /api/v1/rules/{id} | Get a single rule.
[**list_rule**](#list_rule) | **get** /api/v1/rules | List all rules.
[**store_rule**](#store_rule) | **post** /api/v1/rules | Store a new rule
[**test_rule**](#test_rule) | **get** /api/v1/rules/{id}/test | Test which transactions would be hit by the rule. No changes will be made.
[**update_rule**](#update_rule) | **put** /api/v1/rules/{id} | Update existing rule.

# **delete_rule**
<a name="delete_rule"></a>
> delete_rule(id)

Delete an rule.

Delete an rule.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import fireflyiii_client
from fireflyiii_client.apis.tags import rules_api
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
    api_instance = rules_api.RulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    try:
        # Delete an rule.
        api_response = api_instance.delete_rule(
            path_params=path_params,
        )
    except fireflyiii_client.ApiException as e:
        print("Exception when calling RulesApi->delete_rule: %s\n" % e)
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
204 | [ApiResponseFor204](#delete_rule.ApiResponseFor204) | Rule deleted.
404 | [ApiResponseFor404](#delete_rule.ApiResponseFor404) | No such rule

#### delete_rule.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_rule.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fire_rule**
<a name="fire_rule"></a>
> fire_rule(id)

Fire the rule on your transactions.

Fire the rule group on your transactions. Changes will be made by the rules in the group! Limit the result if you want to.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import fireflyiii_client
from fireflyiii_client.apis.tags import rules_api
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
    api_instance = rules_api.RulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    query_params = {
    }
    try:
        # Fire the rule on your transactions.
        api_response = api_instance.fire_rule(
            path_params=path_params,
            query_params=query_params,
        )
    except fireflyiii_client.ApiException as e:
        print("Exception when calling RulesApi->fire_rule: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "123",
    }
    query_params = {
        'start': "Mon Sep 17 00:00:00 UTC 2018",
        'end': "Mon Sep 17 00:00:00 UTC 2018",
        'accounts[]': [1,2,3],
    }
    try:
        # Fire the rule on your transactions.
        api_response = api_instance.fire_rule(
            path_params=path_params,
            query_params=query_params,
        )
    except fireflyiii_client.ApiException as e:
        print("Exception when calling RulesApi->fire_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
start | StartSchema | | optional
end | EndSchema | | optional
accounts[] | AccountsSchema | | optional


# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# EndSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# AccountsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

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
204 | [ApiResponseFor204](#fire_rule.ApiResponseFor204) | The rules in the group are executed. Due to the setup of this function (asynchronous job execution) the result cannot be displayed.

#### fire_rule.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_rule**
<a name="get_rule"></a>
> RuleSingle get_rule(id)

Get a single rule.

Get a single rule.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import fireflyiii_client
from fireflyiii_client.apis.tags import rules_api
from fireflyiii_client.model.rule_single import RuleSingle
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
    api_instance = rules_api.RulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    try:
        # Get a single rule.
        api_response = api_instance.get_rule(
            path_params=path_params,
        )
        pprint(api_response)
    except fireflyiii_client.ApiException as e:
        print("Exception when calling RulesApi->get_rule: %s\n" % e)
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
200 | [ApiResponseFor200](#get_rule.ApiResponseFor200) | The requested rule
404 | [ApiResponseFor404](#get_rule.ApiResponseFor404) | Rule not found

#### get_rule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleSingle**](../../models/RuleSingle.md) |  | 


#### get_rule.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_rule**
<a name="list_rule"></a>
> RuleArray list_rule()

List all rules.

List all rules.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import fireflyiii_client
from fireflyiii_client.apis.tags import rules_api
from fireflyiii_client.model.rule_array import RuleArray
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
    api_instance = rules_api.RulesApi(api_client)

    # example passing only optional values
    query_params = {
        'page': 1,
    }
    try:
        # List all rules.
        api_response = api_instance.list_rule(
            query_params=query_params,
        )
        pprint(api_response)
    except fireflyiii_client.ApiException as e:
        print("Exception when calling RulesApi->list_rule: %s\n" % e)
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
200 | [ApiResponseFor200](#list_rule.ApiResponseFor200) | A list of rules

#### list_rule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleArray**](../../models/RuleArray.md) |  | 


### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **store_rule**
<a name="store_rule"></a>
> RuleSingle store_rule(rule_store)

Store a new rule

Creates a new rule. The data required can be submitted as a JSON body or as a list of parameters.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import fireflyiii_client
from fireflyiii_client.apis.tags import rules_api
from fireflyiii_client.model.rule_single import RuleSingle
from fireflyiii_client.model.rule_store import RuleStore
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
    api_instance = rules_api.RulesApi(api_client)

    # example passing only required values which don't have defaults set
    body = RuleStore(
        title="First rule title.",
        description="First rule description",
        rule_group_id="81",
        rule_group_title="New rule group",
        order=5,
        trigger=RuleTriggerType("store-journal"),
        active=True,
        strict=True,
        stop_processing=False,
        triggers=[
            RuleTriggerStore(
                type=RuleTriggerKeyword("user_action"),
                value="tag1",
                order=5,
                active=True,
                stop_processing=False,
            )
        ],
        actions=[
            RuleActionStore(
                type=RuleActionKeyword("set_category"),
                value="Daily groceries",
                order=5,
                active=True,
                stop_processing=False,
            )
        ],
    )
    try:
        # Store a new rule
        api_response = api_instance.store_rule(
            body=body,
        )
        pprint(api_response)
    except fireflyiii_client.ApiException as e:
        print("Exception when calling RulesApi->store_rule: %s\n" % e)
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
[**RuleStore**](../../models/RuleStore.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleStore**](../../models/RuleStore.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#store_rule.ApiResponseFor200) | New rule stored, result in response.
422 | [ApiResponseFor422](#store_rule.ApiResponseFor422) | Validation errors (see body)

#### store_rule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleSingle**](../../models/RuleSingle.md) |  | 


#### store_rule.ApiResponseFor422
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

# **test_rule**
<a name="test_rule"></a>
> TransactionArray test_rule(id)

Test which transactions would be hit by the rule. No changes will be made.

Test which transactions would be hit by the rule. No changes will be made. Limit the result if you want to.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import fireflyiii_client
from fireflyiii_client.apis.tags import rules_api
from fireflyiii_client.model.transaction_array import TransactionArray
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
    api_instance = rules_api.RulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    query_params = {
    }
    try:
        # Test which transactions would be hit by the rule. No changes will be made.
        api_response = api_instance.test_rule(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except fireflyiii_client.ApiException as e:
        print("Exception when calling RulesApi->test_rule: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "123",
    }
    query_params = {
        'start': "Mon Sep 17 00:00:00 UTC 2018",
        'end': "Mon Sep 17 00:00:00 UTC 2018",
        'accounts[]': [1,2,3],
    }
    try:
        # Test which transactions would be hit by the rule. No changes will be made.
        api_response = api_instance.test_rule(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except fireflyiii_client.ApiException as e:
        print("Exception when calling RulesApi->test_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
start | StartSchema | | optional
end | EndSchema | | optional
accounts[] | AccountsSchema | | optional


# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# EndSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# AccountsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

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
200 | [ApiResponseFor200](#test_rule.ApiResponseFor200) | A list of transactions that would be changed by the rule. No changes will be made.

#### test_rule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**TransactionArray**](../../models/TransactionArray.md) |  | 


### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_rule**
<a name="update_rule"></a>
> RuleSingle update_rule(idrule_update)

Update existing rule.

Update existing rule.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import fireflyiii_client
from fireflyiii_client.apis.tags import rules_api
from fireflyiii_client.model.rule_single import RuleSingle
from fireflyiii_client.model.rule_update import RuleUpdate
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
    api_instance = rules_api.RulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    body = RuleUpdate(
        title="First rule title.",
        description="First rule description",
        rule_group_id="81",
        order=5,
        trigger=RuleTriggerType("store-journal"),
        active=True,
        strict=True,
        stop_processing=False,
        triggers=[
            RuleTriggerUpdate(
                type=RuleTriggerKeyword("user_action"),
                value="tag1",
                order=5,
                active=True,
                stop_processing=False,
            )
        ],
        actions=[
            RuleActionUpdate(
                type=RuleActionKeyword("set_category"),
                value="Daily groceries",
                order=5,
                active=True,
                stop_processing=False,
            )
        ],
    )
    try:
        # Update existing rule.
        api_response = api_instance.update_rule(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except fireflyiii_client.ApiException as e:
        print("Exception when calling RulesApi->update_rule: %s\n" % e)
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
[**RuleUpdate**](../../models/RuleUpdate.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleUpdate**](../../models/RuleUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_rule.ApiResponseFor200) | Updated rule stored, result in response
422 | [ApiResponseFor422](#update_rule.ApiResponseFor422) | Validation errors (see body)

#### update_rule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleSingle**](../../models/RuleSingle.md) |  | 


#### update_rule.ApiResponseFor422
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

