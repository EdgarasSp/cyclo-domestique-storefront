from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from basket.contexts import basket_contents
import stripe


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty.")
        return redirect(reverse('products'))

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Lj6GOGWhq9GX3KeJ68FS7s6Td89Y6mKXFUqUmwA2JXclq5DRiSLrnHntoc2IJxusoswKU0goa4KQQUU8WxaimUA008MnoGmCQ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
    