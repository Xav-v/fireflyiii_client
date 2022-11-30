from fireflyiii_client.paths.api_v1_accounts_id.get import ApiForget
from fireflyiii_client.paths.api_v1_accounts_id.put import ApiForput
from fireflyiii_client.paths.api_v1_accounts_id.delete import ApiFordelete


class ApiV1AccountsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
