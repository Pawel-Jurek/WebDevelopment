from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    price_per_kg = models.FloatField(null=True, blank=True)
    price_per_item = models.FloatField(null=True, blank=True)
    pieced = models.BooleanField()

    def __str__(self):
        return self.name 

class Dish(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='imgs/', blank=True, null=True)
    
    def calculate_price(self):
        total_price = 0.0

        for ingredient in self.ingredients.all():
            if ingredient.product.pieced:
                total_price += ingredient.amount * ingredient.product.price_per_item
            else:
                total_price += (ingredient.amount / 1000) * ingredient.product.price_per_kg
        
        return total_price

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="ingredients")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)

    def __str__(self):
        if self.product.pieced:
            return f'{self.product.name}: {self.amount} szt.'
        else:
            return f'{self.product.name}: {self.amount} g'




