from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import BloodPressureParameters

class BloodPressureParametersForm(forms.ModelForm):

    class Meta:
        model = BloodPressureParameters
        fields = ['systolic','diastolic','pulse','examination_date']

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit','Add',css_class="btn btn-success"))