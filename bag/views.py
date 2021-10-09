from django.shortcuts import render, redirect


def view_bag(request):
    """View which will show selected items on a shopping bag page"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add amount of a product to the shopping cart"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
