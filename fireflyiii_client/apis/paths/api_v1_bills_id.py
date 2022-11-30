from fireflyiii_client.paths.api_v1_bills_id.get import ApiForget
from fireflyiii_client.paths.api_v1_bills_id.put import ApiForput
from fireflyiii_client.paths.api_v1_bills_id.delete import ApiFordelete


class ApiV1BillsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
