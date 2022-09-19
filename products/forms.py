from django import forms
from .models import Product, Category, Division


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        
        divisions = Division.objects.all() # DOES GET DIVISIONS BUT UNABLE TO SHOW IN THE FORM 
        friendly_names_div = [(c.id, c.get_friendly_name()) for c in divisions] # DOES GET DIVISIONS BUT UNABLE TO SHOW IN THE FORM

        self.fields['category'].choices = friendly_names
        self.fields['name'].choices = friendly_names_div  # DOES GET DIVISIONS BUT UNABLE TO SHOW IN THE FORM
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = ''
