from datetime import date
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class GlucosesParameters(models.Model):

    class Meta:
        verbose_name = 'Glukoza'
        verbose_name_plural = 'Glukozy'

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    glucose_level = models.IntegerField()
    examination_date = models.DateField(default=date.today)