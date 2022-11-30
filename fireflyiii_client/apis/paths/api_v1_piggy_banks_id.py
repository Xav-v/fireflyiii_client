from fireflyiii_client.paths.api_v1_piggy_banks_id.get import ApiForget
from fireflyiii_client.paths.api_v1_piggy_banks_id.put import ApiForput
from fireflyiii_client.paths.api_v1_piggy_banks_id.delete import ApiFordelete


class ApiV1PiggyBanksId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
