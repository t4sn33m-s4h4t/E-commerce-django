from products.views import *
from django.urls import path
urlpatterns = [
    path('<slug>', get_product, name='get_product'),
]
