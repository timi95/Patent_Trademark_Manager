from django.db import models

# Create your models here.
class Remider(models.Model):
    date_field = models.DateTimeField()
    details = models.TextField()
    pass