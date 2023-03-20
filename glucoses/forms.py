from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from django import forms
from .models import GlucosesParameters

class GlucosesParametersForm(forms.ModelForm):
    class Meta:
        model = GlucosesParameters
        fields = ['glucose_level','examination_date']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.layout = Layout(
            Fieldset(
                'Add new measurement',
                'glucose_level',
                'examination_date',
            ),
            Submit('submit','Add',css_class="btn btn-success")
        )