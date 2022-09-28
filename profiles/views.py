from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .models import UserProfile
from .forms import UserProfileForm, UpdateOrder
from checkout.models import Order


@login_required
def profile(request):
    """ Display user profile page. """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def profile_orders(request):
    """ Display user orders. """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    orders = user_profile.orders.all()

    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                orders = orders.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            orders = orders.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    template = 'profiles/orders.html'
    context = {

        'orders': orders,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'on_inventory_page': True,
    }

    return render(request, template, context)


@login_required
def site_orders(request):
    """ Display all site orders. """
    orders = Order.objects.all()

    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                orders = orders.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            orders = orders.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    template = 'profiles/site_orders.html'
    context = {
        'orders': orders,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'on_inventory_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Display user orders details/confirmation. """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation was emailed on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def edit_order(request, order_number):
    """ Edit order status in global order history """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    order = get_object_or_404(Order, order_number=order_number)
    if request.method == 'POST':
        form = UpdateOrder(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated order!')
            return redirect(reverse('site_orders'))
        else:
            messages.error(request, 'Failed to update order status.'
                           'Please ensure the form is valid.')
    else:
        form = UpdateOrder(instance=order)
        messages.info(request, f'You are editing status '
                      f'for {order.order_number}')

    template = 'profiles/edit_order.html'
    context = {
        'form': form,
        'order': order,
        'on_inventory_page': True
    }

    return render(request, template, context)
