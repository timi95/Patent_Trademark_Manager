from django.db import models

# Create your models here.
class PatentParticulars(models.Model):
    pass

class SearchAction(models.Model):
    search_status = models.CharField(default="default value", max_length=50)
    reported_to_client = models.CharField(default="default value", max_length=50)
    date_reported_to_client = models.DateField()
    clerk_searching = models.CharField(default="default value", max_length=50)
    pass

class RenewalAction(models.Model):
    patent_registration_no = models.CharField(default="default value", max_length=50)
    invention_description = models.CharField(default="default value", max_length=50)
    patent_start_date = models.DateField()
    patent_end_date = models.DateField()
    renewal_instruction_date = models.DateField()
    renewal_instruction_month = models.CharField(default="default value", max_length=50)
    number_of_renewals = models.IntegerField()
    renewal_due_date = models.DateField()
    renewal_due_month = models.CharField(default="default value", max_length=50)
    date_abuja_instructed_renewal = models.DateField()
    clerk_reviewing = models.CharField(default="default value", max_length=50)
    renewal_status =  models.CharField(default="default value", max_length=50)
    date_renew_cert_received = models.DateField()
    next_renewal_due_date = models.DateField()
    next_renewal_due_month = models.CharField(default="default value", max_length=50)
    official_fee_renewal = models.CharField(default="default value", max_length=50)
    renewal_extension_of_time = models.DateTimeField()
    late_renewal_penalty = models.CharField(default="default value", max_length=50)
    pass

class RegistrationAction(models.Model):
    date_registration_instruction_received = models.DateField()
    month_registration_instruction_received = models.DateField()
    clerk_registration = models.CharField(default="default value", max_length=50)
    date_abuja_instructed_for_registration = models.DateField()
    convention_priority_ref_1 = models.CharField(default="default value", max_length=50)
    convention_priority_date_1 = models.CharField(default="default value", max_length=50)
    convention_priority_ref_2 = models.CharField(default="default value", max_length=50)
    convention_priority_date_2 = models.CharField(default="default value", max_length=50)
    convention_priority_ref_3 = models.CharField(default="default value", max_length=50)
    convention_priority_date_3 = models.CharField(default="default value", max_length=50)
    PCT_ref_no = models.CharField(default="default value", max_length=50)
    PCT_filling_date = models.CharField(default="default value", max_length=50)
    filling_deadline = models.CharField(default="default value", max_length=50)
    application_no = models.CharField(default="default value", max_length=50)
    patent_registration_filling_date = models.CharField(default="default value", max_length=50)
    registration_filling_month = models.CharField(default="default value", max_length=50)
    registration_status = models.CharField(default="default value", max_length=50)
    acknowledgement_status = models.CharField(default="default value", max_length=50)
    acceptance_date = models.DateField()
    cert_procurement_date = models.DateField()
    cert_procurment_month = models.CharField(default="default value", max_length=50)
    patent_registration_no = models.CharField(default="default value", max_length=50)
    correspondence_date =  models.DateField()
    date_of_instruction = models.DateField()
    clients_contact_person = models.CharField(default="default value", max_length=50)
    official_fee_registration = models.CharField(default="default value", max_length=50)
    pass

class ProcurementOfCertificateAction(models.Model):
    date_procurement_instructed = models.DateField()
    application_no = models.CharField(default="default value", max_length=50)
    invention_description = models.CharField(default="default value", max_length=50)
    clerk_procuring = models.CharField(default="default value", max_length=50)
    date_procurement_instructed = models.CharField(default="default value", max_length=50)
    month_clerk_instructed = models.CharField(default="default value", max_length=50)
    procurement_status = models.CharField(default="default value", max_length=50)
    date_cert_procured = models.CharField(default="default value", max_length=50)
    patent_regtn_no = models.CharField(default="default value", max_length=50)
    date_cert_procurement_due = models.CharField(default="default value", max_length=50)
    month_cert_procurement_due = models.CharField(default="default value", max_length=50)
    pass

