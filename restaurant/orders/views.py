from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from kitchen.views import MainPageView, add_to_cart

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
    

class OrdersSummary(ListView):
    model = Order   
    def get_queryset(self):
        return Order.objects.filter(active=False)
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            total_income = sum(float(order.calculate_profit()) for order in self.get_queryset())

            context['total_income'] = f'{total_income:.2f}'

            return context


@login_required
def update_dish(request, orderId, dishId, quantity):
    if request.method == 'PUT':
        try:
            order_item = OrderItem.objects.get(order=orderId, dish=dishId)
            if(quantity == 0):
                order_item.delete()
            else:            
                order_item.quantity = quantity
                order_item.save()

            return JsonResponse({
                "status": 'success'
            })
        except OrderItem.DoesNotExist:
            add_to_cart(dishId)
        except Exception as e: 
            return JsonResponse({
                "status": f'error: {str(e)}'
            })

    return JsonResponse({
        "status": "Error: PUT request required."
    }, status=400)


@login_required
def confirm_order(request, order_id):
    if request.method == 'PUT':
        try:
            order = Order.objects.get(pk=order_id)
            order.active = False
            order.save()

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
        

