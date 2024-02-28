from django.contrib import admin
from stores.models import Store, StockMovement


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('type', 'quantity', 'date', 'store', 'user')