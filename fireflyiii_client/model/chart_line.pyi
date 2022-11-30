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


class ChartLine(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['ChartDataSet']:
            return ChartDataSet

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['ChartDataSet'], typing.List['ChartDataSet']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ChartLine':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'ChartDataSet':
        return super().__getitem__(i)

from fireflyiii_client.model.chart_data_set import ChartDataSet
