from django.db import models

# Create your models here.
class PatentParticulars(models.Model):
    pass

class SearchAction(models.Model):
    search_status = models.CharField(default="default value", max_length=50)
    reported_to_client = models.CharField(default="default value", max_length=50)
    date_reported_to_client = models.DateField()
    clerk_searching = models.CharField(default="default value", max_length=)
    pass

class RenewalAction(models.Model):
    patent_registration_no = models.CharField(default="default value", max_length=50)
    invention_description = models.CharField(default="default value", max_length=50)
    patent_start_date = models.DateField()
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