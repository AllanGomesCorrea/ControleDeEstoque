from django.urls import path
from . import views


urlpatterns = [
    path('customers/', views.CustomerCreateListView.as_view(), name='customer-create-list'),
    path('customers/<int:pk>/', views.CustomerRetrieveUpdateDestroyView.as_view(), name='customer-detail-view'),
]
