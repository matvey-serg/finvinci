from django.urls import path
from .views import Convert, CurrencyList

urlpatterns = [
    path('convert', Convert.as_view(), name='convert'),
    path('currency-list', CurrencyList.as_view())
]
