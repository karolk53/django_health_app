from django.contrib import admin
from .models import BloodPressureParameters
# Register your models here.

@admin.register(BloodPressureParameters)
class BoolPressureParametersAdmin(admin.ModelAdmin):
    list_display = ['systolic','diastolic']