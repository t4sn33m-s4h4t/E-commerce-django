from django.shortcuts import render
from products.models import *
from django.contrib import messages
# Create your views here.
def index(request):
    
    context = {'products': Product.objects.all()}
    return render(request, 'home/index.html', context)
def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(product_name__icontains=query)
    msg = "Showing results for \"{}\"".format(query)
    messages.info(request, msg)
    return render(request, 'home/index.html', {
        'products': products,
    })