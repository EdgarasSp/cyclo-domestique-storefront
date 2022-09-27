from django import forms
from .models import ContactForm

class UpdateMessage(forms.ModelForm):

        class Meta:
            model = ContactForm
            fields = ['status']  ### ('status',)