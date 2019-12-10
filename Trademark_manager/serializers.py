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


class AssignmentMergerAction_serializer(serializers.ModelSerializer):
    model = AssignmentMergerAction
    fields = '__all__'


class CertificateProcurementAction_serializer(serializers.ModelSerializer):
    model = CertificateProcurementAction
    fields = '__all__'


class ChangeName_AddressAction_serializer(serializers.ModelSerializer):
    model = ChangeName_AddressAction
    fields = '__all__'


class ReclassificationAction_serializer(serializers.ModelSerializer):
    model = ReclassificationAction
    fields = '__all__'


class RegistrationAction_serializer(serializers.ModelSerializer):
    model = RegistrationAction
    fields = '__all__'


class RenewalAction_serializer(serializers.ModelSerializer):
    model = RenewalAction
    fields = '__all__'


class SearchAction(serializers.ModelSerializer):
    model = SearchAction
    fields = '__all__'
