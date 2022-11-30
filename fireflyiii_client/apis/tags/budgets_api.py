# coding: utf-8

"""
    Firefly III API v1.5.6

    This is the documentation of the Firefly III API. You can find accompanying documentation on the website of Firefly III itself (see below). Please report any bugs or issues. You may use the \"Authorize\" button to try the API below. This file was last generated on 2022-04-04T03:54:41+00:00   # noqa: E501

    The version of the OpenAPI document: 1.5.6
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""

from fireflyiii_client.paths.api_v1_budgets_id.delete import DeleteBudget
from fireflyiii_client.paths.api_v1_budgets_id_limits_limit_id.delete import DeleteBudgetLimit
from fireflyiii_client.paths.api_v1_budgets_id.get import GetBudget
from fireflyiii_client.paths.api_v1_budgets_id_limits_limit_id.get import GetBudgetLimit
from fireflyiii_client.paths.api_v1_budgets_id_attachments.get import ListAttachmentByBudget
from fireflyiii_client.paths.api_v1_budgets.get import ListBudget
from fireflyiii_client.paths.api_v1_budget_limits.get import ListBudgetLimit
from fireflyiii_client.paths.api_v1_budgets_id_limits.get import ListBudgetLimitByBudget
from fireflyiii_client.paths.api_v1_budgets_id_transactions.get import ListTransactionByBudget
from fireflyiii_client.paths.api_v1_budgets_id_limits_limit_id_transactions.get import ListTransactionByBudgetLimit
from fireflyiii_client.paths.api_v1_budgets_transactions_without_budget.get import ListTransactionWithoutBudget
from fireflyiii_client.paths.api_v1_budgets.post import StoreBudget
from fireflyiii_client.paths.api_v1_budgets_id_limits.post import StoreBudgetLimit
from fireflyiii_client.paths.api_v1_budgets_id.put import UpdateBudget
from fireflyiii_client.paths.api_v1_budgets_id_limits_limit_id.put import UpdateBudgetLimit


class BudgetsApi(
    DeleteBudget,
    DeleteBudgetLimit,
    GetBudget,
    GetBudgetLimit,
    ListAttachmentByBudget,
    ListBudget,
    ListBudgetLimit,
    ListBudgetLimitByBudget,
    ListTransactionByBudget,
    ListTransactionByBudgetLimit,
    ListTransactionWithoutBudget,
    StoreBudget,
    StoreBudgetLimit,
    UpdateBudget,
    UpdateBudgetLimit,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
