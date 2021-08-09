from django.urls import path

from order.views import OrderListView, DetailOrderView, serialized_orders

app_name = 'order'

urlpatterns = [
    path(
        '',
        OrderListView.as_view(),
        name='order_list',
    ),
    path(
        '<int:order_pk>/',
        DetailOrderView.as_view(),
        name='order_detail',
    ),
    path(
        'api/order/json/',
        serialized_orders,
    )
]