from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import ConvertSerializer, CurrencySerializer
from .models import Currency


class Convert(APIView):
    def post(self, request):
        serializer = ConvertSerializer(data=request.data)
        if serializer.is_valid():
            from_cur = request.data.get('from_cur')
            to_cur = request.data.get('to_cur')
            value = float(request.data.get('value'))
            try:
                from_currency = Currency.objects.get(short_name=from_cur)
                to_currency = Currency.objects.get(short_name=to_cur)
            except Currency.DoesNotExist:
                return Response(data={"error": "Not found this currency"}, status=404)
            result = value / from_currency.value * to_currency.value
            return Response(data={'result': result})
        else:
            return Response(data=serializer.errors, status=400)


class CurrencyList(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
