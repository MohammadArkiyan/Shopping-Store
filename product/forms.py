# product/forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label or ''
            })

    class Meta:
        model = Comment

        fields = ['body', 'name', 'email']

