import typing_extensions

from fireflyiii_client.apis.tags import TagValues
from fireflyiii_client.apis.tags.about_api import AboutApi
from fireflyiii_client.apis.tags.configuration_api import ConfigurationApi
from fireflyiii_client.apis.tags.users_api import UsersApi
from fireflyiii_client.apis.tags.autocomplete_api import AutocompleteApi
from fireflyiii_client.apis.tags.charts_api import ChartsApi
from fireflyiii_client.apis.tags.data_api import DataApi
from fireflyiii_client.apis.tags.insight_api import InsightApi
from fireflyiii_client.apis.tags.summary_api import SummaryApi
from fireflyiii_client.apis.tags.search_api import SearchApi
from fireflyiii_client.apis.tags.preferences_api import PreferencesApi
from fireflyiii_client.apis.tags.webhooks_api import WebhooksApi
from fireflyiii_client.apis.tags.accounts_api import AccountsApi
from fireflyiii_client.apis.tags.attachments_api import AttachmentsApi
from fireflyiii_client.apis.tags.available_budgets_api import AvailableBudgetsApi
from fireflyiii_client.apis.tags.bills_api import BillsApi
from fireflyiii_client.apis.tags.budgets_api import BudgetsApi
from fireflyiii_client.apis.tags.categories_api import CategoriesApi
from fireflyiii_client.apis.tags.object_groups_api import ObjectGroupsApi
from fireflyiii_client.apis.tags.piggy_banks_api import PiggyBanksApi
from fireflyiii_client.apis.tags.recurrences_api import RecurrencesApi
from fireflyiii_client.apis.tags.rules_api import RulesApi
from fireflyiii_client.apis.tags.rule_groups_api import RuleGroupsApi
from fireflyiii_client.apis.tags.tags_api import TagsApi
from fireflyiii_client.apis.tags.transactions_api import TransactionsApi
from fireflyiii_client.apis.tags.currencies_api import CurrenciesApi
from fireflyiii_client.apis.tags.links_api import LinksApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ABOUT: AboutApi,
        TagValues.CONFIGURATION: ConfigurationApi,
        TagValues.USERS: UsersApi,
        TagValues.AUTOCOMPLETE: AutocompleteApi,
        TagValues.CHARTS: ChartsApi,
        TagValues.DATA: DataApi,
        TagValues.INSIGHT: InsightApi,
        TagValues.SUMMARY: SummaryApi,
        TagValues.SEARCH: SearchApi,
        TagValues.PREFERENCES: PreferencesApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.ATTACHMENTS: AttachmentsApi,
        TagValues.AVAILABLE_BUDGETS: AvailableBudgetsApi,
        TagValues.BILLS: BillsApi,
        TagValues.BUDGETS: BudgetsApi,
        TagValues.CATEGORIES: CategoriesApi,
        TagValues.OBJECT_GROUPS: ObjectGroupsApi,
        TagValues.PIGGY_BANKS: PiggyBanksApi,
        TagValues.RECURRENCES: RecurrencesApi,
        TagValues.RULES: RulesApi,
        TagValues.RULE_GROUPS: RuleGroupsApi,
        TagValues.TAGS: TagsApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.CURRENCIES: CurrenciesApi,
        TagValues.LINKS: LinksApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ABOUT: AboutApi,
        TagValues.CONFIGURATION: ConfigurationApi,
        TagValues.USERS: UsersApi,
        TagValues.AUTOCOMPLETE: AutocompleteApi,
        TagValues.CHARTS: ChartsApi,
        TagValues.DATA: DataApi,
        TagValues.INSIGHT: InsightApi,
        TagValues.SUMMARY: SummaryApi,
        TagValues.SEARCH: SearchApi,
        TagValues.PREFERENCES: PreferencesApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.ATTACHMENTS: AttachmentsApi,
        TagValues.AVAILABLE_BUDGETS: AvailableBudgetsApi,
        TagValues.BILLS: BillsApi,
        TagValues.BUDGETS: BudgetsApi,
        TagValues.CATEGORIES: CategoriesApi,
        TagValues.OBJECT_GROUPS: ObjectGroupsApi,
        TagValues.PIGGY_BANKS: PiggyBanksApi,
        TagValues.RECURRENCES: RecurrencesApi,
        TagValues.RULES: RulesApi,
        TagValues.RULE_GROUPS: RuleGroupsApi,
        TagValues.TAGS: TagsApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.CURRENCIES: CurrenciesApi,
        TagValues.LINKS: LinksApi,
    }
)
