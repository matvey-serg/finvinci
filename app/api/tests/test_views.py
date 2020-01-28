import json

from django.test import TestCase, Client
from django.urls import reverse

from ..models import Currency

client = Client()


class BaseCurrencyDataTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            "from_cur": "USD",
            "to_cur": "EUR",
            "value": 100
        }

        self.invalid_value = {
            "from_cur": "USD",
            "to_cur": "EUR",
            "value": "100asd1000"
        }

        self.invalid_cur = {
            "from_cur": "AAA",
            "to_cur": "AAA",
            "value": 100
        }
        Currency.objects.create(
            short_name='CZK', value=22.85)
        Currency.objects.create(
            short_name='EUR', value=0.907)
        Currency.objects.create(
            short_name='PLN', value=3.868)
        Currency.objects.create(
            short_name='USD', value=1)

    def test_convert_valid_currency(self):
        result = {
            "result": 90.7
        }
        response = client.post(
            reverse('convert'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, result)

    def test_convert_invalid_amount(self):
        response = client.post(
            reverse('convert'),
            data=json.dumps(self.invalid_value),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_convert_invalid_currency(self):
        response = client.post(
            reverse('convert'),
            data=json.dumps(self.invalid_cur),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)



