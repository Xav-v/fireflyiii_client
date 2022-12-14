# coding: utf-8

"""
    Firefly III API v1.5.6

    This is the documentation of the Firefly III API. You can find accompanying documentation on the website of Firefly III itself (see below). Please report any bugs or issues. You may use the \"Authorize\" button to try the API below. This file was last generated on 2022-04-04T03:54:41+00:00   # noqa: E501

    The version of the OpenAPI document: 1.5.6
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""

from fireflyiii_client.paths.api_v1_categories_id.delete import DeleteCategory
from fireflyiii_client.paths.api_v1_categories_id.get import GetCategory
from fireflyiii_client.paths.api_v1_categories_id_attachments.get import ListAttachmentByCategory
from fireflyiii_client.paths.api_v1_categories.get import ListCategory
from fireflyiii_client.paths.api_v1_categories_id_transactions.get import ListTransactionByCategory
from fireflyiii_client.paths.api_v1_categories_transactions_without_category.get import ListTransactionWithoutCategory
from fireflyiii_client.paths.api_v1_categories.post import StoreCategory
from fireflyiii_client.paths.api_v1_categories_id.put import UpdateCategory


class CategoriesApi(
    DeleteCategory,
    GetCategory,
    ListAttachmentByCategory,
    ListCategory,
    ListTransactionByCategory,
    ListTransactionWithoutCategory,
    StoreCategory,
    UpdateCategory,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
