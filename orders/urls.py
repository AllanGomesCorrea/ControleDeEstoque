from django.urls import path
from . import views


urlpatterns = [
    path('orders/', views.OrderCreateListView.as_view(), name='order-create-list'),
    path('orders/<int:pk>/', views.OrderRetrieveUpdateDestroyView.as_view(), name='order-detail-view'),
    path('orders_item/', views.OrderItemCreateListView.as_view(), name='order_item-create-list'),
    path('orders_item/<int:pk>/', views.OrderItemRetrieveUpdateDestroyView.as_view(), name='order_item-detail-view'),
]
