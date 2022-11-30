from fireflyiii_client.paths.api_v1_users_id.get import ApiForget
from fireflyiii_client.paths.api_v1_users_id.put import ApiForput
from fireflyiii_client.paths.api_v1_users_id.delete import ApiFordelete


class ApiV1UsersId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
