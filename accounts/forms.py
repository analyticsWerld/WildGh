from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms

from .models import Accounts

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = Accounts
        fields = ("email","password1","password2",)
        widgets = {
             'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
             'password1': forms.PasswordInput(attrs={"type":"password",'placeholder': 'Password'}),
             'password2': forms.PasswordInput(attrs={"type":"password",'placeholder': 'Confirm Password'}),
         }


class ChangeForm(UserChangeForm):
    class Meta:
        model = Accounts
        fields = ("photo","gender","mobile_number","address")

class LogInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)