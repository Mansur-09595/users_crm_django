from django.db import models
from django.forms import fields, forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name  = forms.CharField(max_length=100,label='Имя')
    last_name  = forms.CharField(max_length=100, label='Фамилия')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)