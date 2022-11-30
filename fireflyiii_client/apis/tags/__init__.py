# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from fireflyiii_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ABOUT = "about"
    CONFIGURATION = "configuration"
    USERS = "users"
    AUTOCOMPLETE = "autocomplete"
    CHARTS = "charts"
    DATA = "data"
    INSIGHT = "insight"
    SUMMARY = "summary"
    SEARCH = "search"
    PREFERENCES = "preferences"
    WEBHOOKS = "webhooks"
    ACCOUNTS = "accounts"
    ATTACHMENTS = "attachments"
    AVAILABLE_BUDGETS = "available_budgets"
    BILLS = "bills"
    BUDGETS = "budgets"
    CATEGORIES = "categories"
    OBJECT_GROUPS = "object_groups"
    PIGGY_BANKS = "piggy_banks"
    RECURRENCES = "recurrences"
    RULES = "rules"
    RULE_GROUPS = "rule_groups"
    TAGS = "tags"
    TRANSACTIONS = "transactions"
    CURRENCIES = "currencies"
    LINKS = "links"
