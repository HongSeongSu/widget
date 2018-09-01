from django import forms
from django.urls import reverse_lazy
from .models import Country, Post
from .widgets import CounterTextInput, RateitjsWidget, AutoCompleteSelect, DatePickerWidget

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name']
        widgets = {
            'name': CounterTextInput,
        }


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'country': AutoCompleteSelect(ajax_url=reverse_lazy('country_list')),
            'rating': RateitjsWidget,
            'when': DatePickerWidget,
        }