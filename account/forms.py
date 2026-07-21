from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import EmailValidator, MaxLengthValidator, RegexValidator, MinLengthValidator
from django.core.exceptions import ValidationError



# --------------------
# Helper Validators
# --------------------

username_regex = RegexValidator(
    regex=r'^[\w.@+-]+$',
    message='Username mat contain only letters, digits and @/./+/-/_ characters.'
)


# ------------------------
# 1) CustomUserCreationForm: add more fields, messages and feature
# ------------------------

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='Email',
        validators=[EmailValidator(message='Email address is invalid.')],
        help_text='Enter a valid email.',
        error_messages={'required': 'Entering an email is required.', },
        widget=forms.EmailInput(attrs={'placeholder': 'example@gmail.com'}, ),
    )

    first_name = forms.CharField(
        required=False,
        label='First Name',
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}, ),
    )

    last_name = forms.CharField(
        required=True,
        label='Last Name',
        max_length=40,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}, ),
    )

    phone_number = forms.CharField(
        required=True,
        label='Phone Number',
        error_messages={'required': 'Entering a phone number is required'},
        max_length=11,
        widget=forms.NumberInput(attrs={'placeholder': 'Phone Number'}),
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'phone_number',
            'email',
            'password1',
            'password2',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'autocomplete': 'off', })

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('This email is already exist.')

        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords are not same.')

        try:
            validate_password(password2, user=None)
        except ValidationError as e:
            raise forms.ValidationError(e.messages)

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')

        if commit:
            user.save()

        return user


# ------------------------
# 2) ManualSignupForm
# ------------------------

class ManualSignupForm(forms.ModelForm):
    password1 = forms.CharField(
        label='password',
        required=True,
        help_text='create your password',
        strip=False,
        validators=[MinLengthValidator(8)],
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'password'})
    )

    password2 = forms.CharField(
        label='repeat your password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'repeat password', })
    )

    def clean_username(self):
        username = self.cleaned_data.get('username'),
        username_regex(username),
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('This username already exist')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email'),
        if email:
            EmailValidator(message='This email is invalid')
            if User.objects.filter(email__iexact=email).exists():
                raise forms.ValidationError('This email is already exist')
        return email

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('password1')
        p2 = cleaned.get('password2')

        if p1 and p2 and p1 != p2:
            self.add_error('password2', "passwords are not same")

        if p2:
            try:
                validate_password(p2)
            except ValidationError as e:
                # add all messages to password2
                self.add_error('password2', e.messages)
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@gmail.com'}),
        }


# ------------------------
# 3) CustomAuthenticationForm:
# ------------------------

class CustomAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=False, label='remember me')

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=request, *args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'username or email'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'password'})

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError("Your account is inactive.", code='inactive')


from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()



class UserUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']



class ProfileUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'image' in self.fields:
            self.fields['image'].widget.attrs.update({'class': 'form-control-file'})

    class Meta:
        model = Profile
        fields = ['image']
