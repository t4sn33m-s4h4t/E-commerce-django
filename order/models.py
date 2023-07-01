from django.db import models
import uuid
from products.models import *
from base.models import BaseModel
from django.contrib.auth.models import User

class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.CharField(max_length=150, blank=False, null=False)
    phone = models.CharField(max_length=150, blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    tracking_no = models.UUIDField(uuid.uuid4, blank=True, null=True, editable=False)
    total_price = models.FloatField(blank=False, null=False, default=0)
    bkash_transition_id = models.CharField(max_length=250, blank=True, null=True)
    order_statuses = (
        ('Pending', 'Pending'),
        ('Out For Shipping', 'Out For Shipping'),
        ('Delivered', 'Delivered'),
    )
    status = models.CharField(max_length=150, choices=order_statuses, default='Pending')

    def _str_(self):
        return '(){}'.format(self.id, self.tracking_no)


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def _str_(self):
        return '(){}'.format(self.order.id, self.order.tracking_no)

