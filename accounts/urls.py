from django.urls import path
from .views import (signin,  
    register, 
    signout, 
    dashboard,
    )

urlpatterns = [
    path('login', signin, name='login'),
    path('register', register, name='register'),
    path('logout', signout, name='logout'),
    path('dashboard', dashboard, name='dashboard'),
    
]