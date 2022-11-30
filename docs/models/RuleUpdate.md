# fireflyiii_client.model.rule_update.RuleUpdate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**title** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**rule_group_id** | str,  | str,  | ID of the rule group under which the rule must be stored. Either this field or rule_group_title is mandatory. | [optional] 
**order** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**trigger** | [**RuleTriggerType**](RuleTriggerType.md) | [**RuleTriggerType**](RuleTriggerType.md) |  | [optional] 
**active** | bool,  | BoolClass,  | Whether or not the rule is even active. Default is true. | [optional] if omitted the server will use the default value of True
**strict** | bool,  | BoolClass,  | If the rule is set to be strict, ALL triggers must hit in order for the rule to fire. Otherwise, just one is enough. Default value is true. | [optional] 
**stop_processing** | bool,  | BoolClass,  | If this value is true and the rule is triggered, other rules  after this one in the group will be skipped. Default value is false. | [optional] if omitted the server will use the default value of False
**[triggers](#triggers)** | list, tuple,  | tuple,  |  | [optional] 
**[actions](#actions)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# triggers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RuleTriggerUpdate**](RuleTriggerUpdate.md) | [**RuleTriggerUpdate**](RuleTriggerUpdate.md) | [**RuleTriggerUpdate**](RuleTriggerUpdate.md) |  | 

# actions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RuleActionUpdate**](RuleActionUpdate.md) | [**RuleActionUpdate**](RuleActionUpdate.md) | [**RuleActionUpdate**](RuleActionUpdate.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

