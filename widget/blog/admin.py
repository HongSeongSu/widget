from django.contrib import admin
from .models import Country, Post
from .forms import CountryForm, PostForm


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    form = CountryForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
