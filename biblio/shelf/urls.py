from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorListView.as_view(), name="authors"),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name="author_detail"),
    path('books/', views.BookListView.as_view(), name = "books"),
    path('book/<int:pk>', views.BookDetailView.as_view(), name = "book_datail"),

]