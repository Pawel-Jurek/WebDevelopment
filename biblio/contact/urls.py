from django.urls import path

from contact import views

urlpatterns = [
    path("", views.MessageAddView.as_view(), name="message"),
]