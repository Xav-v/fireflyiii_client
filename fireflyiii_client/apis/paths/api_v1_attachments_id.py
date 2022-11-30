from fireflyiii_client.paths.api_v1_attachments_id.get import ApiForget
from fireflyiii_client.paths.api_v1_attachments_id.put import ApiForput
from fireflyiii_client.paths.api_v1_attachments_id.delete import ApiFordelete


class ApiV1AttachmentsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
