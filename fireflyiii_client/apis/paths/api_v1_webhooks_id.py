from fireflyiii_client.paths.api_v1_webhooks_id.get import ApiForget
from fireflyiii_client.paths.api_v1_webhooks_id.put import ApiForput
from fireflyiii_client.paths.api_v1_webhooks_id.delete import ApiFordelete


class ApiV1WebhooksId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
