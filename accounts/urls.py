from django.urls import path
from .views import (signin,  
    register, 
    logout, 
    dashboard,
    )

urlpatterns = [
    path('login', signin, name='login'),
    path('register', register, name='register'),
    path('logout', logout, name='logout'),
    path('dashboard', dashboard, name='dashboard'),
    
]