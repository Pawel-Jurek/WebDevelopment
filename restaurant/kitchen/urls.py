from django.urls import path
from .views import DishesListView, add_to_cart

app_name = 'kitchen'

urlpatterns = [
    path('', DishesListView.as_view(), name='dishes'),
    path('category/<str:category>/', DishesListView.as_view(), name='dishes_category'),
    path('add_to_cart/<int:dish_id>', add_to_cart, name="add_to_cart"),
]