class CTCAction(models.Model):
    application_no = models.CharField(default="default value", max_length=50)
    patent_registration_no = models.CharField(default="default value", max_length=50)
    ctc_required = models.CharField(default="default value", max_length=50)
    date_applied_for_ctc = models.CharField(default="default value", max_length=50)
    ctc_procurement_status = models.CharField(default="default value", max_length=50)
    clerk_responsible = models.CharField(default="default value", max_length=50)
    pass

class ChangeOfNameAction(models.Model):
    change_of_name_instruction_date = models.DateField()
    change_of_name_instruction_month = models.CharField(default="default value", max_length=50)
    new_name_of_patentee = models.CharField(default="default value", max_length=50)
    clerk_for_change_of_name = models.CharField(default="default value", max_length=50)
    status_of_change_of_name = models.CharField(default="default value", max_length=50)
    date_received_change_of_name_certificate  = models.DateField()
    pass

class ChangeOfAddressAction(models.Model):
    change_of_address_instruction_date = models.DateField()
    change_of_address_instruction_month = models.CharField(default="default value", max_length=50)
    new_address_of_patentee = models.CharField(default="default value", max_length=50)
    clerk_of_change_of_address = models.CharField(default="default value", max_length=50)
    status_change_of_address = models.CharField(default="default value", max_length=50)
    date_received_change_of_address_certificate = models.CharField(default="default value", max_length=50)
    pass

class AssignmentMergerAction(object):
    assignment_instruction_date = models.DateField()
    assignment_instruction_month = models.CharField(default="default value", max_length=50)
    date_abuja_instructed_assignment = models.CharField(default="default value", max_length=50)
    clerk_assignment = models.CharField(default="default value", max_length=50)
    status_assignment_registrations = models.CharField(default="default value", max_length=50)
    assignor = models.CharField(default="default value", max_length=50)
    assignor_address = models.CharField(default="default value", max_length=50)
    assignee = models.CharField(default="default value", max_length=50)
    assignee_address = models.CharField(default="default value", max_length=50)
    date_assignment_certificate_received = models.CharField(default="default value", max_length=50)
    pass

class AmendmentAction(models.Model):
    date_ammendment_instruction_received = models.DateField()
    nature_of_amendment = models.CharField(default="default value", max_length=50)
    amending_clerk = models.CharField(default="default value", max_length=50)
    date_amending_clerk_instructed = models.CharField(default="default value", max_length=50)
    status_of_amendment = models.CharField(default="default value", max_length=50)
    date_amendment_received = models.DateField()
    pass

class PatentParticlars(models.Model):
    our_reference_number = models.CharField(default="default value", max_length=50)
    client_id = models.CharField(default="default value", max_length=50)
    clients_reference_number = models.CharField(default="default value", max_length=50)
    curent_instruction = models.CharField(default="default value", max_length=50)
    date_of_instruction = models.DateField()
    name_of_client = models.CharField(default="default value", max_length=50)
    clients_address = models.CharField(default="default value", max_length=50)
    clients_contact_person = models.CharField(default="default value", max_length=50)
    name_of_patentee = models.CharField(default="default value", max_length=50)
    patentees_address = models.CharField(default="default value", max_length=50)
    date_instruction_received = models.DateField()
    lawyer_responsible = models.CharField(default="default value", max_length=50)
    invention_description = models.CharField(default="default value", max_length=50)
    patent_registration_number = models.CharField(default="default value", max_length=50)
    convention_country = models.CharField(default="default value", max_length=50)
    current_status = models.CharField(default="default value", max_length=50)
    date_certificate_procurement_due = models.DateField(default="default value", max_length=50)
    month_certificate_procurement_due = models.CharField(default="default value", max_length=50)
    date_outgoing_abuja_schedule = models.DateField()
    date_incoming_abuja_schedule = models.DateField()
    date_completed_job_received =  models.DateField()
    official_fee =  models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    facilitation = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    incentive_due_clerk = models.CharField(default="default value", max_length=50)
    clerk_responsible = models.CharField(default="default value", max_length=50)
    month_incoming_abuja_schedule = models.CharField(default="default value", max_length=50)
    month_outgoing_abuja_schedule = models.CharField(default="default value", max_length=50)
    filing_receipt_status = models.CharField(default="default value", max_length=50)
    applicable_service_charge = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    quickteller_fee = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    pass
#