from django.shortcuts import render
from django.http import FileResponse, HttpResponse, Http404
from rest_framework import generics, filters, pagination
from .models import *
from .serializers import *


# Create your views here.
class TrademarkProfile_view(generics.ListCreateAPIView):
    queryset = TrademarkProfile.objects.all()
    serializer_class = TrademarkProfile_serializer


class TrademarkAction1_view(generics.ListCreateAPIView):
    queryset = TrademarkAction1.objects.all()
    serializer_class = TrademarkAction1_serializer


class TrademarkAction2_view(generics.ListCreateAPIView):
    queryset = TrademarkAction2.objects.all()
    serializer_class = TrademarkAction2_serializer


class TrademarkParticulars_view(generics.ListCreateAPIView):
    queryset = TrademarkParticulars.objects.all()
    serializer_class = TrademarkParticulars_serializer


class Profile_Actions_Relative_view(generics.ListCreateAPIView):
    """docstring for Profile_Actions_Relative."""
    queryset = Profile_Actions_Relative.objects.all()
    serializer_class = Profile_Actions_Relative_serializer
