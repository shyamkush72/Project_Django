from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm, PasswordChangeForm, \
    PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control border-2'}),
                                required=True)
    password2 = forms.CharField(label="Confirm Password",
                                widget=forms.PasswordInput(attrs={'class': 'form-control border-2'}), required=True)
    email = forms.EmailField(min_length=8, max_length=50, required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control border-2'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control border-2'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(label="Username",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}), required=True)
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class PasscodeChange(PasswordChangeForm):
    old_password = forms.CharField(label="Old Password", strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control border-2', 'autocomplete': 'current-password', 'autofocus': True}))
    new_password1 = forms.CharField(label='New Password', strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control border-2', 'autocomple': 'newpassword'}),
                                    help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label='Confirm Passwordd', strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control border-2', 'autocomplete': 'newpassword'}))


class PassCodeReset(PasswordResetForm):
    email = forms.EmailField(label=_('Email Address'), min_length=8, max_length=20, required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control border-2', 'autofocus': True}))


class MysetPassword(SetPasswordForm):
    new_password1 = forms.CharField(label=_('New Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
                                    help_text=password_validation.password_validators_help_text_html)
    new_password2 = forms.CharField(label=_('Confirm Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}))


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'zipcode', 'state']
        labels = {'name': 'Name', 'locality': 'Locality', 'city': 'City', 'zipcode': 'ZipCode', 'state': 'State'}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'locality': forms.TextInput(attrs={'class': 'form-control'}),
                   'city': forms.TextInput(attrs={'class': 'form-control'}),
                   'state': forms.Select(attrs={'class': 'form-control'}),
                   'zipcode': forms.NumberInput(attrs={'class': 'form-control'}), }
