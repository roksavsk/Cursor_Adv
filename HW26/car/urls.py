from django.urls import path

from car.views import CarsListView, DetailCarView, serialized_cars

app_name = 'car'

urlpatterns = [
    path(
        '',
        CarsListView.as_view(),
        name='car_list',
    ),
    path(
        '<slug:car_slug>/',
        DetailCarView.as_view(),
        name='car_detail',
    ),
    path(
        'api/car/json/',
        serialized_cars,
    )
]
