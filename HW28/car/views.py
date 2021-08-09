from django.core import serializers
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from car.models import Car


class CarsListView(ListView):
    model = Car.objects.all()
    context_object_name = 'cars'
    template_name = 'car/list.html'

    def get_queryset(self):
        return Car.objects.all()


class DetailCarView(DetailView):
    model = Car
    context_object_name = 'cars'
    slug_url_kwarg = 'car_slug'
    template_name = 'car/detail.html'


def serialized_cars(request):
    data = serializers.serialize('json', Car.objects.all())
    return HttpResponse(request.method + '<br>' + data)
