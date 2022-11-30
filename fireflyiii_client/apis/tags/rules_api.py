# coding: utf-8

"""
    Firefly III API v1.5.6

    This is the documentation of the Firefly III API. You can find accompanying documentation on the website of Firefly III itself (see below). Please report any bugs or issues. You may use the \"Authorize\" button to try the API below. This file was last generated on 2022-04-04T03:54:41+00:00   # noqa: E501

    The version of the OpenAPI document: 1.5.6
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""

from fireflyiii_client.paths.api_v1_rules_id.delete import DeleteRule
from fireflyiii_client.paths.api_v1_rules_id_trigger.post import FireRule
from fireflyiii_client.paths.api_v1_rules_id.get import GetRule
from fireflyiii_client.paths.api_v1_rules.get import ListRule
from fireflyiii_client.paths.api_v1_rules.post import StoreRule
from fireflyiii_client.paths.api_v1_rules_id_test.get import TestRule
from fireflyiii_client.paths.api_v1_rules_id.put import UpdateRule


class RulesApi(
    DeleteRule,
    FireRule,
    GetRule,
    ListRule,
    StoreRule,
    TestRule,
    UpdateRule,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass