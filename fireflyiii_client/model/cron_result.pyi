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


class CronResult(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def recurring_transactions() -> typing.Type['CronResultRow']:
                return CronResultRow
        
            @staticmethod
            def auto_budgets() -> typing.Type['CronResultRow']:
                return CronResultRow
        
            @staticmethod
            def telemetry() -> typing.Type['CronResultRow']:
                return CronResultRow
            __annotations__ = {
                "recurring_transactions": recurring_transactions,
                "auto_budgets": auto_budgets,
                "telemetry": telemetry,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recurring_transactions"]) -> 'CronResultRow': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_budgets"]) -> 'CronResultRow': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["telemetry"]) -> 'CronResultRow': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["recurring_transactions", "auto_budgets", "telemetry", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recurring_transactions"]) -> typing.Union['CronResultRow', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_budgets"]) -> typing.Union['CronResultRow', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["telemetry"]) -> typing.Union['CronResultRow', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["recurring_transactions", "auto_budgets", "telemetry", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        recurring_transactions: typing.Union['CronResultRow', schemas.Unset] = schemas.unset,
        auto_budgets: typing.Union['CronResultRow', schemas.Unset] = schemas.unset,
        telemetry: typing.Union['CronResultRow', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CronResult':
        return super().__new__(
            cls,
            *_args,
            recurring_transactions=recurring_transactions,
            auto_budgets=auto_budgets,
            telemetry=telemetry,
            _configuration=_configuration,
            **kwargs,
        )

from fireflyiii_client.model.cron_result_row import CronResultRow