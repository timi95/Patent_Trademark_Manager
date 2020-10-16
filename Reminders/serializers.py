from .models import *
from rest_framework import serializers

# Patent Management serializers

class Reminder_serializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'