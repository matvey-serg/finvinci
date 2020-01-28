from rest_framework import serializers

from .models import Currency

class ConvertSerializer(serializers.Serializer):
    from_cur = serializers.CharField()
    to_cur = serializers.CharField()
    value = serializers.FloatField()


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        modele = Currency
        fields = ('short_name', 'value')
