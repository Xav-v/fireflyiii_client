# coding: utf-8

"""
    Firefly III API v1.5.6

    This is the documentation of the Firefly III API. You can find accompanying documentation on the website of Firefly III itself (see below). Please report any bugs or issues. You may use the \"Authorize\" button to try the API below. This file was last generated on 2022-04-04T03:54:41+00:00   # noqa: E501

    The version of the OpenAPI document: 1.5.6
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""

from fireflyiii_client.paths.api_v1_bills_id.delete import DeleteBill
from fireflyiii_client.paths.api_v1_bills_id.get import GetBill
from fireflyiii_client.paths.api_v1_bills_id_attachments.get import ListAttachmentByBill
from fireflyiii_client.paths.api_v1_bills.get import ListBill
from fireflyiii_client.paths.api_v1_bills_id_rules.get import ListRuleByBill
from fireflyiii_client.paths.api_v1_bills_id_transactions.get import ListTransactionByBill
from fireflyiii_client.paths.api_v1_bills.post import StoreBill
from fireflyiii_client.paths.api_v1_bills_id.put import UpdateBill


class BillsApi(
    DeleteBill,
    GetBill,
    ListAttachmentByBill,
    ListBill,
    ListRuleByBill,
    ListTransactionByBill,
    StoreBill,
    UpdateBill,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
