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

        return render(request, template)

    else:
        return render(request, 'contact/contact.html')


@login_required
def site_messages(request):
    """ Display site messages. """
    all_messages = ContactForm.objects.all()

    template = 'contact/contact_messages.html'
    context = {
        'all_messages': all_messages,
    }

    return render(request, template, context)


@login_required
def delete_message(request, pk):   ### product_id
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    message = get_object_or_404(ContactForm, pk=pk)   ## new
    message.delete()
    messages.success(request, 'Product deleted!')

    return redirect(reverse('site_messages'))
