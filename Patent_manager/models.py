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
    pass

class AssignmentMergerAction(object):
    pass

class AmendmentAction(models.Model):
    pass

class PatentParticlars(models.Model):
    pass