from django import forms
from .models import Condor
from django.contrib.auth.forms import UserCreationForm, UsernameField

from django.contrib.auth import get_user_model

User = get_user_model()


class CreateLead(forms.ModelForm):
    class Meta:
        model = Condor
        fields = (
            "first_name",
            "last_name",
            "age",
            "agent"
        )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
