from .models import *
from rest_framework import serializers
from Patent_Trademark_Strings.Trademarks_Act_Form_33_String import Form33StringClass



class Form_3_serializer(serializers.ModelSerializer):
    class Meta:
        model = Form_3_Model
        fields = '__all__'

class Form_33_serializer(serializers.ModelSerializer):
    class Meta:
        model = Form_33_Model
        fields = '__all__'


class Form_2_serializer(serializers.ModelSerializer):
    class Meta:
        model = Form_2_Model
        fields = '__all__'

class Form_22_serializer(serializers.ModelSerializer):
    class Meta:
        model = Form_22_Model
        fields = '__all__'


class Form_17_serializer(serializers.ModelSerializer):
    class Meta:
        model = Form_17_Model
        fields = '__all__'


class Form_12_serializer(serializers.ModelSerializer):
    class Meta:
        model = Form_12_Model
        fields = '__all__'

class Form_1_serializer(serializers.ModelSerializer):
    class Meta:
        model = Form_1_Model
        fields = '__all__'
