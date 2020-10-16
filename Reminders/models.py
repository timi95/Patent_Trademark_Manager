from django.db import models

# Create your models here.
class Remider(models.Model):
    title = models.CharField()
    reminder_detail = models.TextField()
    reminder_date = models.DateTimeField()
    manager_type = models.CharField()
    document_type = models.CharField()
    document_id = models.CharField()
