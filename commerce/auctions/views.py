from django import forms
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.validators import MinValueValidator


from .models import User, Comment, Bid, Auction, WatchList, Category
from decimal import ROUND_DOWN, Decimal


class AuctionForm(forms.ModelForm):
 
    class Meta:
        model = Auction
        fields = ['title', 'description', 'current_bid', 'image', 'category']
        labels = {'current_bid': 'Starting bid'}

class WatchlistButton(forms.Form):
    pass


class BidForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['current_bid']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['current_bid'].widget.attrs['class'] = 'form-control'
        self.fields['current_bid'].widget.attrs['placeholder'] = 'Enter your bid which must be higher than current bid'
        self.fields['current_bid'].widget.attrs['aria-label'] = 'Bid value'
        self.fields['current_bid'].widget.attrs['name'] = 'user_bid'
        self.fields['current_bid'].widget.attrs['min'] = '0.01'
        self.fields['current_bid'].label = ''

    def clean_current_bid(self):
        current_bid = self.cleaned_data.get('current_bid')
        if current_bid is not None and current_bid <= self.instance.current_bid:
            raise forms.ValidationError("Your bid must be higher than the current bid.")
        return current_bid


def index(request, category_id = 0):
    clicked = []
    winner_auctions = []
    if request.user.is_authenticated:
        winner_auctions = Auction.objects.filter(confirmed = False, winner =  request.user)
    categories = Category.objects.all()
    if category_id:
        listings = Auction.objects.filter(category_id=category_id)
        category_name = Category.objects.get(id= category_id).name
    else:
        listings = Auction.objects.all()
        category_name = "All"
    if request.user.is_authenticated:
        user = request.user
        watchlist, created = WatchList.objects.get_or_create(user=user)
        clicked = [offer.id for offer in watchlist.offer.all()]

    return render(request, "auctions/index.html",{
        "listings": listings.filter(is_active = True),
        "clicked": clicked,
        "categories": categories,
        "category": category_name, 
        "winner_auctions": winner_auctions
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
    winner_auctions = Auction.objects.filter(confirmed = False, winner =  request.user)
    if request.method == 'POST':
        form = AuctionForm(request.POST, request.FILES)
        if form.is_valid():
            auction = form.save(commit=False)
            auction.author = request.user 
            auction.save()  
            form.save()
            return redirect('/')
    else:
        form = AuctionForm()
        
    return render(request, "auctions/addListing.html",{
        "form": form,
        "categories": categories, 
        "winner_auctions": winner_auctions
    })


def product(request, product_id):
    categories = Category.objects.all()
    product = Auction.objects.get(id=product_id)
    bid = Bid.objects.filter(auction=product_id).order_by('-value').first()
    if bid:    
        bid_owner = bid.user.username
    else:
        bid_owner = product.author.username

    if request.user.is_authenticated:
        winner_auctions = Auction.objects.filter(confirmed=False, winner=request.user)       
    else:
        winner_auctions = []

    form = BidForm(instance=product)
    if request.method == "POST":
        if "bid_submit" in request.POST:
            form = BidForm(request.POST,instance=product)
            if form.is_valid():
                user_bid = form.cleaned_data["current_bid"]
                new_bid = Bid(user=request.user, auction=product, value=user_bid)
                new_bid.save()
                product.current_bid = new_bid.value
                product.save()
                return redirect('product', product_id=product_id)
            else:
                print(f"Errors:{form.errors.as_data()}\n") 
                print(f"Errors:{form.is_bound}")            
        
        elif "comment_submit" in request.POST:
            user_comment = request.POST.get("user_comment")
            if user_comment:
                newComment = Comment(user=request.user, text=user_comment, auction=product)
                newComment.save()
            return redirect('product', product_id=product_id)
        
        elif "end_auction" in request.POST:
            if bid is None:
                product.winner = None
                product.confirmed = True
            else:
                product.winner = Bid.objects.get(auction=product, value=bid.value).user
            product.is_active = False
            product.save()
            return redirect('index')
    
    all_comments = Comment.objects.filter(auction=product_id)
    return render(request, "auctions/product.html", {
        "product": product,
        "categories": categories,
        "bid_owner": bid_owner,
        "comments": all_comments,
        "auction_owner": product.author == request.user, 
        "winner_auctions": winner_auctions,
        "form": form
    })


@login_required
def watchlist(request, category_id = 0):
    clicked = []
    winner_auctions = Auction.objects.filter(confirmed = False, winner =  request.user)
    categories = Category.objects.all()
    if category_id:
        listings = Auction.objects.filter(category_id=category_id)
    else:
        listings = Auction.objects.all()


    clicked = [offer.id for offer in WatchList.objects.get(user = request.user).offer.all()]
    
    return render(request, "auctions/watchlist.html",{
        "listings": listings.filter(Q(id__in=clicked)),
        "clicked": clicked,
        "categories": categories, 
        "winner_auctions": winner_auctions
    })

@login_required
def user_offers(request, user, category_id=0):
    user = request.user
    listings = Auction.objects.filter(author=user, is_active = True)
    notactive_listings = Auction.objects.filter(author=user, is_active = False)
    won_listings = Auction.objects.filter(winner = user)
    winner_auctions = Auction.objects.filter(confirmed = False, winner =  user)
    clicked = []
    categories = Category.objects.all()
    if category_id:
        listings = listings.filter(category_id=category_id)
        won_listings = won_listings.filter(category_id=category_id)
        category_name = Category.objects.get(id= category_id).name

    else:
        category_name = "All"
   
    watchlist, created = WatchList.objects.get_or_create(user=user)
    clicked = [offer.id for offer in watchlist.offer.all()]
    return render(request, "auctions/offers.html",{
        "createdlistings": listings,
        "wonlistings": won_listings,
        "clicked": clicked,
        "categories": categories,
        "category": category_name, 
        "winner_auctions": winner_auctions,
        "notactive_listings": notactive_listings
    })

def close_listing(request, listing_id):
    if request.method == "POST" and "close_button" in request.POST:
        product = Auction.objects.get(id = listing_id)
        product.confirmed = True
        product.save()
        print("zamykanie aukcji")
        return redirect(request.META.get('HTTP_REFERER', '/'))
