from rest_framework import serializers
from stores.models import StockMovement, Store


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = '__all__'

class StockMovementSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockMovement
        fields = '__all__'
        