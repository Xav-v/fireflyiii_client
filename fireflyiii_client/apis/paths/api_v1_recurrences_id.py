from fireflyiii_client.paths.api_v1_recurrences_id.get import ApiForget
from fireflyiii_client.paths.api_v1_recurrences_id.put import ApiForput
from fireflyiii_client.paths.api_v1_recurrences_id.delete import ApiFordelete


class ApiV1RecurrencesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
