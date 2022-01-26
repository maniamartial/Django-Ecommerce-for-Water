
from .models import PhoneNumbers
from django.contrib.auth.models import User
from django import forms

from django.forms import fields


class PhoneNumber(forms.ModelForm):
    class Meta:
        model = PhoneNumbers
        fields = ['phone']
