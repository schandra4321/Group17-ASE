from django.shortcuts import render, redirect
from django.http import HttpResponse
from Users.views import *
from Auctions.forms import *
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required
from Auctions.models import *
# Create your views here.

@login_required()
def dashboard(request):
    return render(request, 'Auctions/dashboard.html')

'''
def enter_details(request):
    return render(request, 'Auctions/EnterInfo.html')

def notifications(request):
    return HttpResponse('You Can Create a auction here')

def cart(request):
    return HttpResponse('You Can Create a auction here')

def view_created(request):
    return HttpResponse('You Can Create a auction here')

def view_participating(request):
    return HttpResponse('You Can Create a auction here')

'''

def create_auction(request):

    auction_details = AuctionCreationForm()
    auction_formset = formset_factory(ItemDetailsForm)
    auction_formset_post = auction_formset(request.POST or None)
    if request.method == 'POST':

        auction_details = AuctionCreationForm(request.POST)
        auction_formset_post = auction_formset(request.POST)

        if auction_details.is_valid() and auction_formset_post.is_valid() :

            details = auction_details.save(commit=False)
            for item in auction_formset_post:

                item_name = item.cleaned_data.get('item_name')
                description = item.cleaned_data.get('description')
                base_price = item.cleaned_data.get('base_price')
                keywords =  item.cleaned_data.get('keywords')
        else :
            context = {'auction_details': auction_details,
                       'auction_formset': auction_formset_post}
            return render(request, 'Auctions/createAuction.html', context)


    context = {'auction_details':auction_details, 'auction_formset':auction_formset}
    return render(request, 'Auctions/createAuction.html', context)



