from django.views.generic import CreateView

from django.http import JsonResponse
from .models import Country, Post
from .forms import PostForm

post_new = CreateView.as_view(model=Post, form_class=PostForm)


def country_list(request):
    qs = Country.objects.all()
    q = request.GET.get('q')
    qs = qs.filter(name__icontains=q)
    results = [{'id': country.id, 'text': country.name} for country in qs]
    return JsonResponse({
        'results': results,
    })
