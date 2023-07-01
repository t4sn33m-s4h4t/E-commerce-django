from django.contrib import admin
from order.models import *
# Register your models here.
admin.site.register(OrderItem)
admin.site.register(Order)