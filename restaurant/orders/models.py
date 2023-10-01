from django.db import models
from kitchen.models import Dish


class Order(models.Model):
    dishes = models.ManyToManyField(Dish)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"dishes: [{self.dishes.name}]"
   

   
    