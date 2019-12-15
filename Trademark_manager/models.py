import datetime
from django.core.validators import URLValidator
from django.db import models

# Create your models here.


class AmendementAction(models.Model):
    ammendement_instruction_date = models.DateField()
    date_ammendement_instruction_received = models.DateField()
    nature_of_amendement = models.CharField(default="default value", max_length=50)
    date_amending_clerk_instructed = models.DateField()
    status_of_amendement = models.CharField(default="default value", max_length=50)
    date_amendement_received = models.DateField()


class AssignmentMergerAction(models.Model):
    assignment_instruction_date = models.DateField()
    assignment_instruction_month = models.CharField(default="default value", max_length=50)
    assignee = models.CharField(default="default value", max_length=50)
    assignee_address = models.CharField(default="default value", max_length=50)
    assignor = models.CharField(default="default value", max_length=50)
    assignor_address = models.CharField(default="default value", max_length=50)
    clerk_assigning = models.CharField(default="default value", max_length=50)
    date_abj_instructed_assignment = models.DateField()
    date_assignment_certificate_received = models.DateField()
    date_facillitation_assignment_cert_sent = models.DateField()
    date_facillitation_assignment_cert_sent_sent = models.DateField()
    official_fee_assignment = models.CharField(default="default value", max_length=50)
    status_assignment_registration = models.CharField(default="default value", max_length=50)


class CertificateProcurementAction(models.Model):
    date_procurement_instructed = models.DateField()
    application_no = models.CharField(default="default value", max_length=50)
    trademark_description = models.CharField(default="default value", max_length=50)
    journal_no = models.IntegerField()
    journal_vol = models.IntegerField()
    journal_date = models.DateField()
    journal_page = models.CharField(default="default value", max_length=50)
    date_clerk_instructed_to_procure = models.DateField()
    cert_procurement_status = models.CharField(default="default value", max_length=50)
    date_registration_certificate = models.DateField()
    registration_no = models.IntegerField()
    official_fee_certificate_issuance = models.DecimalField()


class ChangeName_AddressAction(models.Model):
    change_of_address_instruction_date = models.CharField(default="default value", max_length=50)
    change_of_name_instruction_date = models.CharField(default="default value", max_length=50)
    date_received_change_of_address_certificate = models.CharField(default="default value", max_length=50)
    date_received_change_of_name_certificate = models.CharField(default="default value", max_length=50)
    new_address_of_pptr = models.CharField(default="default value", max_length=50)
    new_name_of_pptr = models.CharField(default="default value", max_length=50)
    official_fee_change_name = models.CharField(default="default value", max_length=50)
    official_fee_change_address = models.CharField(default="default value", max_length=50)
    status_change_of_name = models.CharField(default="default value", max_length=50)
    status_change_of_address = models.CharField(default="default value", max_length=50)


class ReclassificationAction(models.Model):
    date_reclassification_instruction = models.CharField(default="default value", max_length=50)
    date_abj_instructed_reclassify = models.CharField(default="default value", max_length=50)
    reclassification_status = models.CharField(default="default value", max_length=50)
    date_publication_of_reclassification = models.CharField(default="default value", max_length=50)
    journal_pg_reclassification = models.CharField(default="default value", max_length=50)


class RegistrationAction(models.Model):
    acceptance_date = models.DateField()
    acceptance_facilitation_sent = models.CharField(default="default value", max_length=50)
    acknowledgement_date = models.DateField()
    acknowledgement_facilitation_sent = models.CharField(default="default value", max_length=50)
    application_no = models.CharField(default="default value", max_length=50)
    trademark_class = models.IntegerField()
    clerk_registering = models.CharField(default="default value", max_length=50)
    colour_limitation = models.CharField(default="default value", max_length=50)
    date_acceptance_facilitation_sent = models.DateField()
    date_acknowledgement_facilitation_sent = models.DateField()
    date_of_registration_instruction = models.DateField()
    date_of_registration_instruction_received = models.DateField()
    date_registration_cert_facilitation_sent = models.DateField()
    date_sent_for_publication = models.DateField()
    date_abj_instructed_for_registration = models.DateField()
    goods = models.CharField(default="default value", max_length=50)
    journal_date = models.DateField()
    journal_no = models.CharField(default="default value", max_length=50)
    journal_page = models.CharField(default="default value", max_length=50)
    journal_vol = models.CharField(default="default value", max_length=50)
    official_fee_registration = models.CharField(default="default value", max_length=50)
    publication = models.CharField(default="default value", max_length=50)
    registration_status = models.CharField(default="default value", max_length=50)
    registration_filing_month = models.CharField(default="default value", max_length=50)
    registration_no = models.CharField(default="default value", max_length=50)
    registraion_cert_facilitation_sent = models.CharField(default="default value", max_length=50)
    tm_registration_filing_date = models.DateField()


