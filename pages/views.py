from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, state_choices, price_choices

# Create your views here.

def home(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings':listings,
        # choices for search
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    
    
    return render (request, '../templates/home.html', context)


def about (request):
    realtors = Realtor.objects.all()

    mvp = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors':realtors,
        'mvp':mvp
    }
    return render (request, '../templates/about.html', context)