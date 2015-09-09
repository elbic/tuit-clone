from django import forms
from django.db import models
from django.contrib.auth.models import User

class Profile(forms.ModelForm):
    class Meta:
        model = User
        # exclude = ['date']
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            "username" : forms.TextInput(attrs={"class" : "form-control"}),
            "first_name" : forms.TextInput(attrs={"class" : "form-control"}),
            "last_name" : forms.TextInput(attrs={"class" : "form-control"}),
            "email" : forms.TextInput(attrs={"class" : "form-control"}),
        }
