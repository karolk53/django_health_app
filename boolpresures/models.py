from datetime import date

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BloodPressureParameters(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    pulse = models.IntegerField()
    examination_date = models.DateField(default=date.today)