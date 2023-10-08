from django.db import models

from django.contrib.auth.models import AbstractUser

from orders.models import Order


class User(AbstractUser):
    orders = models.ManyToManyField(Order, related_name='user')
    new_orders = models.IntegerField(default=0)
    phone = models.CharField(max_length=15) 
    is_owner = models.BooleanField(default=False)

    def __str__(self):
        active_order = self.orders.get(active=True)
        return f"{self.username}: [{active_order.orderItems.all().count()}]"
        
    def get_or_create_order(self):
        if not self.orders or self.orders.filter(active=True).count() == 0:
            newOrder = Order.objects.create()
            self.orders.add(newOrder)
        
        return self.orders.get(active=True)
    

