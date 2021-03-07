from django import forms
from condor.models import Agent


class AgentCreateForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            "user",
        )
