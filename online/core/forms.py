from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'your username'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'your username'
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username' , 'email' , 'password1', 'password2')
        



            