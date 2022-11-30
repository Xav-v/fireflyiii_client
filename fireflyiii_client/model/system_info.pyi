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


class SystemInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "data",
        }
        
        class properties:
            
            
            class data(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "driver",
                        "os",
                        "php_version",
                        "api_version",
                        "version",
                    }
                    
                    class properties:
                        version = schemas.StrSchema
                        api_version = schemas.StrSchema
                        php_version = schemas.StrSchema
                        os = schemas.StrSchema
                        driver = schemas.StrSchema
                        __annotations__ = {
                            "version": version,
                            "api_version": api_version,
                            "php_version": php_version,
                            "os": os,
                            "driver": driver,
                        }
                
                driver: MetaOapg.properties.driver
                os: MetaOapg.properties.os
                php_version: MetaOapg.properties.php_version
                api_version: MetaOapg.properties.api_version
                version: MetaOapg.properties.version
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["api_version"]) -> MetaOapg.properties.api_version: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["php_version"]) -> MetaOapg.properties.php_version: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["os"]) -> MetaOapg.properties.os: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["driver"]) -> MetaOapg.properties.driver: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["version", "api_version", "php_version", "os", "driver", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["api_version"]) -> MetaOapg.properties.api_version: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["php_version"]) -> MetaOapg.properties.php_version: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["os"]) -> MetaOapg.properties.os: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["driver"]) -> MetaOapg.properties.driver: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["version", "api_version", "php_version", "os", "driver", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    driver: typing.Union[MetaOapg.properties.driver, str, ],
                    os: typing.Union[MetaOapg.properties.os, str, ],
                    php_version: typing.Union[MetaOapg.properties.php_version, str, ],
                    api_version: typing.Union[MetaOapg.properties.api_version, str, ],
                    version: typing.Union[MetaOapg.properties.version, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'data':
                    return super().__new__(
                        cls,
                        *_args,
                        driver=driver,
                        os=os,
                        php_version=php_version,
                        api_version=api_version,
                        version=version,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "data": data,
            }
    
    data: MetaOapg.properties.data
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        data: typing.Union[MetaOapg.properties.data, dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SystemInfo':
        return super().__new__(
            cls,
            *_args,
            data=data,
            _configuration=_configuration,
            **kwargs,
        )
