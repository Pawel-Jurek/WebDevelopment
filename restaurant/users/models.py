from django.db import models

from django.contrib.auth.models import AbstractUser

from orders.models import Order


class User(AbstractUser):
    shopping_cart = models.ManyToManyField(Order, related_name='shoping_cart' )
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.username}: [{self.shoping_cart.count()}]"