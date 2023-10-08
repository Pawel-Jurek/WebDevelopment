from django.urls import path
from .views import ShoppingCart, update_dish, OrdersSummary, confirm_order

app_name = 'orders'

urlpatterns = [
    path('cart/<int:pk>', ShoppingCart.as_view() , name="cart_detail"),
    path("cart/update_dish/<int:orderId>/<int:dishId>/<int:quantity>", update_dish, name="update_dish"),
    path('summary', OrdersSummary.as_view(), name="ordersSummary"),
    path('confirm_order/<int:order_id>', confirm_order, name="confirm_order"),
]