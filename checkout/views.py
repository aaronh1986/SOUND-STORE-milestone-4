from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Cart empty for now")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JdFabIMsBgCDn6oLKTRnOXlgmUq0sXrqeSHaCBa3H2VUgH4LoEF766E3XN5xI4nVQjkwFLF7N9CWXANKq3BQS2P00Y5e1iYds',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

