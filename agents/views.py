import random

from django.core.mail import send_mail
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from condor.models import Agent
from .forms import AgentCreateForm
from django.shortcuts import reverse
from .custom_mixins import OwnerAndLoginMixin


# Create your views here.
class GetAgents(OwnerAndLoginMixin, ListView):
    template_name = "agents/agent-list.html"

    def get_queryset(self):
        return Agent.objects.all()


class CreateAgent(OwnerAndLoginMixin, CreateView):
    template_name = "agents/new_agent.html"
    form_class = AgentCreateForm

    def get_success_url(self):
        return reverse("agents:agent-list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_Agent = True
        user.is_owner = False
        user.set_password(f"{random.randit(0,100000000)}")
        user.save()

        Agent.objets.create(user=user, organisation=self.request.user.userprofile)

        send_mail(
            subject="Congratulations Agent f'{user.username}' ",
            message="Your mission, should you choose to accept it, is to  generate wealth for the company in exchange "
                    "for salaries and freedom ",
            from_email="adversary@gmail.com",
            recipient_list=[user.email]

        )
        return super(CreateAgent, self).form_valid(form)


class AgentDetails(OwnerAndLoginMixin, DetailView):
    template_name = "agents/agent-details.html"
    context_object_name = "agents"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation)


class AgentUpdateLead(OwnerAndLoginMixin, UpdateView):
    template_name = "agents/agents-update.html"
    form_class = AgentCreateForm
    context_object_name = "agents"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation)

    def get_success_url(self):
        return reverse("agents:agent-list")


class AgentDeleteLead(OwnerAndLoginMixin, DeleteView):
    template_name = "agents/agents-delete.html"
    context_object_name = "agents"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation)

    def get_success_url(self):
        return reverse("agents:agent-list")
