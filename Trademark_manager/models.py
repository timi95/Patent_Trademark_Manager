import datetime
from django.core.validators import URLValidator
from django.db import models

# Create your models here.
class TrademarkAction1(models.Model):
    pass


class TrademarkAction2(models.Model):
    pass


class TrademarkParticulars(models.Model):
    pass

class TrademarkProfile(models.Model):
    client_name = models.CharField(default="default client name", max_length=50)
    trademark_particulars = models.OneToOneField(TrademarkParticulars, on_delete=models.CASCADE)
    instruction_set =  models.ForeignKey(TrademarkAction1 , on_delete=models.CASCADE),

    # instruction_set = models.ForeignKey(TrademarkAction1, TrademarkAction2, on_delete=models.CASCADE)
