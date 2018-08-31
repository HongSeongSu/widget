from django import forms
from .models import Country, Post
from .widgets import CounterTextInput

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name']
        widgets = {
            'name': CounterTextInput,
        }
