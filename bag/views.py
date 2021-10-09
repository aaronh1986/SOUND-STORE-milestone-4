from django.shortcuts import render


def view_bag(request):
    """View which will show selected items on a shopping bag page"""
    return render(request, 'bag/bag.html')
