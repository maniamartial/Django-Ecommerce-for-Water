from users.models import Profile
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields


class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class User_Update_Form(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class AddressForm(UserCreationForm):
    f_name = forms.CharField(max_length=100)
    l_name = forms.CharField(max_length=100)
    phone = forms.IntegerField()
    address_1 = forms.CharField(max_length=200)
    address_2 = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['f_name', 'l_name', 'phone',
                  'address_1', 'address_2', 'city']
