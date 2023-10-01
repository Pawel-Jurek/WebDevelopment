from django.db import models

from django.contrib.auth.models import AbstractUser

from orders.models import Order


class User(AbstractUser):
    orders = models.ManyToManyField(Order, related_name='orders')
    new_orders = models.IntegerField(default=0)
    phone = models.CharField(max_length=15)  

    def __str__(self):
        active_order = self.orders.get(active=True)
        return f"{self.username}: [{active_order.dishes.count()}]"
    
    def has_active_order(self):
        if self.orders and self.orders.filter(active=True).count() > 0:
            return True
        else:
            return False
    

