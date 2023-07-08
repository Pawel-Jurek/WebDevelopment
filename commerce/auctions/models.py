from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
import os


def get_default_image_path():
    return 'images/auctions/default.jpg'

class User(AbstractUser): 
    def __str__(self):
        return f"{self.username}"


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Auction(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=300)
    current_bid = models.DecimalField(max_digits=15, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/auctions/", default=get_default_image_path)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="auctionCategory")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default = 1, related_name="auctionAutor")
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.title} created by: {self.author}"
    

class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auctionObserver")
    offer = models.ManyToManyField(Auction, related_name="watchlists")

    def __str__(self):
       return f"{self.user}: {', '.join(str(offer) for offer in self.offer.all())}"

    

class Bid(models.Model):
    value = models.DecimalField(max_digits=15, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid_owner")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="auction_bid")

    def __str__(self):
        return f"user:{self.user} value:{self.value} auction:{self.auction}"

class Comment(models.Model):
    text = models.CharField(max_length=254)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_owner")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="auction_comment")

    def __str__(self):
        return f"user:{self.user} text:{self.text[0:30]} auction:{self.auction}"