from django.shortcuts import render
from django.views.generic import DetailView
from .models import WeatherAppUser

# Create your views here.
class WeatherAppUserDetailView(DetailView):
    model = WeatherAppUser