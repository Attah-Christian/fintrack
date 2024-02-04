from django import forms
from .models import FormPage



class FormPageForm(forms.ModelForm):
    class Meta:
        model = FormPage
        fields = ('__all__')
