from .models import *
from rest_framework import serializers


class TrademarkProfile_serializer(serializers.ModelSerializer):
    class Meta:
        model = TrademarkProfile
        fields = '__all__'


class TrademarkParticulars_serializer(serializers.ModelSerializer):
    class Meta:
        model = TrademarkParticulars
        fields = '__all__'
