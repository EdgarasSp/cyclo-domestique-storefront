from django.shortcuts import render

# Create your views here.

def about(request):
    """ A view to return theabout page """

    return render(request, 'about/about.html')
