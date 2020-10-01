from django.shortcuts import render
from django.http import FileResponse, HttpResponse, Http404
from rest_framework import generics, filters, pagination
from .models import *
from .serializers import *
from Trademark_excel_assets.excel_service import *


# Create your views here.

# TrademarkProfile
class TrademarkProfileViewLC(generics.ListCreateAPIView):
    queryset = TrademarkProfile.objects.all()
    serializer_class = TrademarkProfile_serializer
    
class TrademarkProfileViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrademarkProfile.objects.all()
    serializer_class = TrademarkProfile_serializer


# Ammendment Action
class AmendementActionViewLC(generics.ListCreateAPIView):
    queryset = AmendementAction.objects.all()
    serializer_class = AmendementAction_serializer

class AmendementActionViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = AmendementAction.objects.all()
    serializer_class = AmendementAction_serializer


# Assignment Merger
class AssignmentMergerActionViewLC(generics.ListCreateAPIView):
    queryset = AssignmentMergerAction.objects.all()
    serializer_class = AssignmentMergerAction_serializer

class AssignmentMergerActionViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = AssignmentMergerAction.objects.all()
    serializer_class = AssignmentMergerAction_serializer


# Certificate Procurement 
class CertificateProcurementActionViewLC(generics.ListCreateAPIView):
    queryset = CertificateProcurementAction.objects.all()
    serializer_class = CertificateProcurementAction_serializer

class CertificateProcurementActionViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = CertificateProcurementAction.objects.all()
    serializer_class = CertificateProcurementAction_serializer


# Change Name Address
class ChangeName_AddressActionViewLC(generics.ListCreateAPIView):
    queryset = ChangeName_AddressAction.objects.all()
    serializer_class = ChangeName_AddressAction_serializer

class ChangeName_AddressActionViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChangeName_AddressAction.objects.all()
    serializer_class = ChangeName_AddressAction_serializer


# Registration
class RegistrationActionViewLC(generics.ListCreateAPIView):
    queryset = RegistrationAction.objects.all()
    serializer_class = RegistrationAction_serializer

class RegistrationActionViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistrationAction.objects.all()
    serializer_class = RegistrationAction_serializer


# Renewal
class RenewalActionViewLC(generics.ListCreateAPIView):
    queryset = RenewalAction.objects.all()
    serializer_class = RenewalAction_serializer

class RenewalActionViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = RenewalAction.objects.all()
    serializer_class = RenewalAction_serializer


# Reclassification
class ReclassificationActionViewLC(generics.ListCreateAPIView):
    queryset = ReclassificationAction.objects.all()
    serializer_class = ReclassificationAction_serializer


class ReclassificationActionViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = RenewalAction.objects.all()
    serializer_class = RenewalAction_serializer


# Search
class SearchActionViewLC(generics.ListCreateAPIView):
    queryset = SearchAction.objects.all()
    serializer_class = SearchAction_serializer

class SearchActionViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = SearchAction.objects.all()
    serializer_class = SearchAction_serializer
