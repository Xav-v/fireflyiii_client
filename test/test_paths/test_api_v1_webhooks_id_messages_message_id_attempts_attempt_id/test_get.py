# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import fireflyiii_client
from fireflyiii_client.paths.api_v1_webhooks_id_messages_message_id_attempts_attempt_id import get  # noqa: E501
from fireflyiii_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV1WebhooksIdMessagesMessageIdAttemptsAttemptId(ApiTestMixin, unittest.TestCase):
    """
    ApiV1WebhooksIdMessagesMessageIdAttemptsAttemptId unit test stubs
        Get a single failed attempt from a single webhook message.  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
