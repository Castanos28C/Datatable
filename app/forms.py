from django import forms
from django.forms import ModelForm
from .models import Programmer

class ProgrammerForm(ModelForm):
    class Meta:
        model = Programmer
        fields = ['name', 'country', 'birthday','score']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'birthday': forms.DateInput(attrs={'class': 'form-control datetimepicker-input','data-target': '#datetimepicker1'}),
            'score': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }
