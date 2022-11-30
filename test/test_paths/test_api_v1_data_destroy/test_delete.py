# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import fireflyiii_client
from fireflyiii_client.paths.api_v1_data_destroy import delete  # noqa: E501
from fireflyiii_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV1DataDestroy(ApiTestMixin, unittest.TestCase):
    """
    ApiV1DataDestroy unit test stubs
        Endpoint to destroy user data  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()