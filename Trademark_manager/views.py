from django.shortcuts import render
from django.http import FileResponse, HttpResponse, Http404
from rest_framework import generics, filters, pagination
from .models import *
from .serializers import *
from Trademark_excel_assets.excel_service import *


# Create your views here.
class TrademarkProfile_view(generics.ListCreateAPIView,
                            generics.RetrieveUpdateDestroyAPIView):
    queryset = TrademarkProfile.objects.all()
    serializer_class = TrademarkProfile_serializer
    # def dispatch(self, request, args, kwargs):
    #


class AmendementAction_view(generics.ListCreateAPIView,
                            generics.RetrieveUpdateDestroyAPIView):
    queryset = AmendementAction.objects.all()
    serializer_class = AmendementAction_serializer


class AssignmentMergerAction_view(generics.ListCreateAPIView,
                                  generics.RetrieveUpdateDestroyAPIView):
    queryset = AssignmentMergerAction.objects.all()
    serializer_class = AssignmentMergerAction_serializer


class CertificateProcurementAction_view(generics.ListCreateAPIView,
                                        generics.RetrieveUpdateDestroyAPIView):
    queryset = CertificateProcurementAction.objects.all()
    serializer_class = CertificateProcurementAction_serializer


class ChangeName_AddressAction_view(generics.ListCreateAPIView,
                                        generics.RetrieveUpdateDestroyAPIView):
    queryset = ChangeName_AddressAction.objects.all()
    serializer_class = ChangeName_AddressAction_serializer


class RegistrationAction_view(generics.ListCreateAPIView,
                              generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistrationAction.objects.all()
    serializer_class = RegistrationAction_serializer


class RenewalAction_view(generics.ListCreateAPIView,
                         generics.RetrieveUpdateDestroyAPIView):
    queryset = RenewalAction.objects.all()
    serializer_class = RenewalAction_serializer


class SearchAction_view(generics.ListCreateAPIView,
                         generics.RetrieveUpdateDestroyAPIView):
    queryset = SearchAction.objects.all()
    serializer_class = SearchAction_serializer


# testing the data wrangling service
# which will become the import feature from excel files
HelloService(SearchAction)
