from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("get_city_suggestions/<str:input>", views.get_city_suggestions)
]