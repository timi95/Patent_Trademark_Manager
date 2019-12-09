import datetime
from django.core.validators import URLValidator
from django.db import models

# Create your models here.


class AmendementAction(models.Model):
    ammendement_instruction_date = models.CharField(max_length=50)
    date_ammendement_instruction_received = models.CharField(max_length=50)
    nature_of_amendement = models.CharField(max_length=50)
    date_amending_clerk_instructed = models.CharField(max_length=50)
    status_of_amendement = models.CharField(max_length=50)
    date_amendement_received = models.CharField(max_length=50)



class AssignmentMergerAction(models.Model):
    assignment_instruction_date = models.CharField(max_length=50)
    assignment_instruction_month = models.CharField(max_length=50)
    assignee = models.CharField(max_length=50)
    assignee_address = models.CharField(max_length=50)
    assignor = models.CharField(max_length=50)
    assignor_address = models.CharField(max_length=50)
    clerk_assigning = models.CharField(max_length=50)
    date_abj_instructed_assignment = models.CharField(max_length=50)
    date_assignment_certificate_received = models.CharField(max_length=50)
    date_facillitation_assignment_cert_sent = models.CharField(max_length=50)
    date_facillitation_assignment_cert_sent_sent = models.CharField(max_length=50)
    official_fee_assignment = models.CharField(max_length=50)
    status_assignment_registration = models.CharField(max_length=50)


class CertificateProcurementAction(models.Model):
    date_procurement_instructed = models.CharField(max_length=50)
    application_no = models.CharField(max_length=50)
    trademark_description = models.CharField(max_length=50)
    journal_no = models.CharField(max_length=50)
    journal_vol = models.CharField(max_length=50)
    journal_date = models.CharField(max_length=50)
    journal_page = models.CharField(max_length=50)
    date_clerk_instructed_to_procure = models.CharField(max_length=50)
    cert_procurement_status = models.CharField(max_length=50)
    date_registration_certificate = models.CharField(max_length=50)
    registration_no = models.CharField(max_length=50)
    official_fee_certificate_issuance = models.CharField(max_length=50)


class ChangeName_AddressAction(models.Model):
    change_of_address_instruction_date = models.CharField(max_length=50)
    change_of_name_instruction_date = models.CharField(max_length=50)
    date_received_change_of_address_certificate = models.CharField(max_length=50)
    date_received_change_of_name_certificate = models.CharField(max_length=50)
    new_address_of_pptr = models.CharField(max_length=50)
    new_name_of_pptr = models.CharField(max_length=50)
    official_fee_change_name = models.CharField(max_length=50)
    official_fee_change_address = models.CharField(max_length=50)
    status_change_of_name = models.CharField(max_length=50)
    status_change_of_address = models.CharField(max_length=50)


class ReclassificationAction(models.Model):
    date_reclassification_instruction = models.CharField(max_length=50)
    date_abj_instructed_reclassify = models.CharField(max_length=50)
    reclassification_status = models.CharField(max_length=50)
    date_publication_of_reclassification = models.CharField(max_length=50)
    journal_pg_reclassification = models.CharField(max_length=50)


class RegistrationAction(models.Model):
    acceptance_date = models.CharField(max_length=50)
    acceptance_facilitation_sent = models.CharField(max_length=50)
    acknowledgement_date = models.CharField(max_length=50)
    acknowledgement_facilitation_sent = models.CharField(max_length=50)
    application_no = models.CharField(max_length=50)
    trademark_class = models.CharField(max_length=50)
    clerk_registering = models.CharField(max_length=50)
    colour_limitation = models.CharField(max_length=50)
    date_acceptance_facilitation_sent = models.CharField(max_length=50)
    date_acknowledgement_facilitation_sent = models.CharField(max_length=50)
    date_of_registration_instruction = models.CharField(max_length=50)
    date_of_registration_instruction_received = models.CharField(max_length=50)
    date_registration_cert_facilitation_sent = models.CharField(max_length=50)
    date_sent_for_publication = models.CharField(max_length=50)
    date_abj_instructed_for_registration = models.CharField(max_length=50)
    goods = models.CharField(max_length=50)
    journal_date = models.CharField(max_length=50)
    journal_no = models.CharField(max_length=50)
    journal_page = models.CharField(max_length=50)
    journal_vol = models.CharField(max_length=50)
    official_fee_registration = models.CharField(max_length=50)
    publication = models.CharField(max_length=50)
    registration_status = models.CharField(max_length=50)
    registration_filing_month = models.CharField(max_length=50)
    registration_no = models.CharField(max_length=50)
    registraion_cert_facilitation_sent = models.CharField(max_length=50)
    tm_registration_filing_date = models.CharField(max_length=50)


