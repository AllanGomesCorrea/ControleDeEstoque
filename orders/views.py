from rest_framework import generics
from orders.models import Order, OrderItem
from orders.serializers import OrderSerializer, OrderItemSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from products.models import Product


class OrderCreateListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemCreateListView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
    def perform_create(self, serializer):
        product_id = int(self.request.data.get('product'))
        quantity = int(self.request.data.get('quantity'))
        subtotal = self.request.data.get('subtotal')
        order_id = int(self.request.data.get('order'))
        product = Product.objects.get(pk=product_id)
        order = Order.objects.get(pk=order_id)
        
        if product.stock_quantity < quantity :
            raise ValidationError("Quantidade maior que o estoque. Ordem de item cancelada.")
        
        order_item = OrderItem.objects.create(order= order, product= product, quantity= quantity, subtotal= subtotal)
        serializer.instance = order_item
        product.stock_quantity = product.stock_quantity - quantity
        product.save()
    
    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({"ERROR": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        return response


class OrderItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer