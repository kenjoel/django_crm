from django import forms
from .models import Condor


class CreateLead(forms.ModelForm):
    class Meta:
        model = Condor
        fields = (
            "first_name",
            "last_name",
            "age",
            "agent"
        )