class RenewalAction(models.Model):
    date_renewal_cert_facilitation_sent = models.CharField(max_length=50)
    dt_abj_instructed_renewal = models.CharField(max_length=50)
    dt_renew_cert_received = models.CharField(max_length=50)
    next_renewal_due_date = models.CharField(max_length=50)
    next_renewal_due_month = models.CharField(max_length=50)
    official_fee_renewal = models.CharField(max_length=50)
    renewal_cert_facilitation_sent = models.CharField(max_length=50)
    renewal_due_date = models.CharField(max_length=50)
    renewal_due_month = models.CharField(max_length=50)
    renewal_instruction_date = models.CharField(max_length=50)
    renewal_instruction_month = models.CharField(max_length=50)
    renewal_status = models.CharField(max_length=50)


class SearchAction(models.Model):
    clerk_searching = models.CharField(max_length=50)
    conflicting_mark = models.CharField(max_length=50)
    date_of_search_report = models.CharField(max_length=50)
    date_reported_to_client = models.CharField(max_length=50)
    official_search_fee = models.CharField(max_length=50)
    reported_to_client = models.CharField(max_length=50)
    search_instruction_date = models.CharField(max_length=50)
    search_status = models.CharField(max_length=50)
    search_type =  models.CharField(max_length=50)

class TrademarkProfile(models.Model):
    client_name = models.CharField(default="default client name", max_length=50)
    client_ref_no = models.CharField(max_length=50)
    correspondence_date = models.CharField(max_length=50)
    current_instruction = models.CharField(max_length=50)
    current_status = models.CharField(max_length=50)
    date_instruction_received = models.CharField(max_length=50)
    date_current_instruction = models.CharField(max_length=50)
    date_completed_job_received = models.CharField(max_length=50)
    date_incoming_abj_schedule = models.CharField(max_length=50)
    date_outgoing_abj_schedule = models.CharField(max_length=50)
    filing_receipt = models.CharField(max_length=50)
    goods = models.CharField(max_length=50)
    incentive_due_clerk = models.CharField(max_length=50)
    lawyer_responsible = models.CharField(max_length=50)
    month_incoming_schedule = models.CharField(max_length=50)
    month_outgoing_schedule = models.CharField(max_length=50)
    name_of_client = models.CharField(max_length=50)
    name_of_proprietor = models.CharField(max_length=50)
    official_fee_ctc = models.CharField(max_length=50)
    official_fee_late_renewal_penalty = models.CharField(max_length=50)
    official_fee_merger = models.CharField(max_length=50)
    official_fee_registered_user = models.CharField(max_length=50)
    our_ref_no = models.CharField(max_length=50)
    proprietors_address = models.CharField(max_length=50)
    quicktellers_fee = models.CharField(max_length=50)
    registration_no = models.CharField(max_length=50)
    trademark_description = models.CharField(max_length=50)

    search_action = models.ForeignKey(SearchAction, on_delete=models.CASCADE, null=True)
    renewal_action = models.ForeignKey(RenewalAction, on_delete=models.CASCADE, null=True)
    registration_action = models.ForeignKey(RegistrationAction, on_delete=models.CASCADE, null=True)
    certificate_procurement_action = models.ForeignKey(CertificateProcurementAction, on_delete=models.CASCADE, null=True)
