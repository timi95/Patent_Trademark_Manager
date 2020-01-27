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
    pass

class ProcurementOfCertificateAction(models.Model):
    pass

class CTCAction(models.Model):
    pass

class ChangeOfNameAction(models.Model):
    pass

class ChangeOfAddressAction(models.Model):
    pass

class AssignmentMergerAction(object):
    pass

class AmendmentAction(models.Model):
    pass

class PatentParticlars(models.Model):
    pass