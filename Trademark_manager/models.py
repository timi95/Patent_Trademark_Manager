import datetime
from django.core.validators import URLValidator
from django.db import models

# Create your models here.


class RenewalAction(models.Model):
    date_renewal_cert_facilitation_sent = models.CharField()
    dt_abj_instructed_renewal = models.CharField()
    dt_renew_cert_received = models.CharField()
    next_renewal_due_date = models.CharField()
    next_renewal_due_month = models.CharField()
    official_fee_renewal = models.CharField()
    renewal_cert_facilitation_sent = models.CharField()
    renewal_due_date = models.CharField()
    renewal_due_month = models.CharField()
    renewal_instruction_date = models.CharField()
    renewal_instruction_month = models.CharField()
    renewal_status = models.CharField()
    


class SearchAction(models.Model):
    clerk_searching = models.CharField()
    conflicting_mark = models.CharField()
    date_of_search_report = models.CharField()
    date_reported_to_client = models.CharField()
    official_search_fee = models.CharField()
    reported_to_client = models.CharField()
    search_instruction_date = models.CharField()
    search_status = models.CharField()
    search_type =  models.CharField()

class TrademarkProfile(models.Model):
    client_name = models.CharField(default="default client name", max_length=50)
    client_ref_no = models.CharField()
    correspondence_date = models.CharField()
    current_instruction = models.CharField()
    current_status = models.CharField()
    date_instruction_received = models.CharField()
    date_current_instruction = models.CharField()
    date_completed_job_received = models.CharField()
    date_incoming_abj_schedule = models.CharField()
    date_outgoing_abj_schedule = models.CharField()
    filing_receipt = models.CharField()
    goods = models.CharField()
    incentive_due_clerk = models.CharField()
    lawyer_responsible = models.CharField()
    month_incoming_schedule = models.CharField()
    month_outgoing_schedule = models.CharField()
    name_of_client = models.CharField()
    name_of_proprietor = models.CharField()
    official_fee_ctc = models.CharField()
    official_fee_late_renewal_penalty = models.CharField()
    official_fee_merger = models.CharField()
    official_fee_registered_user = models.CharField()
    our_ref_no = models.CharField()
    proprietors_address = models.CharField()
    quicktellers_fee = models.CharField()
    registration_no = models.CharField()
    trademark_description = models.CharField()

    search_action = models.ForeignKey(SearchAction, on_delete=models.CASCADE, null=True)
    renewal_action = models.ForeignKey(RenewalAction, on_delete=models.CASCADE, null=True)
    # action2 = models.ForeignKey(TrademarkAction2, on_delete=models.CASCADE, null=True, related_name='action2')
