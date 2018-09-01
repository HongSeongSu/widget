from django import forms
from .models import Country, Post
from .widgets import CounterTextInput, RateitjsWidget

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
            "rating": RateitjsWidget,
        }