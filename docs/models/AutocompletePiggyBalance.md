# fireflyiii_client.model.autocomplete_piggy_balance.AutocompletePiggyBalance

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Name of the piggy bank found by an auto-complete search. | 
**id** | str,  | str,  |  | 
**name_with_balance** | str,  | str,  | Name of the piggy bank found by an auto-complete search with the current balance formatted nicely. | [optional] 
**object_group_id** | None, str,  | NoneClass, str,  | The group ID of the group this object is part of. NULL if no group. | [optional] 
**object_group_title** | None, str,  | NoneClass, str,  | The name of the group. NULL if no group. | [optional] 
**currency_id** | str,  | str,  | Currency ID for this piggy bank. | [optional] 
**currency_code** | str,  | str,  | Currency code for this piggy bank. | [optional] 
**currency_symbol** | str,  | str,  |  | [optional] 
**currency_decimal_places** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

