from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import ContactForm

# Create your views here.

def contact(request):
    """ A view to return the contact page """

    if request.method == 'POST':
        """ A view to post contact message """

        subject_type = request.POST.get('subject_type')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        contact_number = request.POST.get('contact_number')
        email_address = request.POST.get('email_address')
        message = request.POST.get('message')

        contact_form = ContactForm.objects.create(
            subject_type=subject_type,
            first_name=first_name,
            last_name=last_name,
            contact_number=contact_number,
            email_address=email_address,
            message=message,
        )

        contact_form.save()

        messages.add_message(
            request, messages.SUCCESS, f"Thank you {first_name}."
            f" For your message, we will reply within 24 hours.")

        template = 'contact/contact.html'

        context = {
        'on_inventory_page': True,
    }


        return render(request, template, context)

    else:
        return render(request, 'contact/contact.html')


@login_required
def site_messages(request):
    """ Display site messages. """
    all_messages = ContactForm.objects.all()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                all_messages = all_messages.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            all_messages = all_messages.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter search term!")
                return redirect(reverse('site_message'))  #tbs was site
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            all_messages = all_messages.filter(queries)

    current_sorting = f'{sort}_{direction}'

    template = 'contact/contact_messages.html'
    context = {
        'all_messages': all_messages,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'on_inventory_page': True,
    }

    return render(request, template, context)



###################  FIX   ##################################### 


@login_required
def delete_message(request, pk):   ### product_id
    """ Delete user messages from the admin inbox"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    message = get_object_or_404(ContactForm, pk=pk)   ## new
    message.delete()
    messages.success(request, 'Message deleted!')

    return redirect(reverse('site_messages'))
