
from django.urls import path
from cart.views import *
urlpatterns = [
    path('', cart, name='cart'),
    path('add/<product_id>', add_to_cart, name='add_to_cart'),
    path('remove/<product_id>', remove_from_cart, name='remove_from_cart'),
]
