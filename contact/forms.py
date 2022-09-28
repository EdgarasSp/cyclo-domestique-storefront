from django import forms
from .models import ContactForm


class UpdateMessage(forms.ModelForm):
    """ Update user messgae status """
    class Meta:
        model = ContactForm
        fields = ['status']
