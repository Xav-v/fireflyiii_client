# fireflyiii_client.model.insight_group_entry.InsightGroupEntry

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | This ID is a reference to the original object. | [optional] 
**name** | str,  | str,  | This is the name of the object. | [optional] 
**difference** | str,  | str,  | The amount spent or earned between start date and end date, a number defined as a string, for this object and all asset accounts. | [optional] 
**difference_float** | decimal.Decimal, int, float,  | decimal.Decimal,  | The amount spent or earned between start date and end date, a number as a float, for this object and all asset accounts. May have rounding errors. | [optional] value must be a 64 bit float
**currency_id** | str,  | str,  | The currency ID of the expenses listed for this account. | [optional] 
**currency_code** | str,  | str,  | The currency code of the expenses listed for this account. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

