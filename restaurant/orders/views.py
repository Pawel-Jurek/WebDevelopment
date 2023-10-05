from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from kitchen.models import Dish

# Create your views here.
from .models import Order, OrderItem


class ShoppingCart(DetailView):
    model = Order
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        user = self.request.user
        if user.is_authenticated:
            user.new_orders = 0
            user.save()
        return context
    

@login_required
def update_dish(request, orderId, dishId, quantity):
    if request.method == 'PUT':
        try:
            order_item = OrderItem.objects.get(order=orderId, dish=dishId)
            order_item.quantity = quantity
            order_item.save()

            return JsonResponse({
                "status": 'success'
            })
        except Exception as e: 
            return JsonResponse({
                "status": f'error: {str(e)}'
            })

    return JsonResponse({
        "status": "Error: PUT request required."
    }, status=400)