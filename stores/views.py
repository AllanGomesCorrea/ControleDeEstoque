from rest_framework import generics
from stores.models import Store, StockMovement
from stores.serializers import StoreSerializer, StockMovementSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from products.models import Product
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class StoreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class StoreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class StockMovementCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer
    
    def perform_create(self, serializer):
        type = self.request.data.get('type')
        product_id = self.request.data.get('product')
        quantity = int(self.request.data.get('quantity'))
        
        if type == 'IN':
           product = Product.objects.get(pk=product_id)
           product.stock_quantity = product.stock_quantity + quantity
           
        if type == 'OUT':
           product = Product.objects.get(pk=product_id)
           
           if quantity > product.stock_quantity:
               raise ValidationError("Quantidade maior que o estoque. Movimentação cancelada.")
           
           product.stock_quantity = product.stock_quantity - quantity
           
        product.save()
        
        
    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({"ERROR": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        return response


class StockMovementRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer