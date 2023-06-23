from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:word>", views.wiki, name = "wiki"),
    path("wiki/", views.wiki, name = "wikiNoParam"),
    path("newPage", views.newPage, name = "newPage"),
    path("updatePage/<str:title>", views.updatePage, name = "updatePage"),
    path("randomPage", views.randomPage, name="randomPage")
]
