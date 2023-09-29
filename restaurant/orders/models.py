from django.db import models
from kitchen.models import Dish
from django.conf import settings


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    dishes = models.ManyToManyField(Dish)
    completed = models.BooleanField(default=False)

    
    def __str__(self):
        return f"{self.user.username}: [{self.dishes.name}]"
   