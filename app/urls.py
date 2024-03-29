from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('customers.urls')),
    path('api/v1/', include('orders.urls')),
    path('api/v1/', include('products.urls')),
    path('api/v1/', include('stores.urls')),
]
