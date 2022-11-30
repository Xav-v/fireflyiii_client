from fireflyiii_client.paths.api_v1_transactions_id.get import ApiForget
from fireflyiii_client.paths.api_v1_transactions_id.put import ApiForput
from fireflyiii_client.paths.api_v1_transactions_id.delete import ApiFordelete


class ApiV1TransactionsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
