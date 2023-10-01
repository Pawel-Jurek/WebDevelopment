from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.decorators import login_required

from .models import Dish
from users.models import User
from orders.models import Order

# Create your views here.

class MainPageView(TemplateView):
    template_name = 'index.html'
    
index_view = MainPageView.as_view()


class DishesListView(ListView):
    model = Dish


@login_required
def add_to_cart(request, dish_id):
    if request.method == "PUT":
        try:
            dish = Dish.objects.get(pk=dish_id)
            user = User.objects.get(username=request.user.username)
            user.new_orders += 1

            if user.has_active_order():
                order = user.orders.get(is_active=True)
            else:
                order = Order.objects.create()
                user.orders.add(order)
    
            order.dishes.add(dish)
            order.save()
            user.save()

            return JsonResponse({
                "new_items": user.new_orders
            })
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            })

    return JsonResponse({
        "error": "PUT request required."
    }, status=400)