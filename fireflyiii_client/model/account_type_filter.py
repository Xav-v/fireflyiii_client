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


class AccountTypeFilter(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "all": "ALL",
            "asset": "ASSET",
            "cash": "CASH",
            "expense": "EXPENSE",
            "revenue": "REVENUE",
            "special": "SPECIAL",
            "hidden": "HIDDEN",
            "liability": "LIABILITY",
            "liabilities": "LIABILITIES",
            "Default account": "DEFAULT_ACCOUNT",
            "Cash account": "CASH_ACCOUNT",
            "Asset account": "ASSET_ACCOUNT",
            "Expense account": "EXPENSE_ACCOUNT",
            "Revenue account": "REVENUE_ACCOUNT",
            "Initial balance account": "INITIAL_BALANCE_ACCOUNT",
            "Beneficiary account": "BENEFICIARY_ACCOUNT",
            "Import account": "IMPORT_ACCOUNT",
            "Reconciliation account": "RECONCILIATION_ACCOUNT",
            "Loan": "LOAN",
            "Debt": "DEBT",
            "Mortgage": "MORTGAGE",
        }
    
    @schemas.classproperty
    def ALL(cls):
        return cls("all")
    
    @schemas.classproperty
    def ASSET(cls):
        return cls("asset")
    
    @schemas.classproperty
    def CASH(cls):
        return cls("cash")
    
    @schemas.classproperty
    def EXPENSE(cls):
        return cls("expense")
    
    @schemas.classproperty
    def REVENUE(cls):
        return cls("revenue")
    
    @schemas.classproperty
    def SPECIAL(cls):
        return cls("special")
    
    @schemas.classproperty
    def HIDDEN(cls):
        return cls("hidden")
    
    @schemas.classproperty
    def LIABILITY(cls):
        return cls("liability")
    
    @schemas.classproperty
    def LIABILITIES(cls):
        return cls("liabilities")
    
    @schemas.classproperty
    def DEFAULT_ACCOUNT(cls):
        return cls("Default account")
    
    @schemas.classproperty
    def CASH_ACCOUNT(cls):
        return cls("Cash account")
    
    @schemas.classproperty
    def ASSET_ACCOUNT(cls):
        return cls("Asset account")
    
    @schemas.classproperty
    def EXPENSE_ACCOUNT(cls):
        return cls("Expense account")
    
    @schemas.classproperty
    def REVENUE_ACCOUNT(cls):
        return cls("Revenue account")
    
    @schemas.classproperty
    def INITIAL_BALANCE_ACCOUNT(cls):
        return cls("Initial balance account")
    
    @schemas.classproperty
    def BENEFICIARY_ACCOUNT(cls):
        return cls("Beneficiary account")
    
    @schemas.classproperty
    def IMPORT_ACCOUNT(cls):
        return cls("Import account")
    
    @schemas.classproperty
    def RECONCILIATION_ACCOUNT(cls):
        return cls("Reconciliation account")
    
    @schemas.classproperty
    def LOAN(cls):
        return cls("Loan")
    
    @schemas.classproperty
    def DEBT(cls):
        return cls("Debt")
    
    @schemas.classproperty
    def MORTGAGE(cls):
        return cls("Mortgage")
