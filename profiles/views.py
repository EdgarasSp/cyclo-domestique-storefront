from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm, UpdateOrder

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders, 
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def profile_orders(request):
    """ Display the user orders. """
    profile = get_object_or_404(UserProfile, user=request.user)

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/orders.html'
    context = {
        'orders': orders,  
    }

    return render(request, template, context)

@login_required
def site_orders(request):
    """ Display site orders. """
    orders = Order.objects.all()

    template = 'profiles/site_orders.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)




    


######################### CHANGE STATUS ORDER ##########################################
@login_required
def edit_order(request, order_number):
    """ Edit a order in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    order = get_object_or_404(Order, order_number=order_number) 
    if request.method == 'POST':
        form = UpdateOrder(request.POST, instance=order)    ####MABU THIS SHOULD BE order_number ####WAS ORDER
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated order!')
            # return redirect(reverse('inventory'))
            return redirect(reverse('site_orders'))  # if from product details and if from inventory
        else:
            messages.error(request, 'Failed to update order. Please ensure the form is valid.')
    else:
        form = UpdateOrder(instance=order)  ####WAS ORDER
        messages.info(request, f'You are editing {order.order_number}')

    template = 'profiles/edit_order.html'
    context = {
        'form': form,
        'order': order,
        'on_inventory_page': True
    }

    return render(request, template, context)

