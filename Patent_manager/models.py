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

class Registration(models.Model):
    pass

class ProcurementOfCertificate(models.Model):
    pass

class CTC(models.Model):
    pass

