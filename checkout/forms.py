from django import forms
from .models import Address


class AddressForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'placeholder': field.label})


    class Meta:
        model = Address

        fields = [
            'first_name', 'last_name', 'email', 'phone_number',
            'address_line1', 'address_line2', 'postal_code', 'country', 'city', 'state',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Mohammad'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Arkiyan'}),
            'email': forms.TextInput(attrs={'placeholder': 'someone@gmail.com'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '093398004252'}),
            'address_line1': forms.TextInput(attrs={'placeholder': 'Iran, Guilan, Rasht, ...'}),
            'address_line2': forms.TextInput(attrs={'placeholder': 'Golsar, street 98'}),
            'postal_code': forms.TextInput(attrs={'placeholder': '737739472'}),
            'country': forms.TextInput(attrs={'placeholder': 'Iran'}),
            'city': forms.TextInput(attrs={'placeholder': 'Rasht'}),
            'state': forms.TextInput(attrs={'placeholder': 'Golsar'}),
        }
