# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class DeviceTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.trusted_comms.devices.create(phone_number="phone_number", push_token="push_token")

        values = {'PhoneNumber': "phone_number", 'PushToken': "push_token", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/TrustedComms/Devices',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "binding_sid": "BSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "phone_number": "+573000000000",
                "sid": "DDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://preview.twilio.com/TrustedComms/Devices"
            }
            '''
        ))

        actual = self.client.preview.trusted_comms.devices.create(phone_number="phone_number", push_token="push_token")

        self.assertIsNotNone(actual)
