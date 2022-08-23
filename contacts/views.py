from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from .models import Contact
from django.core.mail import send_mail

# Create your views here.


def contact(request):
    if request.method == 'POST':

        # Get form values
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']       
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check if user made an inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)

            if has_contacted:
                messages.error(request, 'You already made an inquiry for this listing')
                return redirect ('/listings/'+listing_id)

        contact = Contact(
            listing=listing,
            listing_id = listing_id,
            name = name,
            email = email,
            phone = phone,
            message = message,
            user_id = user_id
            )

        contact.save()

        # #SEND email

        # send_mail(
        #     'Property Listing Inquiry',
        #     'We received an inquiry for ' + listing + '. Sign into the admin panel for more info',
        #     'tal.practice.django@gmail.com',
        #     [realtor_email, 'shlamovich@yandex.ru'],
        #     fail_silently=False
        # )

    return redirect ('/listings/'+listing_id)