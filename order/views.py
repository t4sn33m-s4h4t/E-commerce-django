from django.shortcuts import render, redirect
from order.models import *
from cart.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.


# user........
# name
# email
# phone
# address
# tracking_no
# total_price............
# bkash_transition_id
# status.........

@login_required(login_url='/accounts/login/')
def place_order(request):
    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        bkash_transition_id = request.POST['bkash_transition_id']
        cart = Cart.objects.filter(user=request.user)
        cart_items = CartItems.objects.filter(user = request.user)
        temp_total_price = 0

        def get_total_price(cart_items, temp_total_price):
            
            for item in cart_items:
                temp_total_price += item.product.price * item.quantity


            return temp_total_price

        total_price = get_total_price(cart_items, temp_total_price)
        order = Order.objects.create(
            user=request.user,
            name = name,
            email =email,
            address= address,
            phone = phone,
            total_price = total_price,
            bkash_transition_id =bkash_transition_id,
            status='Pending',
        )
        for item in cart_items:
            order_item = OrderItem.objects.create(
                order = order ,
                product = item.product,
                price = item.product.price,
                quantity = item.quantity,
            )



        Cart.objects.all().delete()

    return render(request,'order/order.html')
