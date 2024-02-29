from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Введите действующий email адрес.')

    class Meta:
        model = User
        fields = ('email', 'phone', 'image', 'country', 'password1', )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', ]


class UserProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'image', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
