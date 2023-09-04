from django.contrib import admin
from .models import Author, Publisher, Book, BookItem, BookCategory, BookEdition


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name']
    ordering = ['last_name']


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']


class PublisherAdmin(admin.ModelAdmin):
    search_fields= ['name']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)

admin.site.register([BookItem, BookCategory, BookEdition])