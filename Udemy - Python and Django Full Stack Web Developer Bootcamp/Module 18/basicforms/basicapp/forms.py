from typing import Text
from django import forms
from django.forms.fields import EmailField
from django.core import validators



class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        v_mail = all_clean_data['verify_email']

        if v_mail != email:
            raise forms.ValidationError("Emails don't match")
        return