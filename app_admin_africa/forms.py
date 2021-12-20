from django import forms
from django.forms import fields, widgets
from django.forms.models import ModelForm
from .models import Country, Admin


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['name','lastname','email','mobile','country']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
            'lastname': forms.TextInput(attrs={'class':'form-control', 'id':'lastnameid'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'id':'emailid'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control', 'id':'mobileid'}),
            'country': forms.Select(attrs={'class':'form-control', 'id':'countryeid'})

        }
