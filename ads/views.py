import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Ad


def main_view(request):
    return JsonResponse({'status': 'OK'})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request):
        all_category = Category.objects.all()
        return JsonResponse([{'id': category.id, 'name': category.name} for category in all_category], safe=False)

    def post(self, request):
        data = json.loads(request.body)
        category = Category.objects.create(name=data.get('name'))
        return JsonResponse({'id': category.id, 'name': category.name})


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):
    def get(self, request):
        all_ad = Ad.objects.all()
        return JsonResponse([{'id': ad.id,
                              'name': ad.name,
                              'author': ad.author,
                              'price': ad.price,
                              'description': ad.description,
                              'address': ad.address,
                              'is_published': ad.is_published
                              } for ad in all_ad], safe=False)

    def post(self, request):
        data = json.loads(request.body)
        ad = Ad.objects.create(**data)
        return JsonResponse({'id': ad.id,
                             'name': ad.name,
                             'author': ad.author,
                             'price': ad.price,
                             'description': ad.description,
                             'address': ad.address,
                             'is_published': ad.is_published
                             })


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({'id': category.id, 'name': category.name})


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({'id': ad.id,
                             'name': ad.name,
                             'author': ad.author,
                             'price': ad.price,
                             'description': ad.description,
                             'address': ad.address,
                             'is_published': ad.is_published
                             })
