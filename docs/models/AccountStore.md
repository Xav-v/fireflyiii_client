# fireflyiii_client.model.account_store.AccountStore

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | 
**type** | [**ShortAccountTypeProperty**](ShortAccountTypeProperty.md) | [**ShortAccountTypeProperty**](ShortAccountTypeProperty.md) |  | 
**iban** | None, str,  | NoneClass, str,  |  | [optional] 
**bic** | None, str,  | NoneClass, str,  |  | [optional] 
**account_number** | None, str,  | NoneClass, str,  |  | [optional] 
**opening_balance** | str,  | str,  | Represents the opening balance, the initial amount this account holds. | [optional] 
**opening_balance_date** | None, str, date,  | NoneClass, str,  | Represents the date of the opening balance. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**virtual_balance** | str,  | str,  |  | [optional] 
**currency_id** | str,  | str,  | Use either currency_id or currency_code. Defaults to the user&#x27;s default currency. | [optional] 
**currency_code** | str,  | str,  | Use either currency_id or currency_code. Defaults to the user&#x27;s default currency. | [optional] 
**active** | bool,  | BoolClass,  | If omitted, defaults to true. | [optional] if omitted the server will use the default value of True
**order** | decimal.Decimal, int,  | decimal.Decimal,  | Order of the account | [optional] value must be a 32 bit integer
**include_net_worth** | bool,  | BoolClass,  | If omitted, defaults to true. | [optional] if omitted the server will use the default value of True
**account_role** | [**AccountRoleProperty**](AccountRoleProperty.md) | [**AccountRoleProperty**](AccountRoleProperty.md) |  | [optional] 
**credit_card_type** | [**CreditCardType**](CreditCardType.md) | [**CreditCardType**](CreditCardType.md) |  | [optional] 
**monthly_payment_date** | None, str, date,  | NoneClass, str,  | Mandatory when the account_role is ccAsset. Moment at which CC payment installments are asked for by the bank. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**liability_type** | [**LiabilityType**](LiabilityType.md) | [**LiabilityType**](LiabilityType.md) |  | [optional] 
**liability_direction** | [**LiabilityDirection**](LiabilityDirection.md) | [**LiabilityDirection**](LiabilityDirection.md) |  | [optional] 
**interest** | None, str,  | NoneClass, str,  | Mandatory when type is liability. Interest percentage. | [optional] if omitted the server will use the default value of "0"
**interest_period** | [**InterestPeriod**](InterestPeriod.md) | [**InterestPeriod**](InterestPeriod.md) |  | [optional] 
**notes** | None, str,  | NoneClass, str,  |  | [optional] 
**latitude** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Latitude of the accounts&#x27;s location, if applicable. Can be used to draw a map. | [optional] value must be a 64 bit float
**longitude** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Latitude of the accounts&#x27;s location, if applicable. Can be used to draw a map. | [optional] value must be a 64 bit float
**zoom_level** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Zoom level for the map, if drawn. This to set the box right. Unfortunately this is a proprietary value because each map provider has different zoom levels. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
