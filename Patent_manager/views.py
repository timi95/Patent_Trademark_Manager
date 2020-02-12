from django.shortcuts import render
from django.shortcuts import render
from django.http import FileResponse, HttpResponse, Http404
from rest_framework import generics, filters, pagination
from .models import *
from .serializers import *

# Create your views here.
class PatentParticulars_view(generics.ListCreateAPIView,
                    generics.RetrieveUpdateDestroyAPIView):
    queryset = PatentParticulars.objects.all()
    serializer_class = PatentParticulars_serializer


class AmendementAction_view(generics.ListCreateAPIView,
                            generics.RetrieveUpdateDestroyAPIView):
    queryset = AmendementAction.objects.all()
    serializer_class = AmendementAction_serializer