# cart/views.py
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from cart.models import *
from django.contrib.auth.models import User
from products.models import Product
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def cart(request):
    cart_items = CartItems.objects.filter(user=request.user)

    total_price = 0

    for cart_item in cart_items:
        product_price = int(Product.objects.get(slug=cart_item.product.slug).price)
        print(product_price)
        total_price += product_price * int(cart_item.quantity)

    return render(request, 'cart/cart.html', context = {'cart_items': cart_items, 'total_price': total_price})


@login_required(login_url='/accounts/login/')
def add_to_cart(request, product_id):
    product = Product.objects.get(slug=product_id)
    quantity = int(request.GET.get('quantity'))
    cart = Cart.objects.filter(user=request.user).first()
    if cart is None:
        cart = Cart.objects.create(user=request.user)
    cart_items, created = CartItems.objects.get_or_create(
        cart=cart,
        user=request.user,
        product=product,

    )

    if created:
        cart_items.quantity = quantity
    else:
        cart_items.quantity += quantity

    cart_items.save()
    
    messages.success(request, "Product added to cart.")
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
@login_required(login_url='/accounts/login/')
def remove_from_cart(request, product_id):
    product = Product.objects.get(slug=product_id)
    cart_items = CartItems.objects.get(product=product, user=request.user)
    cart_items.delete()
    return redirect('cart')