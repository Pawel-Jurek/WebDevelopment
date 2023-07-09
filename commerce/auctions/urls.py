from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:category_id>", views.index, name="indexWithCategory"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("addListing", views.addListing, name="addListing"),
    path("details/<int:product_id>", views.product, name="product"),
    path('add_to_watchlist/<str:auction_id>', views.add_to_watchlist, name='add_to_watchlist'),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watchlist/<int:category_id>", views.watchlist, name="watchlistWithCateogry"),
    path("<str:user>/offers/<int:category_id>", views.user_offers, name="user_offers_withCategory"),
    path("<str:user>/offers", views.user_offers, name="user_offers"),
    path("close_listing/<int:listing_id>", views.close_listing, name="close_listing")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)