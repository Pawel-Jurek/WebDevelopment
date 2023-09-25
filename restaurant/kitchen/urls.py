from django.urls import path
from .views import DishesListView 

urlpatterns = [
    path('', DishesListView.as_view(), name='dishes'),
]
