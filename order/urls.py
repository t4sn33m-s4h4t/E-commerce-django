from order.views import *
from django.urls import path

urlpatterns = [
    path('place-order/', place_order, name='place_order'),
]
