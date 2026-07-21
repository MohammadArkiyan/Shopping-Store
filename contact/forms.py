from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'placeholder': field.label})

    class Meta:
        model = Contact

        fields = [
            'username', 'email', 'subject', 'body'
        ]
