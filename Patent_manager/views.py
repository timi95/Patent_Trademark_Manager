from django.shortcuts import render
from django.shortcuts import render
from django.http import FileResponse, HttpResponse, Http404
from rest_framework import generics, filters, pagination
from django_filters.rest_framework import DjangoFilterBackend,DateTimeFromToRangeFilter
from .models import *
from .serializers import *
from .custom_filters import *
from rest_framework.response import Response

# Create your views here.
# I need to make separate classes inheriting from the list-create views, and RUD views
# I need to update my naming strategy, the underscore is annoying

# def get_queryset(self, Model):
#     user = self.request.user
#     entities = Model.objects.all()
#     date_from = self.request.query_params.get('date_from')
#     date_to = self.request.query_params.get('date_to')

#     if date_from and date_to:
#         entities = entities.filter(date__range=convert_to_UTC('Asia/Kolkata', date_from, date_to))
#     return entities

# Patent Particulars 
class PatentParticularsViewLC(generics.ListCreateAPIView):
    queryset = PatentParticlars.objects.all()
    serializer_class = PatentParticulars_serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    

class PatentParticularsViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatentParticlars.objects.all()
    serializer_class = PatentParticulars_serializer

# Ammendment Action
class AmendementActionViewLC(generics.ListCreateAPIView):
    queryset = AmendmentAction.objects.all()
    serializer_class = AmendmentAction_serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    # def get(self, request, *args, **kwargs):
    #     print(next(iter(request.query_params)))
    #     if next(iter(request.query_params)) is 'date_from':
    #         self.queryset = AmendmentAction.objects.filter(
    #             date_amendment_instruction_received__range=[
    #                 self.request.query_params['date_from'],
    #                 self.request.query_params['date_to']
    #                 ]
    #             )
    #     return super().get(request, *args, **kwargs)

class AmendementActionViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = AmendmentAction.objects.all()
    serializer_class = AmendmentAction_serializer

# Assignment merger
class AssignmentMergerActionViewLC(generics.ListCreateAPIView):
    queryset = AssignmentMergerAction.objects.all()
    serializer_class = AssignmentMergerAction_serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
        
class AssignmentMergerActionViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = AssignmentMergerAction.objects.all()
    serializer_class = AssignmentMergerAction_serializer    

# ChangeOFAdressView
class ChangeOfAddressViewLC(generics.ListCreateAPIView):
    queryset = ChangeOfAddressAction.objects.all()                                  
    serializer_class = ChangeOfAddress_serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

class ChangeOfAddressViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChangeOfAddressAction.objects.all()                                  
    serializer_class = ChangeOfAddress_serializer

# ChangeOfNameView
class ChangeOfNameViewLC(generics.ListCreateAPIView):
    queryset = ChangeOfNameAction.objects.all()
    serializer_class = ChangeOfName_serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

class ChangeOfNameViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChangeOfNameAction.objects.all()
    serializer_class = ChangeOfName_serializer

# CTCView
class CTCViewLC(generics.ListCreateAPIView):
    queryset = CTCAction.objects.all()
    serializer_class = CTC_serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

class CTCViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = CTCAction.objects.all()
    serializer_class = CTC_serializer

# ProcurementOfCertificationView
class ProcurementOfCertificationViewLC(generics.ListCreateAPIView):
    queryset = ProcurementOfCertificateAction.objects.all()
    serializer_class = ProcurementOfCertification_serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

class ProcurementOfCertificationViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProcurementOfCertificateAction.objects.all()
    serializer_class = ProcurementOfCertification_serializer

# RegistrationView
class RegistrationViewLC(generics.ListCreateAPIView):
    queryset = RegistrationAction.objects.all()
    serializer_class = Registration_serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

class RegistrationViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistrationAction.objects.all()
    serializer_class = Registration_serializer

# RenewalsView
class RenewalsViewLC(generics.ListCreateAPIView):
    queryset = RenewalAction.objects.all()
    serializer_class = Registration_serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

class RenewalsViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = RenewalAction.objects.all()
    serializer_class = Registration_serializer

# SearchView
class SearchViewLC(generics.ListCreateAPIView):
    queryset = SearchAction.objects.all()
    serializer_class = Search_serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

class SearchViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = SearchAction.objects.all()
    serializer_class = Search_serializer


exec(open('Patent_manager/test_script.py').read())
