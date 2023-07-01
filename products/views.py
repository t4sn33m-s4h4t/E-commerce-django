
from django.shortcuts import render
from products.models import Product


def get_product(request, slug):
    
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
                }
    
    return render(request, 'products/product.html', context)


