from django.shortcuts import render
from django.shortcuts import render
from django.http import FileResponse, HttpResponse, Http404
from rest_framework import generics, filters, pagination
from .models import *
from .serializers import *

# Create your views here.
# I need to make separate classes inheriting from the list-create views, and RUD views
# I need to update my naming strategy, the underscore is annoying

# Patent Particulars 
class PatentParticularsViewLC(generics.ListCreateAPIView):
    queryset = PatentParticlars.objects.all()
    serializer_class = PatentParticulars_serializer

class PatentParticularsViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatentParticlars.objects.all()
    serializer_class = PatentParticulars_serializer

# Ammendment Action
class AmendementActionViewLC(generics.ListCreateAPIView):
    queryset = AmendmentAction.objects.all()
    serializer_class = AmendmentAction_serializer

class AmendementActionViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = AmendmentAction.objects.all()
    serializer_class = AmendmentAction_serializer

# Assignment merger
class AssignmentMergerActionViewLC(generics.ListCreateAPIView):
    queryset = AssignmentMergerAction.objects.all()
    serializer_class = AssignmentMergerAction_serializer
    
class AssignmentMergerActionViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = AssignmentMergerAction.objects.all()
    serializer_class = AssignmentMergerAction_serializer    


# ChangeOFAdressView
class ChangeOfAddressViewLC(generics.ListCreateAPIView):
    queryset = ChangeOfAddressAction.objects.all()                                  
    serializer_class = ChangeOfAddress_serializer
class ChangeOfAddressViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChangeOfAddressAction.objects.all()                                  
    serializer_class = ChangeOfAddress_serializer

# ChangeOfNameView
class ChangeOfNameViewLC(generics.ListCreateAPIView):
    queryset = ChangeOfNameAction.objects.all()
    serializer_class = ChangeOfName_serializer
class ChangeOfNameViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChangeOfNameAction.objects.all()
    serializer_class = ChangeOfName_serializer

# CTCView
class CTCViewLC(generics.ListCreateAPIView):
    queryset = CTCAction.objects.all()
    serializer_class = CTC_serializer
class CTCViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = CTCAction.objects.all()
    serializer_class = CTC_serializer

# ProcurementOfCertificationView
class ProcurementOfCertificationViewLC(generics.ListCreateAPIView):
    queryset = ProcurementOfCertificateAction.objects.all()
    serializer_class = ProcurementOfCertification_serializer
class ProcurementOfCertificationViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProcurementOfCertificateAction.objects.all()
    serializer_class = ProcurementOfCertification_serializer

# RegistrationView
class RegistrationViewLC(generics.ListCreateAPIView):
    queryset = RegistrationAction.objects.all()
    serializer_class = Registration_serializer
class RegistrationViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistrationAction.objects.all()
    serializer_class = Registration_serializer

# RenewalsView
class RenewalsViewLC(generics.ListCreateAPIView):
    queryset = RenewalAction.objects.all()
    serializer_class = Registration_serializer
class RenewalsViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = RenewalAction.objects.all()
    serializer_class = Registration_serializer

# SearchView
class SearchViewLC(generics.ListCreateAPIView):
    queryset = SearchAction.objects.all()
    serializer_class = Search_serializer
class SearchViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = SearchAction.objects.all()
    serializer_class = Search_serializer