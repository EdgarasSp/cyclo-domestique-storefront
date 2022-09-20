from django import forms
from .models import UserProfile
from checkout.models import Order


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {

            'default_full_name': 'Full Name',
            'default_email': 'Email',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County, State or Locality',
            'default_postcode': 'Postal Code',
        }

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ''  # may need to change to match crispy form style border-black rounded-0 profile-form-input
            self.fields[field].label = False





################################# CHANGE STATUS ORDER ##############################
class UpdateOrder(forms.ModelForm):

        class Meta:
            model = Order
            fields = ('status',)

        def status(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            state = Order.status.objects.all()

            self.fields['status'].choices = state
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = ''
