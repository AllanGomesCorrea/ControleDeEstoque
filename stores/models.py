from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Store(models.Model):
    name = models.CharField(max_length=150)
    location = models.TextField()

    def __str__(self):
        return self.name

class StockMovement(models.Model):
    TYPE_CHOICES = [
        ('IN', 'In'),
        ('OUT', 'Out'),
    ]

    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type} - {self.product} - {self.quantity} units"
