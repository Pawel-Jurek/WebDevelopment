from django import forms
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q


from .models import User, Comment, Bid, Auction, WatchList, Category
from decimal import Decimal


class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['title', 'description', 'current_bid', 'image', 'category']
        labels = {'current_bid': 'Starting bid'}

class WatchlistButton(forms.Form):
    pass



def index(request, category_id = 0):
    clicked = []
    categories = Category.objects.all()
    if category_id:
        listings = Auction.objects.filter(category_id=category_id)
    else:
        listings = Auction.objects.all()
    if request.user.is_authenticated:
        user = request.user
        watchlist, created = WatchList.objects.get_or_create(user=user)
        clicked = [offer.id for offer in watchlist.offer.all()]
    return render(request, "auctions/index.html",{
        "listings": listings,
        "clicked": clicked,
        "categories": categories
    })


@login_required
def add_to_watchlist(request, auction_id):
    auction = Auction.objects.get(id=auction_id)
    user = request.user
    watchlist, created = WatchList.objects.get_or_create(user=user)

    if auction in watchlist.offer.all():
        watchlist.offer.remove(auction)
    else:
        watchlist.offer.add(auction)
    
    #return redirect(reverse("index"))
    return redirect(request.META.get('HTTP_REFERER', '/'))



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def addListing(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = AuctionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AuctionForm()
        
    return render(request, "auctions/addListing.html",{
        "form": form,
        "categories": categories
    })


def product(request, product_id):
    categories = Category.objects.all()
    product = Auction.objects.get(id=product_id)
    bid = Bid.objects.filter(auction=product_id).order_by('-value').first()
    if bid:    
        bid_owner = bid.user.username
    else:
        bid_owner = product.author.username

    if request.method == "POST":
        if "bid_submit" in request.POST:
            user_bid = request.POST.get("user_bid")
            print(f"\nuser_bid: {user_bid}")
            if product.current_bid is None or Decimal(user_bid) > product.current_bid:
                new_bid = Bid()
                new_bid.user = request.user
                new_bid.auction = product
                new_bid.value = Decimal(str(user_bid))
                new_bid.save()
                product.current_bid = new_bid.value
                product.save()
                print(f"\nnew bid: {product.current_bid}")
                return redirect('product', product_id=product_id)
        
        elif "comment_submit" in request.POST:
            user_comment = request.POST.get("user_comment")
            newComment = Comment()
            newComment.user = request.user
            newComment.text = user_comment
            newComment.auction = product
            newComment.save()
            return redirect('product', product_id=product_id)
    
    all_comments = Comment.objects.all()
    return render(request, "auctions/product.html", {
        "product": product,
        "categories": categories,
        "bid_owner": bid_owner,
        "comments": all_comments
    })


@login_required
def watchlist(request, category_id = 0):
    clicked = []
    categories = Category.objects.all()
    if category_id:
        listings = Auction.objects.filter(category_id=category_id)
    else:
        listings = Auction.objects.all()

    clicked = [offer.id for offer in WatchList.objects.get(user = request.user).offer.all()]
    
    return render(request, "auctions/watchlist.html",{
        "listings": listings.filter(Q(id__in=clicked)),
        "clicked": clicked,
        "categories": categories
    })