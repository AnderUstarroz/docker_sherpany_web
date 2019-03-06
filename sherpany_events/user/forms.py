from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from .models import User
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', )

    def clean_email(self):
        try:
            if User.objects.get(email=self.cleaned_data['email']):
                raise ValidationError('%s already exists' % self.cleaned_data['email'])
        except User.DoesNotExist:
            pass

        return self.cleaned_data['email']


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        self.user = authenticate(username=self.cleaned_data.get('email'), password=self.cleaned_data.get('password1'))
        if not self.user:
            raise ValidationError('Invalid user or password')

        return self.cleaned_data
