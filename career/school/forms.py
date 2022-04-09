from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SchoolBuffer

class CreateUserForm(forms.ModelForm):
    class Meta:
        model=SchoolBuffer
        fields=['name','address','standard','username','password','board']
