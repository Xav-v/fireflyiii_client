# coding: utf-8

"""
    Firefly III API v1.5.6

    This is the documentation of the Firefly III API. You can find accompanying documentation on the website of Firefly III itself (see below). Please report any bugs or issues. You may use the \"Authorize\" button to try the API below. This file was last generated on 2022-04-04T03:54:41+00:00   # noqa: E501

    The version of the OpenAPI document: 1.5.6
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""

from fireflyiii_client.paths.api_v1_available_budgets_id.delete import DeleteAvailableBudget
from fireflyiii_client.paths.api_v1_available_budgets_id.get import GetAvailableBudget
from fireflyiii_client.paths.api_v1_available_budgets.get import ListAvailableBudget
from fireflyiii_client.paths.api_v1_available_budgets.post import StoreAvailableBudget
from fireflyiii_client.paths.api_v1_available_budgets_id.put import UpdateAvailableBudget


class AvailableBudgetsApi(
    DeleteAvailableBudget,
    GetAvailableBudget,
    ListAvailableBudget,
    StoreAvailableBudget,
    UpdateAvailableBudget,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
