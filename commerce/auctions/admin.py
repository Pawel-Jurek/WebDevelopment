from django.contrib import admin

from .models import Category, Auction, Comment, User, Bid, WatchList
# Register your models here.

admin.site.register(Category)
admin.site.register(Auction)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Bid)
admin.site.register(WatchList)