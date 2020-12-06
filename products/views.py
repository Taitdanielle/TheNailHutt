from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):

    products = get_object_or_404(product, pk=product_id)

    context = {
        'product': products,
    }
    
    return render(request, 'products/product_detail.html', context)    