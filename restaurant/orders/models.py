from django.db import models
from kitchen.models import Dish


class Order(models.Model):
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pk}. {self.orderItems}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orderItems")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Dish: {self.dish.name}, Quantity: {self.quantity}"