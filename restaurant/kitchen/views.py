from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Dish

# Create your views here.

class MainPageView(TemplateView):
    template_name = 'index.html'
    
index_view = MainPageView.as_view()


class DishesListView(ListView):
    model = Dish