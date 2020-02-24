from django.shortcuts import render
from django.shortcuts import render
from django.http import FileResponse, HttpResponse, Http404
from rest_framework import generics, filters, pagination
from .models import *
from .serializers import *

# Create your views here.
class PatentParticulars_view(generics.ListCreateAPIView,
                    generics.RetrieveUpdateDestroyAPIView):
    queryset = PatentParticlars.objects.all()
    serializer_class = PatentParticulars_serializer


class AmendementAction_view(generics.ListCreateAPIView,
                            generics.RetrieveUpdateDestroyAPIView):
    queryset = AmendmentAction.objects.all()
    serializer_class = AmendmentAction_serializer


class AssignmentMergerAction_view(generics.ListCreateAPIView,
                                  generics.RetrieveUpdateDestroyAPIView):
    queryset = AssignmentMergerAction.objects.all()
    serializer_class = AssignmentMergerAction_serializer


class ChangeOfAddress_view(generics.ListCreateAPIView,
                        generics.RetrieveUpdateDestroyAPIView):
    queryset = ChangeOfAddressAction.objects.all()                                  
    serializer_class = ChangeOfAddress_serializer


class ChangeOfName_view(generics.ListCreateAPIView,
                        generics.RetrieveUpdateDestroyAPIView):
    queryset = ChangeOfNameAction.objects.all()
    serializer_class = ChangeOfName_serializer


class CTC_view(generics.ListCreateAPIView,
                generics.RetrieveUpdateDestroyAPIView):
    queryset = CTCAction.objects.all()
    serializer_class = CTC_serializer


class ProcurementOfCertification_view(generics.ListCreateAPIView,
                                     generics.RetrieveUpdateDestroyAPIView):
    queryset = ProcurementOfCertificateAction
    serialzer_class = ProcurementOfCertification_serializer


class Registration_view(generics.ListCreateAPIView,
                        generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistrationAction
    serializer_class = Registration_serializer


class Renewals_view(generics.ListCreateAPIView,
                                  generics.RetrieveUpdateDestroyAPIView):
    queryset = RenewalAction
    serializer_class = Registration_serializer


class Search_view(generics.ListCreateAPIView,
                  generics.RetrieveUpdateDestroyAPIView):
    queryset = SearchAction
    serializer_class = Search_serializer