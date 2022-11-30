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


class LiabilityType(
    schemas.EnumBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Mandatory when type is liability. Specifies the exact type.
    """


    class MetaOapg:
        format = 'string'
        enum_value_to_name = {
            "loan": "LOAN",
            "debt": "DEBT",
            "mortgage": "MORTGAGE",
            schemas.NoneClass.NONE: "NONE",
        }
    
    @schemas.classproperty
    def LOAN(cls):
        return cls("loan")
    
    @schemas.classproperty
    def DEBT(cls):
        return cls("debt")
    
    @schemas.classproperty
    def MORTGAGE(cls):
        return cls("mortgage")
    
    @schemas.classproperty
    def NONE(cls):
        return cls(None)


    def __new__(
        cls,
        *_args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'LiabilityType':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
        )
