from django.shortcuts import render
from django.http import FileResponse, HttpResponse, Http404
from rest_framework import generics, filters, pagination
from .models import *
from .serializers import *


# Create your views here.
class TrademarkProfile_view(generics.ListCreateAPIView):
    queryset = TrademarkProfile.objects.all()
    serializer_class = TrademarkProfile_serializer

class TrademarkParticulars_view(generics.ListCreateAPIView):
    queryset = TrademarkParticulars.objects.all()
    serializer_class = TrademarkParticulars_serializer
