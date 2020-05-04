from .models import *
from rest_framework import serializers

# Patent Management serializers

class PatentParticulars_serializer(serializers.ModelSerializer):
    class Meta:
        model = PatentParticlars
        fields = '__all__'
        depth = 1


class AmendmentAction_serializer(serializers.ModelSerializer):
    class Meta:
        model = AmendmentAction
        fields = '__all__'
        depth = 1


class AssignmentMergerAction_serializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentMergerAction
        fields = '__all__'



class ChangeOfAddress_serializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeOfAddressAction
        fields = '__all__'


class ChangeOfName_serializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeOfNameAction
        fields = '__all__'


class CTC_serializer(serializers.ModelSerializer):
    class Meta:
        model = CTCAction
        fields = '__all__'


class ProcurementOfCertification_serializer(serializers.ModelSerializer):
    class Meta:
        model = ProcurementOfCertificateAction
        fields = '__all__'


class Registration_serializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationAction
        fields = '__all__'


class Renewal_serializer(serializers.ModelSerializer):
    class Meta:
        model = RenewalAction
        fields = '__all__'


class Search_serializer(serializers.ModelSerializer):
    class Meta:
        model = SearchAction
        fields = '__all__'





