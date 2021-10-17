from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """Shows all products + search functionality + sorting"""

    # Returns all objects from the database
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)


        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Use searchbar to search for products + categories")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A detailed page for a single product"""
    # Returns one object from the database
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def admin_product_add(request):
    """Allow a superuser to add to the database while logged in to the site"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Product Added to Database")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Product not added, have you filled out form correctly?')
    else:
        form = ProductForm()
    template = 'products/admin_add.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def admin_product_edit(request, product_id):
    """Allow a superuser to edit products in the database while logged in to the site"""
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product edited in database.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, f'Update failed, have you filled out the form correctly?')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'Editing {product.name}')
    template = 'products/admin_edit.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def admin_product_delete(request, product_id):
    """Allow a superuser to delete products in the database while logged in to the site"""
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f"Product deleted from database")
    return redirect(reverse('products'))