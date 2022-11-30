from fireflyiii_client.paths.api_v1_rule_groups_id.get import ApiForget
from fireflyiii_client.paths.api_v1_rule_groups_id.put import ApiForput
from fireflyiii_client.paths.api_v1_rule_groups_id.delete import ApiFordelete


class ApiV1RuleGroupsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
