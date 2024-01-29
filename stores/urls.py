from django.urls import path
from . import views


urlpatterns = [
    path('stores/', views.StoreCreateListView.as_view(), name='stores-create-list'),
    path('stores/<int:pk>/', views.StoreRetrieveUpdateDestroyView.as_view(), name='stores-detail-view'),
    path('stock_movement/', views.StockMovementCreateListView.as_view(), name='stock_movement-create-list'),
    path('stock_movement/<int:pk>/', views.StockMovementCreateListView.as_view(), name='stock_movement-detail-view'),
]
