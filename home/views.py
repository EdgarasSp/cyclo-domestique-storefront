from django.shortcuts import render, redirect, reverse, get_object_or_404


from products.models import Product

# Create your views here.

def index(request):
    """ A view to return the index page """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)
