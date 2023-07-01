from django.contrib import admin
from django.urls import path
from accounts.views import *
urlpatterns = [
    path('login/', login_page, name='login'),
    path('profile/', profile_page, name='profile'),
    path('logout/', logout_page, name='logout'),
    path('register/', register, name='register'),
    path('activate/<email_token>/', activate_email, name='activate_email'),
    
]
