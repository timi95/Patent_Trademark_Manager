from django.shortcuts import render
from django.shortcuts import render
from django.http import FileResponse, HttpResponse, Http404
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend,DateTimeFromToRangeFilter
from django.db.models import Q
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
    def get(self, request, *args, **kwargs):
        if request.query_params and list(iter(request.query_params))[0] == 'date_from':
            self.queryset = PatentParticlars.objects.filter(
                Q(date_outgoing_abuja_schedule__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(date_incoming_abuja_schedule__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(date_completed_job_received__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(date_of_instruction__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(date_instruction_received__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(date_certificate_procurement_due__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])                
                )
        return super().get(request, *args, **kwargs)    
    

class PatentParticularsViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatentParticlars.objects.all()
    serializer_class = PatentParticulars_serializer

# Ammendment Action
class AmendementActionViewLC(generics.ListCreateAPIView):
    queryset = AmendmentAction.objects.all()
    serializer_class = AmendmentAction_serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    def get(self, request, *args, **kwargs):
        if request.query_params and list(iter(request.query_params))[0] == 'date_from':
            self.queryset = AmendmentAction.objects.filter(
                Q(date_amending_clerk_instructed__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(date_amendment_instruction_received__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(date_amendment_received__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])                
                )
        return super().get(request, *args, **kwargs)

class AmendementActionViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = AmendmentAction.objects.all()
    serializer_class = AmendmentAction_serializer

# Assignment merger
class AssignmentMergerActionViewLC(generics.ListCreateAPIView):
    queryset = AssignmentMergerAction.objects.all()
    serializer_class = AssignmentMergerAction_serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    def get(self, request, *args, **kwargs):
        if request.query_params and list(iter(request.query_params))[0] == 'date_from':
            self.queryset = AssignmentMergerAction.objects.filter(
                Q(date_assignment_certificate_received__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(date_abuja_instructed_assignment__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(assignment_instruction_date__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])              
                )
        return super().get(request, *args, **kwargs)    
  
        
class AssignmentMergerActionViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = AssignmentMergerAction.objects.all()
    serializer_class = AssignmentMergerAction_serializer    

# ChangeOFAdressView
class ChangeOfAddressViewLC(generics.ListCreateAPIView):
    queryset = ChangeOfAddressAction.objects.all()                                  
    serializer_class = ChangeOfAddress_serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    def get(self, request, *args, **kwargs):
        if request.query_params and list(iter(request.query_params))[0] == 'date_from':
            self.queryset = ChangeOfAddressAction.objects.filter(
                Q(change_of_address_instruction_date__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(date_received_change_of_address_certificate__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])          
                )
        return super().get(request, *args, **kwargs)     

class ChangeOfAddressViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChangeOfAddressAction.objects.all()                                  
    serializer_class = ChangeOfAddress_serializer

# ChangeOfNameView
class ChangeOfNameViewLC(generics.ListCreateAPIView):
    queryset = ChangeOfNameAction.objects.all()
    serializer_class = ChangeOfName_serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    def get(self, request, *args, **kwargs):
        if request.query_params and list(iter(request.query_params))[0] == 'date_from':
            self.queryset = ChangeOfNameAction.objects.filter(
                Q(change_of_name_instruction_date__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(date_received_change_of_name_certificate__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])          
                )
        return super().get(request, *args, **kwargs)       

class ChangeOfNameViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChangeOfNameAction.objects.all()
    serializer_class = ChangeOfName_serializer

# CTCView
class CTCViewLC(generics.ListCreateAPIView):
    queryset = CTCAction.objects.all()
    serializer_class = CTC_serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    def get(self, request, *args, **kwargs):
        if request.query_params and list(iter(request.query_params))[0] == 'date_from':
            self.queryset = CTCAction.objects.filter(
                Q(date_applied_for_ctc__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])          
                )
        return super().get(request, *args, **kwargs)     

class CTCViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = CTCAction.objects.all()
    serializer_class = CTC_serializer

# ProcurementOfCertificationView
class ProcurementOfCertificationViewLC(generics.ListCreateAPIView):
    queryset = ProcurementOfCertificateAction.objects.all()
    serializer_class = ProcurementOfCertification_serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    def get(self, request, *args, **kwargs):
        if request.query_params and list(iter(request.query_params))[0] == 'date_from':
            self.queryset = ProcurementOfCertificateAction.objects.filter(
            Q(date_procurement_instructed__range=[
                self.request.query_params['date_from'],
                self.request.query_params['date_to']
                ])|
            Q(date_cert_procurement_due__range=[
                self.request.query_params['date_from'],
                self.request.query_params['date_to']
                ]) 
            )
        return super().get(request, *args, **kwargs)     

class ProcurementOfCertificationViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProcurementOfCertificateAction.objects.all()
    serializer_class = ProcurementOfCertification_serializer

# RegistrationView
class RegistrationViewLC(generics.ListCreateAPIView):
    queryset = RegistrationAction.objects.all()
    serializer_class = Registration_serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    def get(self, request, *args, **kwargs):
        if request.query_params and list(iter(request.query_params))[0] == 'date_from':
            self.queryset = RegistrationAction.objects.filter(
                Q(date_registration_instruction_received__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(date_abuja_instructed_for_registration__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(acceptance_date__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(cert_procurement_date__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(correspondence_date__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(date_of_instruction__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])                                                      
                )
        return super().get(request, *args, **kwargs)     

class RegistrationViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistrationAction.objects.all()
    serializer_class = Registration_serializer

# RenewalsView
class RenewalsViewLC(generics.ListCreateAPIView):
    queryset = RenewalAction.objects.all()
    serializer_class = Registration_serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    def get(self, request, *args, **kwargs):
        if request.query_params and list(iter(request.query_params))[0] == 'date_from':
            self.queryset = RenewalAction.objects.filter(
                Q(patent_start_date__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(patent_end_date__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(renewal_instruction_date__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(renewal_due_date__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(date_abuja_instructed_renewal__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(date_renew_cert_received__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(next_renewal_due_date__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])|
                Q(renewal_extension_of_time__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])                                                       
                )
        return super().get(request, *args, **kwargs)           


class RenewalsViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = RenewalAction.objects.all()
    serializer_class = Registration_serializer

# SearchView
class SearchViewLC(generics.ListCreateAPIView):
    queryset = SearchAction.objects.all()
    serializer_class = Search_serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    def get(self, request, *args, **kwargs):
        if request.query_params and list(iter(request.query_params))[0] == 'date_from':
            self.queryset = SearchAction.objects.filter(
                Q(date_reported_to_client__range=[
                    self.request.query_params['date_from'],
                    self.request.query_params['date_to']
                    ])                                                
                )
        return super().get(request, *args, **kwargs)     


class SearchViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = SearchAction.objects.all()
    serializer_class = Search_serializer


exec(open('Patent_manager/test_script.py').read())
