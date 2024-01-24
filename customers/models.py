from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
