from django.contrib import admin

from .models import Dish, Ingredient, Product

# Register your models here.

class DishAdmin(admin.ModelAdmin):
    search_fields = ['name']

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']



admin.site.register(Dish, DishAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Ingredient)