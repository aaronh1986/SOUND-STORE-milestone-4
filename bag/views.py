from django.shortcuts import render, redirect, reverse, HttpResponse


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
    # print(request.session['bag']) / Write in readme as a testing technique
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity in the bag to given amount"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Removes item from bag"""

    bag = request.session.get('bag', {})

    try:
        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
