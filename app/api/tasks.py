import urllib3
import json

from django.conf import settings
from celery import shared_task
from .models import Currency


@shared_task
def update():
    Currency.objects.all().delete()
    http = urllib3.PoolManager()
    r = http.request('GET',
                     'https://api.exchangerate-api.com/v4/latest/USD',
                     )
    response_data = json.loads(r.data.decode('utf-8'))
    currencies = response_data.get('rates', None)
    result_list = []
    if currencies:
        for currency in currencies:
            if currency in settings.LIST_CURRENCY:
                result_list.append(Currency(short_name=currency, value=currencies[currency]))
        Currency.objects.bulk_create(result_list)