class RenewalAction(models.Model):
    date_renewal_cert_facilitation_sent = models.CharField(default="default value", max_length=50)
    dt_abj_instructed_renewal = models.CharField(default="default value", max_length=50)
    dt_renew_cert_received = models.CharField(default="default value", max_length=50)
    next_renewal_due_date = models.CharField(default="default value", max_length=50)
    next_renewal_due_month = models.CharField(default="default value", max_length=50)
    official_fee_renewal = models.CharField(default="default value", max_length=50)
    renewal_cert_facilitation_sent = models.CharField(default="default value", max_length=50)
    renewal_due_date = models.CharField(default="default value", max_length=50)
    renewal_due_month = models.CharField(default="default value", max_length=50)
    renewal_instruction_date = models.CharField(default="default value", max_length=50)
    renewal_instruction_month = models.CharField(default="default value", max_length=50)
    renewal_status = models.CharField(default="default value", max_length=50)


class SearchAction(models.Model):
    clerk_searching = models.CharField(default="default value", max_length=50)
    conflicting_mark = models.CharField(default="default value", max_length=50)
    date_of_search_report = models.CharField(default="default value", max_length=50)
    date_reported_to_client = models.CharField(default="default value", max_length=50)
    official_search_fee = models.CharField(default="default value", max_length=50)
    reported_to_client = models.CharField(default="default value", max_length=50)
    search_instruction_date = models.CharField(default="default value", max_length=50)
    search_status = models.CharField(default="default value", max_length=50)
    search_type =  models.CharField(default="default value", max_length=50)

class TrademarkProfile(models.Model):
    applicable_official_fee = models.DecimalField()
    applicable_service_charge = models.DecimalField()
    trademark_class = models.IntegerField()
    clerk_responsible = models.CharField(default="default value", max_length=50)
    clients_email_address = models.CharField(default="default value", max_length=50)
    clients_id = models.CharField(default="default value", max_length=50)
    clients_address = models.CharField(default="default value", max_length=50)
    clients_contact_person = models.CharField(default="default value", max_length=50)
    client_ref_no = models.CharField(default="default value", max_length=50)
    correspondence_date = models.DateField(auto_now=False, auto_now_add=False)
    current_instruction = models.CharField(default="default value", max_length=50)
    current_status = models.CharField(default="default value", max_length=50)
    date_instruction_received = models.DateField(auto_now=False, auto_now_add=False)
    date_current_instruction = models.DateField(auto_now=False, auto_now_add=False)
    date_completed_job_received = models.DateField(auto_now=False, auto_now_add=False)
    date_incoming_abj_schedule = models.DateField(auto_now=False, auto_now_add=False)
    date_outgoing_abj_schedule = models.DateField(auto_now=False, auto_now_add=False)
    filing_receipt = models.CharField(default="default value", max_length=50)
    goods = models.CharField(default="default value", max_length=50)
    incentive_due_clerk = models.IntegerField()
    lawyer_responsible = models.CharField(default="default value", max_length=50)
    month_incoming_schedule = models.CharField(default="default value", max_length=50)
    month_outgoing_schedule = models.CharField(default="default value", max_length=50)
    name_of_client = models.CharField(default="default value", max_length=50)
    name_of_proprietor = models.CharField(default="default value", max_length=50)
    official_fee_ctc = models.CharField(default="default value", max_length=50)
    official_fee_late_renewal_penalty = models.CharField(default="default value", max_length=50)
    official_fee_merger = models.CharField(default="default value", max_length=50)
    official_fee_registered_user = models.CharField(default="default value", max_length=50)
    our_ref_no = models.CharField(default="default value", max_length=50)
    proprietors_address = models.CharField(default="default value", max_length=50)
    quicktellers_fee = models.DecimalField()
    registration_no = models.IntegerField()
    trademark_description = models.CharField(default="default value", max_length=50)

    search_action = models.ForeignKey(SearchAction, on_delete=models.CASCADE, null=True)
    renewal_action = models.ForeignKey(RenewalAction, on_delete=models.CASCADE, null=True)
    registration_action = models.ForeignKey(RegistrationAction, on_delete=models.CASCADE, null=True)
    certificate_procurement_action = models.ForeignKey(CertificateProcurementAction, on_delete=models.CASCADE, null=True)
