from urllib import request
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signin (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect ('dashboard')

        else:
            messages.error(request, 'Invalid credentials')
            return redirect ('login')

    else:
        return render(request, 'accounts/login.html')

def register (request):

    if request.method == 'POST':

        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username is taken')
            # check email  
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email is already registered')
                    return redirect('register')
                # create user
                else:
                    user = User.objects.create_user(
                        username = username,
                        password = password,
                        email = email,
                        first_name = first_name,
                        last_name = last_name
                        )
                    user.save()
                    messages.success(request, 'Thank you for registering, you can now log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render (request, 'accounts/register.html')


def signout (request):
    if request.method == 'POST':
        logout(request)
    
    return redirect ('home')

def dashboard (request):
    return render (request, 'accounts/dashboard.html')