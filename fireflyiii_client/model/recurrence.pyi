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


class Recurrence(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            created_at = schemas.DateTimeSchema
            updated_at = schemas.DateTimeSchema
        
            @staticmethod
            def type() -> typing.Type['RecurrenceTransactionType']:
                return RecurrenceTransactionType
            title = schemas.StrSchema
            description = schemas.StrSchema
            first_date = schemas.DateTimeSchema
            
            
            class latest_date(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'latest_date':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class repeat_until(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'repeat_until':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class nr_of_repetitions(
                schemas.Int32Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'nr_of_repetitions':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            apply_rules = schemas.BoolSchema
            active = schemas.BoolSchema
            
            
            class notes(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'string'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'notes':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class repetitions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['RecurrenceRepetition']:
                        return RecurrenceRepetition
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['RecurrenceRepetition'], typing.List['RecurrenceRepetition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'repetitions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'RecurrenceRepetition':
                    return super().__getitem__(i)
            
            
            class transactions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['RecurrenceTransaction']:
                        return RecurrenceTransaction
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['RecurrenceTransaction'], typing.List['RecurrenceTransaction']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'transactions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'RecurrenceTransaction':
                    return super().__getitem__(i)
            __annotations__ = {
                "created_at": created_at,
                "updated_at": updated_at,
                "type": type,
                "title": title,
                "description": description,
                "first_date": first_date,
                "latest_date": latest_date,
                "repeat_until": repeat_until,
                "nr_of_repetitions": nr_of_repetitions,
                "apply_rules": apply_rules,
                "active": active,
                "notes": notes,
                "repetitions": repetitions,
                "transactions": transactions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'RecurrenceTransactionType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_date"]) -> MetaOapg.properties.first_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["latest_date"]) -> MetaOapg.properties.latest_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["repeat_until"]) -> MetaOapg.properties.repeat_until: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nr_of_repetitions"]) -> MetaOapg.properties.nr_of_repetitions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apply_rules"]) -> MetaOapg.properties.apply_rules: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["repetitions"]) -> MetaOapg.properties.repetitions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactions"]) -> MetaOapg.properties.transactions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["created_at", "updated_at", "type", "title", "description", "first_date", "latest_date", "repeat_until", "nr_of_repetitions", "apply_rules", "active", "notes", "repetitions", "transactions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union['RecurrenceTransactionType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_date"]) -> typing.Union[MetaOapg.properties.first_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["latest_date"]) -> typing.Union[MetaOapg.properties.latest_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["repeat_until"]) -> typing.Union[MetaOapg.properties.repeat_until, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nr_of_repetitions"]) -> typing.Union[MetaOapg.properties.nr_of_repetitions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apply_rules"]) -> typing.Union[MetaOapg.properties.apply_rules, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["repetitions"]) -> typing.Union[MetaOapg.properties.repetitions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactions"]) -> typing.Union[MetaOapg.properties.transactions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["created_at", "updated_at", "type", "title", "description", "first_date", "latest_date", "repeat_until", "nr_of_repetitions", "apply_rules", "active", "notes", "repetitions", "transactions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        type: typing.Union['RecurrenceTransactionType', schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        first_date: typing.Union[MetaOapg.properties.first_date, str, datetime, schemas.Unset] = schemas.unset,
        latest_date: typing.Union[MetaOapg.properties.latest_date, None, str, datetime, schemas.Unset] = schemas.unset,
        repeat_until: typing.Union[MetaOapg.properties.repeat_until, None, str, datetime, schemas.Unset] = schemas.unset,
        nr_of_repetitions: typing.Union[MetaOapg.properties.nr_of_repetitions, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        apply_rules: typing.Union[MetaOapg.properties.apply_rules, bool, schemas.Unset] = schemas.unset,
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, None, str, schemas.Unset] = schemas.unset,
        repetitions: typing.Union[MetaOapg.properties.repetitions, list, tuple, schemas.Unset] = schemas.unset,
        transactions: typing.Union[MetaOapg.properties.transactions, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Recurrence':
        return super().__new__(
            cls,
            *_args,
            created_at=created_at,
            updated_at=updated_at,
            type=type,
            title=title,
            description=description,
            first_date=first_date,
            latest_date=latest_date,
            repeat_until=repeat_until,
            nr_of_repetitions=nr_of_repetitions,
            apply_rules=apply_rules,
            active=active,
            notes=notes,
            repetitions=repetitions,
            transactions=transactions,
            _configuration=_configuration,
            **kwargs,
        )

from fireflyiii_client.model.recurrence_repetition import RecurrenceRepetition
from fireflyiii_client.model.recurrence_transaction import RecurrenceTransaction
from fireflyiii_client.model.recurrence_transaction_type import RecurrenceTransactionType