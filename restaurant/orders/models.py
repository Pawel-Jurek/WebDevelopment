from django.db import models
from kitchen.models import Dish


class Order(models.Model):
    active = models.BooleanField(default=True)

    def calculate_total_price(self):
        return f'{sum(item.quantity * item.dish.price for item in self.orderItems.all()):.2f}'
    
    def calculate_costs(self):
        return f'{sum(item.quantity * item.dish.calculate_price() for item in self.orderItems.all()):.2f}'
    
    def calculate_profit(self):
        return f'{float(self.calculate_total_price()) - float(self.calculate_costs()):.2f}'

    def __str__(self):
        return f"{self.pk}. {self.orderItems.all()}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orderItems")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Dish: {self.dish.name}, Quantity: {self.quantity}"