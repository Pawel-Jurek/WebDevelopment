from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:pk>', views.WeatherAppUserDetailView.as_view(), name="user_profile"),
]