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


class RecurrenceRepetitionUpdate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def type() -> typing.Type['RecurrenceRepetitionType']:
                return RecurrenceRepetitionType
            moment = schemas.StrSchema
            skip = schemas.Int32Schema
            weekend = schemas.Int32Schema
            __annotations__ = {
                "type": type,
                "moment": moment,
                "skip": skip,
                "weekend": weekend,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'RecurrenceRepetitionType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["moment"]) -> MetaOapg.properties.moment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skip"]) -> MetaOapg.properties.skip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weekend"]) -> MetaOapg.properties.weekend: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "moment", "skip", "weekend", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union['RecurrenceRepetitionType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["moment"]) -> typing.Union[MetaOapg.properties.moment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skip"]) -> typing.Union[MetaOapg.properties.skip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weekend"]) -> typing.Union[MetaOapg.properties.weekend, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "moment", "skip", "weekend", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union['RecurrenceRepetitionType', schemas.Unset] = schemas.unset,
        moment: typing.Union[MetaOapg.properties.moment, str, schemas.Unset] = schemas.unset,
        skip: typing.Union[MetaOapg.properties.skip, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        weekend: typing.Union[MetaOapg.properties.weekend, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RecurrenceRepetitionUpdate':
        return super().__new__(
            cls,
            *_args,
            type=type,
            moment=moment,
            skip=skip,
            weekend=weekend,
            _configuration=_configuration,
            **kwargs,
        )

from fireflyiii_client.model.recurrence_repetition_type import RecurrenceRepetitionType