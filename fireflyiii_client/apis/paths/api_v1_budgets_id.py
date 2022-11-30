from fireflyiii_client.paths.api_v1_budgets_id.get import ApiForget
from fireflyiii_client.paths.api_v1_budgets_id.put import ApiForput
from fireflyiii_client.paths.api_v1_budgets_id.delete import ApiFordelete


class ApiV1BudgetsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
