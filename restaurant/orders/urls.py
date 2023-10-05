from django.urls import path
from .views import ShoppingCart, update_dish

app_name = 'orders'

urlpatterns = [
    path('cart/<int:pk>', ShoppingCart.as_view() , name="cart_detail"),
    path("cart/update_dish/<int:orderId>/<int:dishId>/<int:quantity>", update_dish, name="update_dish"),
]