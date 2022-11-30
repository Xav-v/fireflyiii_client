from fireflyiii_client.paths.api_v1_tags_tag.get import ApiForget
from fireflyiii_client.paths.api_v1_tags_tag.put import ApiForput
from fireflyiii_client.paths.api_v1_tags_tag.delete import ApiFordelete


class ApiV1TagsTag(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
