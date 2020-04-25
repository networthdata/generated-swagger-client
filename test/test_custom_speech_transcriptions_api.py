# coding: utf-8

"""
    Speech Services API v2.0

    Speech Services API v2.0.  # noqa: E501

    OpenAPI spec version: v2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.custom_speech_transcriptions_api import CustomSpeechTranscriptionsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCustomSpeechTranscriptionsApi(unittest.TestCase):
    """CustomSpeechTranscriptionsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.custom_speech_transcriptions_api.CustomSpeechTranscriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_transcription(self):
        """Test case for create_transcription

        Creates a new transcription.  # noqa: E501
        """
        pass

    def test_delete_transcription(self):
        """Test case for delete_transcription

        Deletes the specified transcription task.  # noqa: E501
        """
        pass

    def test_get_supported_locales_for_transcriptions_b_ba(self):
        """Test case for get_supported_locales_for_transcriptions_b_ba

        Gets a list of supported locales for offline transcriptions.  # noqa: E501
        """
        pass

    def test_get_transcription(self):
        """Test case for get_transcription

        Gets the transcription identified by the given ID.  # noqa: E501
        """
        pass

    def test_get_transcriptions(self):
        """Test case for get_transcriptions

        Gets a list of transcriptions for the authenticated subscription.  # noqa: E501
        """
        pass

    def test_update_transcription(self):
        """Test case for update_transcription

        Updates the mutable details of the transcription identified by its ID.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()