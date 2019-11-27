from .models import *
from rest_framework import serializers


class TrademarkProfile_serializer(serializers.ModelSerializer):
    class Meta:
        model = TrademarkProfile
        fields = '__all__'


class TrademarkAction1_serializer(serializers.ModelSerializer):
    class Meta:
        model = TrademarkAction1
        fields = '__all__'


class TrademarkAction2_serializer(serializers.ModelSerializer):
    class Meta:
        model = TrademarkAction2
        fields = '__all__'


class TrademarkParticulars_serializer(serializers.ModelSerializer):
    class Meta:
        model = TrademarkParticulars
        fields = '__all__'

class Profile_Actions_Relative_serializer(serializers.ModelSerializer):
    profile = TrademarkProfile()
    action1 = TrademarkAction1()
    action2 = TrademarkAction2()
    class Meta:
        model = Profile_Actions_Relative
        # fields = ('profile','action1','action2')
        fields = '__all__'
