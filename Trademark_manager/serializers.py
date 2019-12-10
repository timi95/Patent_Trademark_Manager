from .models import *
from rest_framework import serializers


class TrademarkProfile_serializer(serializers.ModelSerializer):
    class Meta:
        model = TrademarkProfile
        fields = '__all__'
        depth = 1


class AmendementAction_serializer(serializers.ModelSerializer):
    class Meta:
        model = AmendementAction
        fields = '__all__'


class AssignmentMergerAction_serializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentMergerAction
        fields = '__all__'


class CertificateProcurementAction_serializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateProcurementAction
        fields = '__all__'


class ChangeName_AddressAction_serializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ChangeName_AddressAction


class ReclassificationAction_serializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ReclassificationAction


class RegistrationAction_serializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = RegistrationAction


class RenewalAction_serializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = RenewalAction


class SearchAction_serializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = SearchAction
