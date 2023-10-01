from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Order


class ShoppingCart(DetailView):
    model = Order
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        user = self.request.user
        if user.is_authenticated:
            user.new_orders = 0
            user.save()  # Zapisz zmiany w bazie danych
        return context