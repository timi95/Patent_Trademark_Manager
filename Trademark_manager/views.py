from django.shortcuts import render
from django.http import FileResponse, HttpResponse, Http404
from rest_framework import generics, filters, pagination
from .models import *
from .serializers import *


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



import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile



filename = '/home/psykinetic/workspace/Python_and_Django/Patent_Trademark_Manager/Trademark_manager/Trademark_excel_assets/Search.xlsx'

df = pd.read_excel(filename, 'Sheet1')

    # clerk_searching,
    # conflicting_mark,
    # date_of_search_report,
    # date_reported_to_client,
    # official_search_fee,
    # reported_to_client,
    # search_instruction_date,
    # search_status,
    # search_type
    #
    #
    # clerk_searching = models.CharField(default="default value", max_length=50)
    # conflicting_mark = models.CharField(default="default value", max_length=50)
    # date_of_search_report = models.DateField()
    # date_reported_to_client = models.CharField(default="default value", max_length=50)
    # official_search_fee = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    # reported_to_client = models.CharField(default="default value", max_length=50)
    # search_instruction_date = models.DateField()
    # search_status = models.CharField(default="default value", max_length=50)
    # search_type =  models.CharField(default="default value", max_length=50)
    #
    #
mySearchAction = SearchAction()

# print("Column headings:")
print(df.rows)

print("As if nested loops in python are a good fucking idea...")
# going by rows first
# for i in df.rows:
#     print(df.rows[i])
# for i in df.columns:
#     mySearchAction.
#     print(df.columns[i])
#     for j in df.index:
#         print(df[i][j])
