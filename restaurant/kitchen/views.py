from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.contrib.auth.decorators import login_required

from .models import Dish
from users.models import User
from orders.models import OrderItem

# Create your views here.

class MainPageView(TemplateView):
    template_name = 'index.html'
    
index_view = MainPageView.as_view()


class DishesListView(ListView):
    model = Dish


@login_required
def add_to_cart(request, dish_id):
    print('\njesteśmy w funkcji Dodawania do koszyka')
    if request.method == "PUT":
        try:
            dish = Dish.objects.get(pk=dish_id)
            user = User.objects.get(username=request.user.username)
            user.new_orders += 1

            order = user.get_or_create_order()

            order_item, created = OrderItem.objects.get_or_create(order=order, dish=dish)

            if not created:
                order_item.quantity += 1
                order_item.save()

            user.save()

            return JsonResponse({
                "new_items": user.new_orders
            }, status=200)
        except Exception as e: 
            return JsonResponse({
                "error": str(e)
            }, status=401 )

    return JsonResponse({
        "error": "PUT request required."
    }, status=400)