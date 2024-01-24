from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.ProductCreateListView.as_view(), name='products-create-list'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='products-detail-view'),
    path('category/', views.CategoryCreateListView.as_view(), name='category-create-list'),
    path('category/<int:pk>/', views.CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail-view'),
]
