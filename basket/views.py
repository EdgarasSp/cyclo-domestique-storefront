from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'{product.name} quantity updated to {basket[item_id]}')
    else:
        basket[item_id] = quantity
        messages.success(request, f'{product.name} added to basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def update_basket(request, item_id):
    """ Update quantity of the specified product to the shopping basket """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        print(quantity)
        basket[item_id] = quantity
        messages.success(request, f'{product.name} quantity updated to {basket[item_id]}')
        
    else:
        basket.pop(item_id)
        messages.success(request, f'{product.name} removed from the basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_basket_item(request, item_id):
    """Remove product from the shopping basket"""

    try:
        product = Product.objects.get(pk=item_id)
        basket = request.session.get('basket', {})
        basket.pop(item_id)
        messages.success(request, f'{product.name} removed from the basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
