from fireflyiii_client.paths.api_v1_categories_id.get import ApiForget
from fireflyiii_client.paths.api_v1_categories_id.put import ApiForput
from fireflyiii_client.paths.api_v1_categories_id.delete import ApiFordelete


class ApiV1CategoriesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
