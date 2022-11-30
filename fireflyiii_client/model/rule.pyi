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


class Rule(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "trigger",
            "rule_group_id",
            "title",
            "triggers",
            "actions",
        }
        
        class properties:
            title = schemas.StrSchema
            rule_group_id = schemas.StrSchema
        
            @staticmethod
            def trigger() -> typing.Type['RuleTriggerType']:
                return RuleTriggerType
            
            
            class triggers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['RuleTrigger']:
                        return RuleTrigger
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['RuleTrigger'], typing.List['RuleTrigger']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'triggers':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'RuleTrigger':
                    return super().__getitem__(i)
            
            
            class actions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['RuleAction']:
                        return RuleAction
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['RuleAction'], typing.List['RuleAction']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'actions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'RuleAction':
                    return super().__getitem__(i)
            created_at = schemas.DateTimeSchema
            updated_at = schemas.DateTimeSchema
            description = schemas.StrSchema
            rule_group_title = schemas.StrSchema
            order = schemas.Int32Schema
            active = schemas.BoolSchema
            strict = schemas.BoolSchema
            stop_processing = schemas.BoolSchema
            __annotations__ = {
                "title": title,
                "rule_group_id": rule_group_id,
                "trigger": trigger,
                "triggers": triggers,
                "actions": actions,
                "created_at": created_at,
                "updated_at": updated_at,
                "description": description,
                "rule_group_title": rule_group_title,
                "order": order,
                "active": active,
                "strict": strict,
                "stop_processing": stop_processing,
            }
    
    trigger: 'RuleTriggerType'
    rule_group_id: MetaOapg.properties.rule_group_id
    title: MetaOapg.properties.title
    triggers: MetaOapg.properties.triggers
    actions: MetaOapg.properties.actions
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rule_group_id"]) -> MetaOapg.properties.rule_group_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trigger"]) -> 'RuleTriggerType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["triggers"]) -> MetaOapg.properties.triggers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actions"]) -> MetaOapg.properties.actions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rule_group_title"]) -> MetaOapg.properties.rule_group_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["strict"]) -> MetaOapg.properties.strict: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stop_processing"]) -> MetaOapg.properties.stop_processing: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "rule_group_id", "trigger", "triggers", "actions", "created_at", "updated_at", "description", "rule_group_title", "order", "active", "strict", "stop_processing", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rule_group_id"]) -> MetaOapg.properties.rule_group_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trigger"]) -> 'RuleTriggerType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["triggers"]) -> MetaOapg.properties.triggers: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actions"]) -> MetaOapg.properties.actions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rule_group_title"]) -> typing.Union[MetaOapg.properties.rule_group_title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> typing.Union[MetaOapg.properties.order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["strict"]) -> typing.Union[MetaOapg.properties.strict, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stop_processing"]) -> typing.Union[MetaOapg.properties.stop_processing, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "rule_group_id", "trigger", "triggers", "actions", "created_at", "updated_at", "description", "rule_group_title", "order", "active", "strict", "stop_processing", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        trigger: 'RuleTriggerType',
        rule_group_id: typing.Union[MetaOapg.properties.rule_group_id, str, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        triggers: typing.Union[MetaOapg.properties.triggers, list, tuple, ],
        actions: typing.Union[MetaOapg.properties.actions, list, tuple, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        rule_group_title: typing.Union[MetaOapg.properties.rule_group_title, str, schemas.Unset] = schemas.unset,
        order: typing.Union[MetaOapg.properties.order, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        strict: typing.Union[MetaOapg.properties.strict, bool, schemas.Unset] = schemas.unset,
        stop_processing: typing.Union[MetaOapg.properties.stop_processing, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Rule':
        return super().__new__(
            cls,
            *_args,
            trigger=trigger,
            rule_group_id=rule_group_id,
            title=title,
            triggers=triggers,
            actions=actions,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            rule_group_title=rule_group_title,
            order=order,
            active=active,
            strict=strict,
            stop_processing=stop_processing,
            _configuration=_configuration,
            **kwargs,
        )

from fireflyiii_client.model.rule_action import RuleAction
from fireflyiii_client.model.rule_trigger import RuleTrigger
from fireflyiii_client.model.rule_trigger_type import RuleTriggerType
