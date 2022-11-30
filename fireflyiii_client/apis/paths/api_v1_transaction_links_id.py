from fireflyiii_client.paths.api_v1_transaction_links_id.get import ApiForget
from fireflyiii_client.paths.api_v1_transaction_links_id.put import ApiForput
from fireflyiii_client.paths.api_v1_transaction_links_id.delete import ApiFordelete


class ApiV1TransactionLinksId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
