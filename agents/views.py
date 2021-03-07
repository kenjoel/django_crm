from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from condor.models import Agent
from .forms import AgentCreateForm
from django.shortcuts import reverse


# Create your views here.
class GetAgents(LoginRequiredMixin, ListView):
    template_name = "agents/agent-list.html"

    def get_queryset(self):
        return Agent.objects.all()


class CreateAgent(LoginRequiredMixin, CreateView):
    template_name = "agents/new_agent.html"
    form_class = AgentCreateForm

    def get_success_url(self):
        return reverse("agents:agent-list")

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(CreateAgent, self).form_valid(form)


class AgentDetails(LoginRequiredMixin,DetailView):
    template_name = "agents/agent-details.html"
    context_object_name = "agents"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation)


class AgentUpdateLead(LoginRequiredMixin, UpdateView):
    template_name = "agents/agents-update.html"
    form_class = AgentCreateForm
    context_object_name = "agents"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation)

    def get_success_url(self):
        return reverse("agents:agent-list")


class AgentDeleteLead(LoginRequiredMixin, DeleteView):
    template_name = "agents/agents-delete.html"
    context_object_name = "agents"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation)

    def get_success_url(self):
        return reverse("agents:agent-list")


