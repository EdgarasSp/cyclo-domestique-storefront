from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Lj6GOGWhq9GX3KeJ68FS7s6Td89Y6mKXFUqUmwA2JXclq5DRiSLrnHntoc2IJxusoswKU0goa4KQQUU8WxaimUA008MnoGmCQ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
    