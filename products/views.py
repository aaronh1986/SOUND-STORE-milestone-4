from django.shortcuts import render
from .models import Product


def all_products(request):
    """Shows all products + search functionality + sorting"""
    # Returns all objects from the database
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
