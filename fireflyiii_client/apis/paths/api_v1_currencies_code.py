from fireflyiii_client.paths.api_v1_currencies_code.get import ApiForget
from fireflyiii_client.paths.api_v1_currencies_code.put import ApiForput
from fireflyiii_client.paths.api_v1_currencies_code.delete import ApiFordelete


class ApiV1CurrenciesCode(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
