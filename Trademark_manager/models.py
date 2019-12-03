import datetime
from django.core.validators import URLValidator
from django.db import models

# Create your models here.


class TrademarkAction1(models.Model):
    action_name = models.CharField(default="default action", max_length=50)
    # profile = models.ForeignKey(TrademarkProfile, on_delete=models.CASCADE, null=True)


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

    action1 = models.ForeignKey(TrademarkAction1, on_delete=models.CASCADE, null=True)
    # action2 = models.ForeignKey(TrademarkAction2, on_delete=models.CASCADE, null=True, related_name='action2')
