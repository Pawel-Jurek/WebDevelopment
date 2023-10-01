from django.urls import path
from .views import ShoppingCart

app_name = 'orders'

urlpatterns = [
    path('cart/<int:pk>', ShoppingCart.as_view() , name="cart_detail"),
]