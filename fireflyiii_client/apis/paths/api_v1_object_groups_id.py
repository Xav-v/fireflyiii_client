from fireflyiii_client.paths.api_v1_object_groups_id.get import ApiForget
from fireflyiii_client.paths.api_v1_object_groups_id.put import ApiForput
from fireflyiii_client.paths.api_v1_object_groups_id.delete import ApiFordelete


class ApiV1ObjectGroupsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
