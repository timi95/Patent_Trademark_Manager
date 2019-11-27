import datetime
from django.core.validators import URLValidator
from django.db import models

# Create your models here.


class TrademarkParticulars(models.Model):
    pass


class TrademarkProfile(models.Model):
    client_name = models.CharField(default="default client name", max_length=50)
    # trademark_particulars = models.OneToOneField(TrademarkParticulars, on_delete=models.CASCADE)
    # action1_actions = models.OneToMany(to=TrademarkAction1)
    # action2 = models.ForeignKey(TrademarkAction2, on_delete=models.CASCADE, null=True)


class TrademarkAction1(models.Model):
    action_name = models.CharField(default="default action", max_length=50)
    # profile = models.ForeignKey(TrademarkProfile, on_delete=models.CASCADE, null=True)
    pass


class TrademarkAction2(models.Model):
    action_name = models.CharField(default="default action", max_length=50)
    # profile = models.ForeignKey(TrademarkProfile, on_delete=models.CASCADE, null=True)
    pass


class Profile_Actions_Relative(models.Model):
    """docstring for Profile_Actions_Relative.models.Model"""
    profile = models.OneToOneField(TrademarkProfile, on_delete=models.CASCADE, null=True)
    action1 = models.ForeignKey(TrademarkAction1, on_delete=models.CASCADE, null=True)
    action2 = models.ForeignKey(TrademarkAction2, on_delete=models.CASCADE, null=True)
