from django.contrib import admin
from .models import GlucosesParameters
# Register your models here.


@admin.register(GlucosesParameters)
class GlucosesParametersAdmin(admin.ModelAdmin):
    list_display = ['glucose_level']

