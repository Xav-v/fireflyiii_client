from fireflyiii_client.paths.api_v1_rules_id.get import ApiForget
from fireflyiii_client.paths.api_v1_rules_id.put import ApiForput
from fireflyiii_client.paths.api_v1_rules_id.delete import ApiFordelete


class ApiV1RulesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
