from home.views import *
from django.urls import path
urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search'),
]
