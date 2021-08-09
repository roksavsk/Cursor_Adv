from django.urls import path

from dealer.views import DealerListView, DetailDealerView, serialized_dealers

app_name = 'dealer'

urlpatterns = [
    path(
        '',
        DealerListView.as_view(),
        name='dealer_list',
    ),
    path(
        '<int:dealer_pk>/',
        DetailDealerView.as_view(),
        name='dealer_detail',
    ),
    path(
        'api/dealer/json/',
        serialized_dealers,
    )
]