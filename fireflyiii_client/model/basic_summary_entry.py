# coding: utf-8

"""
    Firefly III API v1.5.6

    This is the documentation of the Firefly III API. You can find accompanying documentation on the website of Firefly III itself (see below). Please report any bugs or issues. You may use the \"Authorize\" button to try the API below. This file was last generated on 2022-04-04T03:54:41+00:00   # noqa: E501

    The version of the OpenAPI document: 1.5.6
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from fireflyiii_client import schemas  # noqa: F401


class BasicSummaryEntry(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            key = schemas.StrSchema
            title = schemas.StrSchema
            monetary_value = schemas.Float64Schema
            currency_id = schemas.StrSchema
            currency_code = schemas.StrSchema
            currency_symbol = schemas.StrSchema
            currency_decimal_places = schemas.Int32Schema
            value_parsed = schemas.StrSchema
            local_icon = schemas.StrSchema
            sub_title = schemas.StrSchema
            __annotations__ = {
                "key": key,
                "title": title,
                "monetary_value": monetary_value,
                "currency_id": currency_id,
                "currency_code": currency_code,
                "currency_symbol": currency_symbol,
                "currency_decimal_places": currency_decimal_places,
                "value_parsed": value_parsed,
                "local_icon": local_icon,
                "sub_title": sub_title,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["monetary_value"]) -> MetaOapg.properties.monetary_value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_id"]) -> MetaOapg.properties.currency_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_code"]) -> MetaOapg.properties.currency_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_symbol"]) -> MetaOapg.properties.currency_symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_decimal_places"]) -> MetaOapg.properties.currency_decimal_places: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value_parsed"]) -> MetaOapg.properties.value_parsed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["local_icon"]) -> MetaOapg.properties.local_icon: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sub_title"]) -> MetaOapg.properties.sub_title: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["key", "title", "monetary_value", "currency_id", "currency_code", "currency_symbol", "currency_decimal_places", "value_parsed", "local_icon", "sub_title", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> typing.Union[MetaOapg.properties.key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["monetary_value"]) -> typing.Union[MetaOapg.properties.monetary_value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_id"]) -> typing.Union[MetaOapg.properties.currency_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_code"]) -> typing.Union[MetaOapg.properties.currency_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_symbol"]) -> typing.Union[MetaOapg.properties.currency_symbol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_decimal_places"]) -> typing.Union[MetaOapg.properties.currency_decimal_places, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value_parsed"]) -> typing.Union[MetaOapg.properties.value_parsed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["local_icon"]) -> typing.Union[MetaOapg.properties.local_icon, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sub_title"]) -> typing.Union[MetaOapg.properties.sub_title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["key", "title", "monetary_value", "currency_id", "currency_code", "currency_symbol", "currency_decimal_places", "value_parsed", "local_icon", "sub_title", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        key: typing.Union[MetaOapg.properties.key, str, schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        monetary_value: typing.Union[MetaOapg.properties.monetary_value, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        currency_id: typing.Union[MetaOapg.properties.currency_id, str, schemas.Unset] = schemas.unset,
        currency_code: typing.Union[MetaOapg.properties.currency_code, str, schemas.Unset] = schemas.unset,
        currency_symbol: typing.Union[MetaOapg.properties.currency_symbol, str, schemas.Unset] = schemas.unset,
        currency_decimal_places: typing.Union[MetaOapg.properties.currency_decimal_places, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        value_parsed: typing.Union[MetaOapg.properties.value_parsed, str, schemas.Unset] = schemas.unset,
        local_icon: typing.Union[MetaOapg.properties.local_icon, str, schemas.Unset] = schemas.unset,
        sub_title: typing.Union[MetaOapg.properties.sub_title, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BasicSummaryEntry':
        return super().__new__(
            cls,
            *_args,
            key=key,
            title=title,
            monetary_value=monetary_value,
            currency_id=currency_id,
            currency_code=currency_code,
            currency_symbol=currency_symbol,
            currency_decimal_places=currency_decimal_places,
            value_parsed=value_parsed,
            local_icon=local_icon,
            sub_title=sub_title,
            _configuration=_configuration,
            **kwargs,
        )
