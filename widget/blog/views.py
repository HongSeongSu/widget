from django.http import JsonResponse
from .models import Country


def country_list(request):
    qs = Country.objects.all()
    q = request.GET.get('q')
    qs = qs.filter(name__icontains=q)
    results = [{'id': country.id, 'text': country.name} for country in qs]
    return JsonResponse({
        'results': results,
    })
