# fireflyiii_client.model.transaction_link_update.TransactionLinkUpdate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**link_type_id** | str,  | str,  | The link type ID to use. Use this field OR use the link_type_name field. | [optional] 
**link_type_name** | str,  | str,  | The link type name to use. Use this field OR use the link_type_id field. | [optional] 
**inward_id** | str,  | str,  | The inward transaction transaction_journal_id for the link. This becomes the &#x27;is paid by&#x27; transaction of the set. | [optional] 
**outward_id** | str,  | str,  | The outward transaction transaction_journal_id for the link. This becomes the &#x27;pays for&#x27; transaction of the set. | [optional] 
**notes** | None, str,  | NoneClass, str,  | Optional. Some notes. If you submit an empty string the current notes will be removed | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

