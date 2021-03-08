from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Condor
from .form import CreateLead, CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.custom_mixins import OwnerAndLoginMixin


# Create your views here.
class GenericViewLanding(TemplateView):
    template_name = "landing.html"


class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class GenericListContent(LoginRequiredMixin, ListView):
    template_name = "root.html"
    context_object_name = "condor"

    # This queryset filters agent by userprofile(from owner) first if the user is an Agent(therefore belongs to an
    # organisation)
    # if the user is an owner, he already has a userprofile so we will filter by it

    def get_queryset(self):
        user = self.request.user
        if user.is_Agent:
            queryset = Condor.objects.filter(organisation=user.agent.organisation)
            # filter by logged in Agent
            queryset = queryset.objects.filter(agent__user=user)
        else:
            queryset = Condor.objects.filter(organisatioin=user.userprofile)

        return queryset


class GenericGetEachLead(LoginRequiredMixin, DetailView):
    template_name = "details.html"
    context_object_name = "details"

    def get_queryset(self):
        user = self.request.user
        if user.is_Agent:
            queryset = Condor.objects.filter(organisation=user.agent.organisation)
            # filter by logged in Agent
            queryset = queryset.objects.filter(agent__user=user)
        else:
            queryset = Condor.objects.filter(organisatioin=user.userprofile)

        return queryset


class GenericCreateLead(OwnerAndLoginMixin, CreateView):
    template_name = "new_lead.html"
    form_class = CreateLead

    def get_success_url(self):
        return reverse("leads:condor")

    def form_valid(self, form):
        # Mail logic
        send_mail(
            subject="I Love you",
            message="Nakupea Sukari",
            from_email="kenjoelmuigai@gmail.com",
            recipient_list=["jrjoemuigai@gmail.com"],
            fail_silently=False
        )
        return super(GenericCreateLead, self).form_valid(form)


class GenericUpdateLead(OwnerAndLoginMixin, UpdateView):
    template_name = "update.html"
    form_class = CreateLead
    context_object_name = "update"

    def get_queryset(self):
        user = self.request.user
        return Condor.objects.filter(organisatioin=user.userprofile)

    def get_success_url(self):
        return reverse("leads:condor")


class GenericDeleteLead(OwnerAndLoginMixin, DeleteView):
    template_name = "delete.html"
    context_object_name = "delete"

    def get_queryset(self):
        user = self.request.user
        return Condor.objects.filter(organisatioin=user.userprofile)

    def get_success_url(self):
        return reverse("leads:condor")
