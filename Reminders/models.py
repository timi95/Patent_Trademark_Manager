from django.db import models

# Create your models here.
class Reminder(models.Model):
    title = models.CharField(default="default value", max_length=50)
    reminder_detail = models.TextField()
    reminder_date = models.DateTimeField()
    manager_type = models.CharField(default="default value", max_length=50)
    document_type = models.CharField(default="default value", max_length=50)
    document_id = models.CharField(default="default value", max_length=50)
    matured = models.BooleanField(default=False)