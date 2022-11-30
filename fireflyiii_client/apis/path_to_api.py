import typing_extensions

from fireflyiii_client.paths import PathValues
from fireflyiii_client.apis.paths.api_v1_autocomplete_rule_groups import ApiV1AutocompleteRuleGroups
from fireflyiii_client.apis.paths.api_v1_autocomplete_categories import ApiV1AutocompleteCategories
from fireflyiii_client.apis.paths.api_v1_autocomplete_transaction_types import ApiV1AutocompleteTransactionTypes
from fireflyiii_client.apis.paths.api_v1_autocomplete_object_groups import ApiV1AutocompleteObjectGroups
from fireflyiii_client.apis.paths.api_v1_autocomplete_rules import ApiV1AutocompleteRules
from fireflyiii_client.apis.paths.api_v1_autocomplete_transactions import ApiV1AutocompleteTransactions
from fireflyiii_client.apis.paths.api_v1_autocomplete_transactions_with_id import ApiV1AutocompleteTransactionsWithId
from fireflyiii_client.apis.paths.api_v1_autocomplete_budgets import ApiV1AutocompleteBudgets
from fireflyiii_client.apis.paths.api_v1_autocomplete_piggy_banks import ApiV1AutocompletePiggyBanks
from fireflyiii_client.apis.paths.api_v1_autocomplete_piggy_banks_with_balance import ApiV1AutocompletePiggyBanksWithBalance
from fireflyiii_client.apis.paths.api_v1_autocomplete_currencies import ApiV1AutocompleteCurrencies
from fireflyiii_client.apis.paths.api_v1_autocomplete_currencies_with_code import ApiV1AutocompleteCurrenciesWithCode
from fireflyiii_client.apis.paths.api_v1_autocomplete_accounts import ApiV1AutocompleteAccounts
from fireflyiii_client.apis.paths.api_v1_autocomplete_tags import ApiV1AutocompleteTags
from fireflyiii_client.apis.paths.api_v1_autocomplete_bills import ApiV1AutocompleteBills
from fireflyiii_client.apis.paths.api_v1_autocomplete_recurring import ApiV1AutocompleteRecurring
from fireflyiii_client.apis.paths.api_v1_chart_account_overview import ApiV1ChartAccountOverview
from fireflyiii_client.apis.paths.api_v1_data_export_accounts import ApiV1DataExportAccounts
from fireflyiii_client.apis.paths.api_v1_data_export_bills import ApiV1DataExportBills
from fireflyiii_client.apis.paths.api_v1_data_export_budgets import ApiV1DataExportBudgets
from fireflyiii_client.apis.paths.api_v1_data_export_categories import ApiV1DataExportCategories
from fireflyiii_client.apis.paths.api_v1_data_export_piggy_banks import ApiV1DataExportPiggyBanks
from fireflyiii_client.apis.paths.api_v1_data_export_recurring import ApiV1DataExportRecurring
from fireflyiii_client.apis.paths.api_v1_data_export_rules import ApiV1DataExportRules
from fireflyiii_client.apis.paths.api_v1_data_export_tags import ApiV1DataExportTags
from fireflyiii_client.apis.paths.api_v1_data_export_transactions import ApiV1DataExportTransactions
from fireflyiii_client.apis.paths.api_v1_data_destroy import ApiV1DataDestroy
from fireflyiii_client.apis.paths.api_v1_data_bulk_transactions import ApiV1DataBulkTransactions
from fireflyiii_client.apis.paths.api_v1_insight_expense_bill import ApiV1InsightExpenseBill
from fireflyiii_client.apis.paths.api_v1_insight_expense_no_bill import ApiV1InsightExpenseNoBill
from fireflyiii_client.apis.paths.api_v1_insight_expense_total import ApiV1InsightExpenseTotal
from fireflyiii_client.apis.paths.api_v1_insight_income_total import ApiV1InsightIncomeTotal
from fireflyiii_client.apis.paths.api_v1_insight_transfer_total import ApiV1InsightTransferTotal
from fireflyiii_client.apis.paths.api_v1_insight_expense_category import ApiV1InsightExpenseCategory
from fireflyiii_client.apis.paths.api_v1_insight_expense_no_category import ApiV1InsightExpenseNoCategory
from fireflyiii_client.apis.paths.api_v1_insight_income_category import ApiV1InsightIncomeCategory
from fireflyiii_client.apis.paths.api_v1_insight_income_no_category import ApiV1InsightIncomeNoCategory
from fireflyiii_client.apis.paths.api_v1_insight_transfer_category import ApiV1InsightTransferCategory
from fireflyiii_client.apis.paths.api_v1_insight_transfer_no_category import ApiV1InsightTransferNoCategory
from fireflyiii_client.apis.paths.api_v1_insight_expense_expense import ApiV1InsightExpenseExpense
from fireflyiii_client.apis.paths.api_v1_insight_expense_asset import ApiV1InsightExpenseAsset
from fireflyiii_client.apis.paths.api_v1_insight_income_revenue import ApiV1InsightIncomeRevenue
from fireflyiii_client.apis.paths.api_v1_insight_income_asset import ApiV1InsightIncomeAsset
from fireflyiii_client.apis.paths.api_v1_insight_transfer_asset import ApiV1InsightTransferAsset
from fireflyiii_client.apis.paths.api_v1_insight_expense_budget import ApiV1InsightExpenseBudget
from fireflyiii_client.apis.paths.api_v1_insight_expense_no_budget import ApiV1InsightExpenseNoBudget
from fireflyiii_client.apis.paths.api_v1_insight_expense_tag import ApiV1InsightExpenseTag
from fireflyiii_client.apis.paths.api_v1_insight_expense_no_tag import ApiV1InsightExpenseNoTag
from fireflyiii_client.apis.paths.api_v1_insight_income_tag import ApiV1InsightIncomeTag
from fireflyiii_client.apis.paths.api_v1_insight_income_no_tag import ApiV1InsightIncomeNoTag
from fireflyiii_client.apis.paths.api_v1_insight_transfer_tag import ApiV1InsightTransferTag
from fireflyiii_client.apis.paths.api_v1_insight_transfer_no_tag import ApiV1InsightTransferNoTag
from fireflyiii_client.apis.paths.api_v1_summary_basic import ApiV1SummaryBasic
from fireflyiii_client.apis.paths.api_v1_attachments import ApiV1Attachments
from fireflyiii_client.apis.paths.api_v1_attachments_id import ApiV1AttachmentsId
from fireflyiii_client.apis.paths.api_v1_attachments_id_download import ApiV1AttachmentsIdDownload
from fireflyiii_client.apis.paths.api_v1_attachments_id_upload import ApiV1AttachmentsIdUpload
from fireflyiii_client.apis.paths.api_v1_rules_id_test import ApiV1RulesIdTest
from fireflyiii_client.apis.paths.api_v1_rules_id_trigger import ApiV1RulesIdTrigger
from fireflyiii_client.apis.paths.api_v1_bills_id_attachments import ApiV1BillsIdAttachments
from fireflyiii_client.apis.paths.api_v1_bills_id_rules import ApiV1BillsIdRules
from fireflyiii_client.apis.paths.api_v1_bills_id_transactions import ApiV1BillsIdTransactions
from fireflyiii_client.apis.paths.api_v1_bills import ApiV1Bills
from fireflyiii_client.apis.paths.api_v1_bills_id import ApiV1BillsId
from fireflyiii_client.apis.paths.api_v1_rules import ApiV1Rules
from fireflyiii_client.apis.paths.api_v1_rules_id import ApiV1RulesId
from fireflyiii_client.apis.paths.api_v1_transactions import ApiV1Transactions
from fireflyiii_client.apis.paths.api_v1_transactions_id import ApiV1TransactionsId
from fireflyiii_client.apis.paths.api_v1_object_groups import ApiV1ObjectGroups
from fireflyiii_client.apis.paths.api_v1_object_groups_id import ApiV1ObjectGroupsId
from fireflyiii_client.apis.paths.api_v1_categories_id_transactions import ApiV1CategoriesIdTransactions
from fireflyiii_client.apis.paths.api_v1_categories_transactions_without_category import ApiV1CategoriesTransactionsWithoutCategory
from fireflyiii_client.apis.paths.api_v1_categories_id_attachments import ApiV1CategoriesIdAttachments
from fireflyiii_client.apis.paths.api_v1_recurrences import ApiV1Recurrences
from fireflyiii_client.apis.paths.api_v1_recurrences_id import ApiV1RecurrencesId
from fireflyiii_client.apis.paths.api_v1_transactions_id_attachments import ApiV1TransactionsIdAttachments
from fireflyiii_client.apis.paths.api_v1_transactions_id_piggy_bank_events import ApiV1TransactionsIdPiggyBankEvents
from fireflyiii_client.apis.paths.api_v1_recurrences_id_transactions import ApiV1RecurrencesIdTransactions
from fireflyiii_client.apis.paths.api_v1_piggy_banks import ApiV1PiggyBanks
from fireflyiii_client.apis.paths.api_v1_piggy_banks_id import ApiV1PiggyBanksId
from fireflyiii_client.apis.paths.api_v1_currencies import ApiV1Currencies
from fireflyiii_client.apis.paths.api_v1_currencies_code_enable import ApiV1CurrenciesCodeEnable
from fireflyiii_client.apis.paths.api_v1_currencies_code_disable import ApiV1CurrenciesCodeDisable
from fireflyiii_client.apis.paths.api_v1_currencies_code_default import ApiV1CurrenciesCodeDefault
from fireflyiii_client.apis.paths.api_v1_currencies_code import ApiV1CurrenciesCode
from fireflyiii_client.apis.paths.api_v1_currencies_default import ApiV1CurrenciesDefault
from fireflyiii_client.apis.paths.api_v1_categories import ApiV1Categories
from fireflyiii_client.apis.paths.api_v1_categories_id import ApiV1CategoriesId
from fireflyiii_client.apis.paths.api_v1_tags import ApiV1Tags
from fireflyiii_client.apis.paths.api_v1_tags_tag import ApiV1TagsTag
from fireflyiii_client.apis.paths.api_v1_transaction_journals_id_links import ApiV1TransactionJournalsIdLinks
from fireflyiii_client.apis.paths.api_v1_transaction_journals_id import ApiV1TransactionJournalsId
from fireflyiii_client.apis.paths.api_v1_accounts import ApiV1Accounts
from fireflyiii_client.apis.paths.api_v1_accounts_id import ApiV1AccountsId
from fireflyiii_client.apis.paths.api_v1_currencies_code_accounts import ApiV1CurrenciesCodeAccounts
from fireflyiii_client.apis.paths.api_v1_currencies_code_available_budgets import ApiV1CurrenciesCodeAvailableBudgets
from fireflyiii_client.apis.paths.api_v1_currencies_code_bills import ApiV1CurrenciesCodeBills
from fireflyiii_client.apis.paths.api_v1_currencies_code_budget_limits import ApiV1CurrenciesCodeBudgetLimits
from fireflyiii_client.apis.paths.api_v1_currencies_code_recurrences import ApiV1CurrenciesCodeRecurrences
from fireflyiii_client.apis.paths.api_v1_currencies_code_rules import ApiV1CurrenciesCodeRules
from fireflyiii_client.apis.paths.api_v1_currencies_code_transactions import ApiV1CurrenciesCodeTransactions
from fireflyiii_client.apis.paths.api_v1_budgets_id_limits import ApiV1BudgetsIdLimits
from fireflyiii_client.apis.paths.api_v1_budgets_id_limits_limit_id import ApiV1BudgetsIdLimitsLimitId
from fireflyiii_client.apis.paths.api_v1_budget_limits import ApiV1BudgetLimits
from fireflyiii_client.apis.paths.api_v1_budgets import ApiV1Budgets
from fireflyiii_client.apis.paths.api_v1_budgets_id import ApiV1BudgetsId
from fireflyiii_client.apis.paths.api_v1_piggy_banks_id_events import ApiV1PiggyBanksIdEvents
from fireflyiii_client.apis.paths.api_v1_piggy_banks_id_attachments import ApiV1PiggyBanksIdAttachments
from fireflyiii_client.apis.paths.api_v1_rule_groups_id_rules import ApiV1RuleGroupsIdRules
from fireflyiii_client.apis.paths.api_v1_rule_groups import ApiV1RuleGroups
from fireflyiii_client.apis.paths.api_v1_rule_groups_id import ApiV1RuleGroupsId
from fireflyiii_client.apis.paths.api_v1_link_types_id_transactions import ApiV1LinkTypesIdTransactions
from fireflyiii_client.apis.paths.api_v1_available_budgets import ApiV1AvailableBudgets
from fireflyiii_client.apis.paths.api_v1_available_budgets_id import ApiV1AvailableBudgetsId
from fireflyiii_client.apis.paths.api_v1_budgets_id_limits_limit_id_transactions import ApiV1BudgetsIdLimitsLimitIdTransactions
from fireflyiii_client.apis.paths.api_v1_tags_tag_attachments import ApiV1TagsTagAttachments
from fireflyiii_client.apis.paths.api_v1_tags_tag_transactions import ApiV1TagsTagTransactions
from fireflyiii_client.apis.paths.api_v1_budgets_id_transactions import ApiV1BudgetsIdTransactions
from fireflyiii_client.apis.paths.api_v1_budgets_transactions_without_budget import ApiV1BudgetsTransactionsWithoutBudget
from fireflyiii_client.apis.paths.api_v1_budgets_id_attachments import ApiV1BudgetsIdAttachments
from fireflyiii_client.apis.paths.api_v1_object_groups_id_piggy_banks import ApiV1ObjectGroupsIdPiggyBanks
from fireflyiii_client.apis.paths.api_v1_object_groups_id_bills import ApiV1ObjectGroupsIdBills
from fireflyiii_client.apis.paths.api_v1_transaction_links import ApiV1TransactionLinks
from fireflyiii_client.apis.paths.api_v1_transaction_links_id import ApiV1TransactionLinksId
from fireflyiii_client.apis.paths.api_v1_link_types import ApiV1LinkTypes
from fireflyiii_client.apis.paths.api_v1_link_types_id import ApiV1LinkTypesId
from fireflyiii_client.apis.paths.api_v1_rule_groups_id_test import ApiV1RuleGroupsIdTest
from fireflyiii_client.apis.paths.api_v1_rule_groups_id_trigger import ApiV1RuleGroupsIdTrigger
from fireflyiii_client.apis.paths.api_v1_accounts_id_transactions import ApiV1AccountsIdTransactions
from fireflyiii_client.apis.paths.api_v1_accounts_id_attachments import ApiV1AccountsIdAttachments
from fireflyiii_client.apis.paths.api_v1_accounts_id_piggy_banks import ApiV1AccountsIdPiggyBanks
from fireflyiii_client.apis.paths.api_v1_search_accounts import ApiV1SearchAccounts
from fireflyiii_client.apis.paths.api_v1_search_transactions import ApiV1SearchTransactions
from fireflyiii_client.apis.paths.api_v1_cron_cli_token import ApiV1CronCliToken
from fireflyiii_client.apis.paths.api_v1_configuration import ApiV1Configuration
from fireflyiii_client.apis.paths.api_v1_configuration_name import ApiV1ConfigurationName
from fireflyiii_client.apis.paths.api_v1_users import ApiV1Users
from fireflyiii_client.apis.paths.api_v1_users_id import ApiV1UsersId
from fireflyiii_client.apis.paths.api_v1_about import ApiV1About
from fireflyiii_client.apis.paths.api_v1_about_user import ApiV1AboutUser
from fireflyiii_client.apis.paths.api_v1_webhooks import ApiV1Webhooks
from fireflyiii_client.apis.paths.api_v1_webhooks_id import ApiV1WebhooksId
from fireflyiii_client.apis.paths.api_v1_webhooks_id_submit import ApiV1WebhooksIdSubmit
from fireflyiii_client.apis.paths.api_v1_webhooks_id_messages import ApiV1WebhooksIdMessages
from fireflyiii_client.apis.paths.api_v1_webhooks_id_messages_message_id import ApiV1WebhooksIdMessagesMessageId
from fireflyiii_client.apis.paths.api_v1_webhooks_id_messages_message_id_attempts import ApiV1WebhooksIdMessagesMessageIdAttempts
from fireflyiii_client.apis.paths.api_v1_webhooks_id_messages_message_id_attempts_attempt_id import ApiV1WebhooksIdMessagesMessageIdAttemptsAttemptId
from fireflyiii_client.apis.paths.api_v1_preferences import ApiV1Preferences
from fireflyiii_client.apis.paths.api_v1_preferences_name import ApiV1PreferencesName

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V1_AUTOCOMPLETE_RULEGROUPS: ApiV1AutocompleteRuleGroups,
        PathValues.API_V1_AUTOCOMPLETE_CATEGORIES: ApiV1AutocompleteCategories,
        PathValues.API_V1_AUTOCOMPLETE_TRANSACTIONTYPES: ApiV1AutocompleteTransactionTypes,
        PathValues.API_V1_AUTOCOMPLETE_OBJECTGROUPS: ApiV1AutocompleteObjectGroups,
        PathValues.API_V1_AUTOCOMPLETE_RULES: ApiV1AutocompleteRules,
        PathValues.API_V1_AUTOCOMPLETE_TRANSACTIONS: ApiV1AutocompleteTransactions,
        PathValues.API_V1_AUTOCOMPLETE_TRANSACTIONSWITHID: ApiV1AutocompleteTransactionsWithId,
        PathValues.API_V1_AUTOCOMPLETE_BUDGETS: ApiV1AutocompleteBudgets,
        PathValues.API_V1_AUTOCOMPLETE_PIGGYBANKS: ApiV1AutocompletePiggyBanks,
        PathValues.API_V1_AUTOCOMPLETE_PIGGYBANKSWITHBALANCE: ApiV1AutocompletePiggyBanksWithBalance,
        PathValues.API_V1_AUTOCOMPLETE_CURRENCIES: ApiV1AutocompleteCurrencies,
        PathValues.API_V1_AUTOCOMPLETE_CURRENCIESWITHCODE: ApiV1AutocompleteCurrenciesWithCode,
        PathValues.API_V1_AUTOCOMPLETE_ACCOUNTS: ApiV1AutocompleteAccounts,
        PathValues.API_V1_AUTOCOMPLETE_TAGS: ApiV1AutocompleteTags,
        PathValues.API_V1_AUTOCOMPLETE_BILLS: ApiV1AutocompleteBills,
        PathValues.API_V1_AUTOCOMPLETE_RECURRING: ApiV1AutocompleteRecurring,
        PathValues.API_V1_CHART_ACCOUNT_OVERVIEW: ApiV1ChartAccountOverview,
        PathValues.API_V1_DATA_EXPORT_ACCOUNTS: ApiV1DataExportAccounts,
        PathValues.API_V1_DATA_EXPORT_BILLS: ApiV1DataExportBills,
        PathValues.API_V1_DATA_EXPORT_BUDGETS: ApiV1DataExportBudgets,
        PathValues.API_V1_DATA_EXPORT_CATEGORIES: ApiV1DataExportCategories,
        PathValues.API_V1_DATA_EXPORT_PIGGYBANKS: ApiV1DataExportPiggyBanks,
        PathValues.API_V1_DATA_EXPORT_RECURRING: ApiV1DataExportRecurring,
        PathValues.API_V1_DATA_EXPORT_RULES: ApiV1DataExportRules,
        PathValues.API_V1_DATA_EXPORT_TAGS: ApiV1DataExportTags,
        PathValues.API_V1_DATA_EXPORT_TRANSACTIONS: ApiV1DataExportTransactions,
        PathValues.API_V1_DATA_DESTROY: ApiV1DataDestroy,
        PathValues.API_V1_DATA_BULK_TRANSACTIONS: ApiV1DataBulkTransactions,
        PathValues.API_V1_INSIGHT_EXPENSE_BILL: ApiV1InsightExpenseBill,
        PathValues.API_V1_INSIGHT_EXPENSE_NOBILL: ApiV1InsightExpenseNoBill,
        PathValues.API_V1_INSIGHT_EXPENSE_TOTAL: ApiV1InsightExpenseTotal,
        PathValues.API_V1_INSIGHT_INCOME_TOTAL: ApiV1InsightIncomeTotal,
        PathValues.API_V1_INSIGHT_TRANSFER_TOTAL: ApiV1InsightTransferTotal,
        PathValues.API_V1_INSIGHT_EXPENSE_CATEGORY: ApiV1InsightExpenseCategory,
        PathValues.API_V1_INSIGHT_EXPENSE_NOCATEGORY: ApiV1InsightExpenseNoCategory,
        PathValues.API_V1_INSIGHT_INCOME_CATEGORY: ApiV1InsightIncomeCategory,
        PathValues.API_V1_INSIGHT_INCOME_NOCATEGORY: ApiV1InsightIncomeNoCategory,
        PathValues.API_V1_INSIGHT_TRANSFER_CATEGORY: ApiV1InsightTransferCategory,
        PathValues.API_V1_INSIGHT_TRANSFER_NOCATEGORY: ApiV1InsightTransferNoCategory,
        PathValues.API_V1_INSIGHT_EXPENSE_EXPENSE: ApiV1InsightExpenseExpense,
        PathValues.API_V1_INSIGHT_EXPENSE_ASSET: ApiV1InsightExpenseAsset,
        PathValues.API_V1_INSIGHT_INCOME_REVENUE: ApiV1InsightIncomeRevenue,
        PathValues.API_V1_INSIGHT_INCOME_ASSET: ApiV1InsightIncomeAsset,
        PathValues.API_V1_INSIGHT_TRANSFER_ASSET: ApiV1InsightTransferAsset,
        PathValues.API_V1_INSIGHT_EXPENSE_BUDGET: ApiV1InsightExpenseBudget,
        PathValues.API_V1_INSIGHT_EXPENSE_NOBUDGET: ApiV1InsightExpenseNoBudget,
        PathValues.API_V1_INSIGHT_EXPENSE_TAG: ApiV1InsightExpenseTag,
        PathValues.API_V1_INSIGHT_EXPENSE_NOTAG: ApiV1InsightExpenseNoTag,
        PathValues.API_V1_INSIGHT_INCOME_TAG: ApiV1InsightIncomeTag,
        PathValues.API_V1_INSIGHT_INCOME_NOTAG: ApiV1InsightIncomeNoTag,
        PathValues.API_V1_INSIGHT_TRANSFER_TAG: ApiV1InsightTransferTag,
        PathValues.API_V1_INSIGHT_TRANSFER_NOTAG: ApiV1InsightTransferNoTag,
        PathValues.API_V1_SUMMARY_BASIC: ApiV1SummaryBasic,
        PathValues.API_V1_ATTACHMENTS: ApiV1Attachments,
        PathValues.API_V1_ATTACHMENTS_ID: ApiV1AttachmentsId,
        PathValues.API_V1_ATTACHMENTS_ID_DOWNLOAD: ApiV1AttachmentsIdDownload,
        PathValues.API_V1_ATTACHMENTS_ID_UPLOAD: ApiV1AttachmentsIdUpload,
        PathValues.API_V1_RULES_ID_TEST: ApiV1RulesIdTest,
        PathValues.API_V1_RULES_ID_TRIGGER: ApiV1RulesIdTrigger,
        PathValues.API_V1_BILLS_ID_ATTACHMENTS: ApiV1BillsIdAttachments,
        PathValues.API_V1_BILLS_ID_RULES: ApiV1BillsIdRules,
        PathValues.API_V1_BILLS_ID_TRANSACTIONS: ApiV1BillsIdTransactions,
        PathValues.API_V1_BILLS: ApiV1Bills,
        PathValues.API_V1_BILLS_ID: ApiV1BillsId,
        PathValues.API_V1_RULES: ApiV1Rules,
        PathValues.API_V1_RULES_ID: ApiV1RulesId,
        PathValues.API_V1_TRANSACTIONS: ApiV1Transactions,
        PathValues.API_V1_TRANSACTIONS_ID: ApiV1TransactionsId,
        PathValues.API_V1_OBJECT_GROUPS: ApiV1ObjectGroups,
        PathValues.API_V1_OBJECT_GROUPS_ID: ApiV1ObjectGroupsId,
        PathValues.API_V1_CATEGORIES_ID_TRANSACTIONS: ApiV1CategoriesIdTransactions,
        PathValues.API_V1_CATEGORIES_TRANSACTIONSWITHOUTCATEGORY: ApiV1CategoriesTransactionsWithoutCategory,
        PathValues.API_V1_CATEGORIES_ID_ATTACHMENTS: ApiV1CategoriesIdAttachments,
        PathValues.API_V1_RECURRENCES: ApiV1Recurrences,
        PathValues.API_V1_RECURRENCES_ID: ApiV1RecurrencesId,
        PathValues.API_V1_TRANSACTIONS_ID_ATTACHMENTS: ApiV1TransactionsIdAttachments,
        PathValues.API_V1_TRANSACTIONS_ID_PIGGY_BANK_EVENTS: ApiV1TransactionsIdPiggyBankEvents,
        PathValues.API_V1_RECURRENCES_ID_TRANSACTIONS: ApiV1RecurrencesIdTransactions,
        PathValues.API_V1_PIGGY_BANKS: ApiV1PiggyBanks,
        PathValues.API_V1_PIGGY_BANKS_ID: ApiV1PiggyBanksId,
        PathValues.API_V1_CURRENCIES: ApiV1Currencies,
        PathValues.API_V1_CURRENCIES_CODE_ENABLE: ApiV1CurrenciesCodeEnable,
        PathValues.API_V1_CURRENCIES_CODE_DISABLE: ApiV1CurrenciesCodeDisable,
        PathValues.API_V1_CURRENCIES_CODE_DEFAULT: ApiV1CurrenciesCodeDefault,
        PathValues.API_V1_CURRENCIES_CODE: ApiV1CurrenciesCode,
        PathValues.API_V1_CURRENCIES_DEFAULT: ApiV1CurrenciesDefault,
        PathValues.API_V1_CATEGORIES: ApiV1Categories,
        PathValues.API_V1_CATEGORIES_ID: ApiV1CategoriesId,
        PathValues.API_V1_TAGS: ApiV1Tags,
        PathValues.API_V1_TAGS_TAG: ApiV1TagsTag,
        PathValues.API_V1_TRANSACTIONJOURNALS_ID_LINKS: ApiV1TransactionJournalsIdLinks,
        PathValues.API_V1_TRANSACTIONJOURNALS_ID: ApiV1TransactionJournalsId,
        PathValues.API_V1_ACCOUNTS: ApiV1Accounts,
        PathValues.API_V1_ACCOUNTS_ID: ApiV1AccountsId,
        PathValues.API_V1_CURRENCIES_CODE_ACCOUNTS: ApiV1CurrenciesCodeAccounts,
        PathValues.API_V1_CURRENCIES_CODE_AVAILABLE_BUDGETS: ApiV1CurrenciesCodeAvailableBudgets,
        PathValues.API_V1_CURRENCIES_CODE_BILLS: ApiV1CurrenciesCodeBills,
        PathValues.API_V1_CURRENCIES_CODE_BUDGET_LIMITS: ApiV1CurrenciesCodeBudgetLimits,
        PathValues.API_V1_CURRENCIES_CODE_RECURRENCES: ApiV1CurrenciesCodeRecurrences,
        PathValues.API_V1_CURRENCIES_CODE_RULES: ApiV1CurrenciesCodeRules,
        PathValues.API_V1_CURRENCIES_CODE_TRANSACTIONS: ApiV1CurrenciesCodeTransactions,
        PathValues.API_V1_BUDGETS_ID_LIMITS: ApiV1BudgetsIdLimits,
        PathValues.API_V1_BUDGETS_ID_LIMITS_LIMIT_ID: ApiV1BudgetsIdLimitsLimitId,
        PathValues.API_V1_BUDGETLIMITS: ApiV1BudgetLimits,
        PathValues.API_V1_BUDGETS: ApiV1Budgets,
        PathValues.API_V1_BUDGETS_ID: ApiV1BudgetsId,
        PathValues.API_V1_PIGGY_BANKS_ID_EVENTS: ApiV1PiggyBanksIdEvents,
        PathValues.API_V1_PIGGY_BANKS_ID_ATTACHMENTS: ApiV1PiggyBanksIdAttachments,
        PathValues.API_V1_RULE_GROUPS_ID_RULES: ApiV1RuleGroupsIdRules,
        PathValues.API_V1_RULE_GROUPS: ApiV1RuleGroups,
        PathValues.API_V1_RULE_GROUPS_ID: ApiV1RuleGroupsId,
        PathValues.API_V1_LINK_TYPES_ID_TRANSACTIONS: ApiV1LinkTypesIdTransactions,
        PathValues.API_V1_AVAILABLE_BUDGETS: ApiV1AvailableBudgets,
        PathValues.API_V1_AVAILABLE_BUDGETS_ID: ApiV1AvailableBudgetsId,
        PathValues.API_V1_BUDGETS_ID_LIMITS_LIMIT_ID_TRANSACTIONS: ApiV1BudgetsIdLimitsLimitIdTransactions,
        PathValues.API_V1_TAGS_TAG_ATTACHMENTS: ApiV1TagsTagAttachments,
        PathValues.API_V1_TAGS_TAG_TRANSACTIONS: ApiV1TagsTagTransactions,
        PathValues.API_V1_BUDGETS_ID_TRANSACTIONS: ApiV1BudgetsIdTransactions,
        PathValues.API_V1_BUDGETS_TRANSACTIONSWITHOUTBUDGET: ApiV1BudgetsTransactionsWithoutBudget,
        PathValues.API_V1_BUDGETS_ID_ATTACHMENTS: ApiV1BudgetsIdAttachments,
        PathValues.API_V1_OBJECT_GROUPS_ID_PIGGY_BANKS: ApiV1ObjectGroupsIdPiggyBanks,
        PathValues.API_V1_OBJECT_GROUPS_ID_BILLS: ApiV1ObjectGroupsIdBills,
        PathValues.API_V1_TRANSACTION_LINKS: ApiV1TransactionLinks,
        PathValues.API_V1_TRANSACTION_LINKS_ID: ApiV1TransactionLinksId,
        PathValues.API_V1_LINK_TYPES: ApiV1LinkTypes,
        PathValues.API_V1_LINK_TYPES_ID: ApiV1LinkTypesId,
        PathValues.API_V1_RULE_GROUPS_ID_TEST: ApiV1RuleGroupsIdTest,
        PathValues.API_V1_RULE_GROUPS_ID_TRIGGER: ApiV1RuleGroupsIdTrigger,
        PathValues.API_V1_ACCOUNTS_ID_TRANSACTIONS: ApiV1AccountsIdTransactions,
        PathValues.API_V1_ACCOUNTS_ID_ATTACHMENTS: ApiV1AccountsIdAttachments,
        PathValues.API_V1_ACCOUNTS_ID_PIGGY_BANKS: ApiV1AccountsIdPiggyBanks,
        PathValues.API_V1_SEARCH_ACCOUNTS: ApiV1SearchAccounts,
        PathValues.API_V1_SEARCH_TRANSACTIONS: ApiV1SearchTransactions,
        PathValues.API_V1_CRON_CLI_TOKEN: ApiV1CronCliToken,
        PathValues.API_V1_CONFIGURATION: ApiV1Configuration,
        PathValues.API_V1_CONFIGURATION_NAME: ApiV1ConfigurationName,
        PathValues.API_V1_USERS: ApiV1Users,
        PathValues.API_V1_USERS_ID: ApiV1UsersId,
        PathValues.API_V1_ABOUT: ApiV1About,
        PathValues.API_V1_ABOUT_USER: ApiV1AboutUser,
        PathValues.API_V1_WEBHOOKS: ApiV1Webhooks,
        PathValues.API_V1_WEBHOOKS_ID: ApiV1WebhooksId,
        PathValues.API_V1_WEBHOOKS_ID_SUBMIT: ApiV1WebhooksIdSubmit,
        PathValues.API_V1_WEBHOOKS_ID_MESSAGES: ApiV1WebhooksIdMessages,
        PathValues.API_V1_WEBHOOKS_ID_MESSAGES_MESSAGE_ID: ApiV1WebhooksIdMessagesMessageId,
        PathValues.API_V1_WEBHOOKS_ID_MESSAGES_MESSAGE_ID_ATTEMPTS: ApiV1WebhooksIdMessagesMessageIdAttempts,
        PathValues.API_V1_WEBHOOKS_ID_MESSAGES_MESSAGE_ID_ATTEMPTS_ATTEMPT_ID: ApiV1WebhooksIdMessagesMessageIdAttemptsAttemptId,
        PathValues.API_V1_PREFERENCES: ApiV1Preferences,
        PathValues.API_V1_PREFERENCES_NAME: ApiV1PreferencesName,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V1_AUTOCOMPLETE_RULEGROUPS: ApiV1AutocompleteRuleGroups,
        PathValues.API_V1_AUTOCOMPLETE_CATEGORIES: ApiV1AutocompleteCategories,
        PathValues.API_V1_AUTOCOMPLETE_TRANSACTIONTYPES: ApiV1AutocompleteTransactionTypes,
        PathValues.API_V1_AUTOCOMPLETE_OBJECTGROUPS: ApiV1AutocompleteObjectGroups,
        PathValues.API_V1_AUTOCOMPLETE_RULES: ApiV1AutocompleteRules,
        PathValues.API_V1_AUTOCOMPLETE_TRANSACTIONS: ApiV1AutocompleteTransactions,
        PathValues.API_V1_AUTOCOMPLETE_TRANSACTIONSWITHID: ApiV1AutocompleteTransactionsWithId,
        PathValues.API_V1_AUTOCOMPLETE_BUDGETS: ApiV1AutocompleteBudgets,
        PathValues.API_V1_AUTOCOMPLETE_PIGGYBANKS: ApiV1AutocompletePiggyBanks,
        PathValues.API_V1_AUTOCOMPLETE_PIGGYBANKSWITHBALANCE: ApiV1AutocompletePiggyBanksWithBalance,
        PathValues.API_V1_AUTOCOMPLETE_CURRENCIES: ApiV1AutocompleteCurrencies,
        PathValues.API_V1_AUTOCOMPLETE_CURRENCIESWITHCODE: ApiV1AutocompleteCurrenciesWithCode,
        PathValues.API_V1_AUTOCOMPLETE_ACCOUNTS: ApiV1AutocompleteAccounts,
        PathValues.API_V1_AUTOCOMPLETE_TAGS: ApiV1AutocompleteTags,
        PathValues.API_V1_AUTOCOMPLETE_BILLS: ApiV1AutocompleteBills,
        PathValues.API_V1_AUTOCOMPLETE_RECURRING: ApiV1AutocompleteRecurring,
        PathValues.API_V1_CHART_ACCOUNT_OVERVIEW: ApiV1ChartAccountOverview,
        PathValues.API_V1_DATA_EXPORT_ACCOUNTS: ApiV1DataExportAccounts,
        PathValues.API_V1_DATA_EXPORT_BILLS: ApiV1DataExportBills,
        PathValues.API_V1_DATA_EXPORT_BUDGETS: ApiV1DataExportBudgets,
        PathValues.API_V1_DATA_EXPORT_CATEGORIES: ApiV1DataExportCategories,
        PathValues.API_V1_DATA_EXPORT_PIGGYBANKS: ApiV1DataExportPiggyBanks,
        PathValues.API_V1_DATA_EXPORT_RECURRING: ApiV1DataExportRecurring,
        PathValues.API_V1_DATA_EXPORT_RULES: ApiV1DataExportRules,
        PathValues.API_V1_DATA_EXPORT_TAGS: ApiV1DataExportTags,
        PathValues.API_V1_DATA_EXPORT_TRANSACTIONS: ApiV1DataExportTransactions,
        PathValues.API_V1_DATA_DESTROY: ApiV1DataDestroy,
        PathValues.API_V1_DATA_BULK_TRANSACTIONS: ApiV1DataBulkTransactions,
        PathValues.API_V1_INSIGHT_EXPENSE_BILL: ApiV1InsightExpenseBill,
        PathValues.API_V1_INSIGHT_EXPENSE_NOBILL: ApiV1InsightExpenseNoBill,
        PathValues.API_V1_INSIGHT_EXPENSE_TOTAL: ApiV1InsightExpenseTotal,
        PathValues.API_V1_INSIGHT_INCOME_TOTAL: ApiV1InsightIncomeTotal,
        PathValues.API_V1_INSIGHT_TRANSFER_TOTAL: ApiV1InsightTransferTotal,
        PathValues.API_V1_INSIGHT_EXPENSE_CATEGORY: ApiV1InsightExpenseCategory,
        PathValues.API_V1_INSIGHT_EXPENSE_NOCATEGORY: ApiV1InsightExpenseNoCategory,
        PathValues.API_V1_INSIGHT_INCOME_CATEGORY: ApiV1InsightIncomeCategory,
        PathValues.API_V1_INSIGHT_INCOME_NOCATEGORY: ApiV1InsightIncomeNoCategory,
        PathValues.API_V1_INSIGHT_TRANSFER_CATEGORY: ApiV1InsightTransferCategory,
        PathValues.API_V1_INSIGHT_TRANSFER_NOCATEGORY: ApiV1InsightTransferNoCategory,
        PathValues.API_V1_INSIGHT_EXPENSE_EXPENSE: ApiV1InsightExpenseExpense,
        PathValues.API_V1_INSIGHT_EXPENSE_ASSET: ApiV1InsightExpenseAsset,
        PathValues.API_V1_INSIGHT_INCOME_REVENUE: ApiV1InsightIncomeRevenue,
        PathValues.API_V1_INSIGHT_INCOME_ASSET: ApiV1InsightIncomeAsset,
        PathValues.API_V1_INSIGHT_TRANSFER_ASSET: ApiV1InsightTransferAsset,
        PathValues.API_V1_INSIGHT_EXPENSE_BUDGET: ApiV1InsightExpenseBudget,
        PathValues.API_V1_INSIGHT_EXPENSE_NOBUDGET: ApiV1InsightExpenseNoBudget,
        PathValues.API_V1_INSIGHT_EXPENSE_TAG: ApiV1InsightExpenseTag,
        PathValues.API_V1_INSIGHT_EXPENSE_NOTAG: ApiV1InsightExpenseNoTag,
        PathValues.API_V1_INSIGHT_INCOME_TAG: ApiV1InsightIncomeTag,
        PathValues.API_V1_INSIGHT_INCOME_NOTAG: ApiV1InsightIncomeNoTag,
        PathValues.API_V1_INSIGHT_TRANSFER_TAG: ApiV1InsightTransferTag,
        PathValues.API_V1_INSIGHT_TRANSFER_NOTAG: ApiV1InsightTransferNoTag,
        PathValues.API_V1_SUMMARY_BASIC: ApiV1SummaryBasic,
        PathValues.API_V1_ATTACHMENTS: ApiV1Attachments,
        PathValues.API_V1_ATTACHMENTS_ID: ApiV1AttachmentsId,
        PathValues.API_V1_ATTACHMENTS_ID_DOWNLOAD: ApiV1AttachmentsIdDownload,
        PathValues.API_V1_ATTACHMENTS_ID_UPLOAD: ApiV1AttachmentsIdUpload,
        PathValues.API_V1_RULES_ID_TEST: ApiV1RulesIdTest,
        PathValues.API_V1_RULES_ID_TRIGGER: ApiV1RulesIdTrigger,
        PathValues.API_V1_BILLS_ID_ATTACHMENTS: ApiV1BillsIdAttachments,
        PathValues.API_V1_BILLS_ID_RULES: ApiV1BillsIdRules,
        PathValues.API_V1_BILLS_ID_TRANSACTIONS: ApiV1BillsIdTransactions,
        PathValues.API_V1_BILLS: ApiV1Bills,
        PathValues.API_V1_BILLS_ID: ApiV1BillsId,
        PathValues.API_V1_RULES: ApiV1Rules,
        PathValues.API_V1_RULES_ID: ApiV1RulesId,
        PathValues.API_V1_TRANSACTIONS: ApiV1Transactions,
        PathValues.API_V1_TRANSACTIONS_ID: ApiV1TransactionsId,
        PathValues.API_V1_OBJECT_GROUPS: ApiV1ObjectGroups,
        PathValues.API_V1_OBJECT_GROUPS_ID: ApiV1ObjectGroupsId,
        PathValues.API_V1_CATEGORIES_ID_TRANSACTIONS: ApiV1CategoriesIdTransactions,
        PathValues.API_V1_CATEGORIES_TRANSACTIONSWITHOUTCATEGORY: ApiV1CategoriesTransactionsWithoutCategory,
        PathValues.API_V1_CATEGORIES_ID_ATTACHMENTS: ApiV1CategoriesIdAttachments,
        PathValues.API_V1_RECURRENCES: ApiV1Recurrences,
        PathValues.API_V1_RECURRENCES_ID: ApiV1RecurrencesId,
        PathValues.API_V1_TRANSACTIONS_ID_ATTACHMENTS: ApiV1TransactionsIdAttachments,
        PathValues.API_V1_TRANSACTIONS_ID_PIGGY_BANK_EVENTS: ApiV1TransactionsIdPiggyBankEvents,
        PathValues.API_V1_RECURRENCES_ID_TRANSACTIONS: ApiV1RecurrencesIdTransactions,
        PathValues.API_V1_PIGGY_BANKS: ApiV1PiggyBanks,
        PathValues.API_V1_PIGGY_BANKS_ID: ApiV1PiggyBanksId,
        PathValues.API_V1_CURRENCIES: ApiV1Currencies,
        PathValues.API_V1_CURRENCIES_CODE_ENABLE: ApiV1CurrenciesCodeEnable,
        PathValues.API_V1_CURRENCIES_CODE_DISABLE: ApiV1CurrenciesCodeDisable,
        PathValues.API_V1_CURRENCIES_CODE_DEFAULT: ApiV1CurrenciesCodeDefault,
        PathValues.API_V1_CURRENCIES_CODE: ApiV1CurrenciesCode,
        PathValues.API_V1_CURRENCIES_DEFAULT: ApiV1CurrenciesDefault,
        PathValues.API_V1_CATEGORIES: ApiV1Categories,
        PathValues.API_V1_CATEGORIES_ID: ApiV1CategoriesId,
        PathValues.API_V1_TAGS: ApiV1Tags,
        PathValues.API_V1_TAGS_TAG: ApiV1TagsTag,
        PathValues.API_V1_TRANSACTIONJOURNALS_ID_LINKS: ApiV1TransactionJournalsIdLinks,
        PathValues.API_V1_TRANSACTIONJOURNALS_ID: ApiV1TransactionJournalsId,
        PathValues.API_V1_ACCOUNTS: ApiV1Accounts,
        PathValues.API_V1_ACCOUNTS_ID: ApiV1AccountsId,
        PathValues.API_V1_CURRENCIES_CODE_ACCOUNTS: ApiV1CurrenciesCodeAccounts,
        PathValues.API_V1_CURRENCIES_CODE_AVAILABLE_BUDGETS: ApiV1CurrenciesCodeAvailableBudgets,
        PathValues.API_V1_CURRENCIES_CODE_BILLS: ApiV1CurrenciesCodeBills,
        PathValues.API_V1_CURRENCIES_CODE_BUDGET_LIMITS: ApiV1CurrenciesCodeBudgetLimits,
        PathValues.API_V1_CURRENCIES_CODE_RECURRENCES: ApiV1CurrenciesCodeRecurrences,
        PathValues.API_V1_CURRENCIES_CODE_RULES: ApiV1CurrenciesCodeRules,
        PathValues.API_V1_CURRENCIES_CODE_TRANSACTIONS: ApiV1CurrenciesCodeTransactions,
        PathValues.API_V1_BUDGETS_ID_LIMITS: ApiV1BudgetsIdLimits,
        PathValues.API_V1_BUDGETS_ID_LIMITS_LIMIT_ID: ApiV1BudgetsIdLimitsLimitId,
        PathValues.API_V1_BUDGETLIMITS: ApiV1BudgetLimits,
        PathValues.API_V1_BUDGETS: ApiV1Budgets,
        PathValues.API_V1_BUDGETS_ID: ApiV1BudgetsId,
        PathValues.API_V1_PIGGY_BANKS_ID_EVENTS: ApiV1PiggyBanksIdEvents,
        PathValues.API_V1_PIGGY_BANKS_ID_ATTACHMENTS: ApiV1PiggyBanksIdAttachments,
        PathValues.API_V1_RULE_GROUPS_ID_RULES: ApiV1RuleGroupsIdRules,
        PathValues.API_V1_RULE_GROUPS: ApiV1RuleGroups,
        PathValues.API_V1_RULE_GROUPS_ID: ApiV1RuleGroupsId,
        PathValues.API_V1_LINK_TYPES_ID_TRANSACTIONS: ApiV1LinkTypesIdTransactions,
        PathValues.API_V1_AVAILABLE_BUDGETS: ApiV1AvailableBudgets,
        PathValues.API_V1_AVAILABLE_BUDGETS_ID: ApiV1AvailableBudgetsId,
        PathValues.API_V1_BUDGETS_ID_LIMITS_LIMIT_ID_TRANSACTIONS: ApiV1BudgetsIdLimitsLimitIdTransactions,
        PathValues.API_V1_TAGS_TAG_ATTACHMENTS: ApiV1TagsTagAttachments,
        PathValues.API_V1_TAGS_TAG_TRANSACTIONS: ApiV1TagsTagTransactions,
        PathValues.API_V1_BUDGETS_ID_TRANSACTIONS: ApiV1BudgetsIdTransactions,
        PathValues.API_V1_BUDGETS_TRANSACTIONSWITHOUTBUDGET: ApiV1BudgetsTransactionsWithoutBudget,
        PathValues.API_V1_BUDGETS_ID_ATTACHMENTS: ApiV1BudgetsIdAttachments,
        PathValues.API_V1_OBJECT_GROUPS_ID_PIGGY_BANKS: ApiV1ObjectGroupsIdPiggyBanks,
        PathValues.API_V1_OBJECT_GROUPS_ID_BILLS: ApiV1ObjectGroupsIdBills,
        PathValues.API_V1_TRANSACTION_LINKS: ApiV1TransactionLinks,
        PathValues.API_V1_TRANSACTION_LINKS_ID: ApiV1TransactionLinksId,
        PathValues.API_V1_LINK_TYPES: ApiV1LinkTypes,
        PathValues.API_V1_LINK_TYPES_ID: ApiV1LinkTypesId,
        PathValues.API_V1_RULE_GROUPS_ID_TEST: ApiV1RuleGroupsIdTest,
        PathValues.API_V1_RULE_GROUPS_ID_TRIGGER: ApiV1RuleGroupsIdTrigger,
        PathValues.API_V1_ACCOUNTS_ID_TRANSACTIONS: ApiV1AccountsIdTransactions,
        PathValues.API_V1_ACCOUNTS_ID_ATTACHMENTS: ApiV1AccountsIdAttachments,
        PathValues.API_V1_ACCOUNTS_ID_PIGGY_BANKS: ApiV1AccountsIdPiggyBanks,
        PathValues.API_V1_SEARCH_ACCOUNTS: ApiV1SearchAccounts,
        PathValues.API_V1_SEARCH_TRANSACTIONS: ApiV1SearchTransactions,
        PathValues.API_V1_CRON_CLI_TOKEN: ApiV1CronCliToken,
        PathValues.API_V1_CONFIGURATION: ApiV1Configuration,
        PathValues.API_V1_CONFIGURATION_NAME: ApiV1ConfigurationName,
        PathValues.API_V1_USERS: ApiV1Users,
        PathValues.API_V1_USERS_ID: ApiV1UsersId,
        PathValues.API_V1_ABOUT: ApiV1About,
        PathValues.API_V1_ABOUT_USER: ApiV1AboutUser,
        PathValues.API_V1_WEBHOOKS: ApiV1Webhooks,
        PathValues.API_V1_WEBHOOKS_ID: ApiV1WebhooksId,
        PathValues.API_V1_WEBHOOKS_ID_SUBMIT: ApiV1WebhooksIdSubmit,
        PathValues.API_V1_WEBHOOKS_ID_MESSAGES: ApiV1WebhooksIdMessages,
        PathValues.API_V1_WEBHOOKS_ID_MESSAGES_MESSAGE_ID: ApiV1WebhooksIdMessagesMessageId,
        PathValues.API_V1_WEBHOOKS_ID_MESSAGES_MESSAGE_ID_ATTEMPTS: ApiV1WebhooksIdMessagesMessageIdAttempts,
        PathValues.API_V1_WEBHOOKS_ID_MESSAGES_MESSAGE_ID_ATTEMPTS_ATTEMPT_ID: ApiV1WebhooksIdMessagesMessageIdAttemptsAttemptId,
        PathValues.API_V1_PREFERENCES: ApiV1Preferences,
        PathValues.API_V1_PREFERENCES_NAME: ApiV1PreferencesName,
    }
)
