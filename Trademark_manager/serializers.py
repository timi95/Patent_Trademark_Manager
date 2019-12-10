from .models import *
from rest_framework import serializers


class TrademarkProfile_serializer(serializers.ModelSerializer):
    class Meta:
        model = TrademarkProfile
        fields = '__all__'
        depth = 1


class AmendementAction_serializer(serializers.ModelSerializer):
    model = AmendementAction
    fields = '__all__'
