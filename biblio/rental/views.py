from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Rental

class BookRentView(CreateView):
    model = Rental
    fields = ['who', 'what']
    success_url = '/'
