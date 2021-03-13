from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

from agents.forms import AssignAgentForm
from .models import Condor, Category
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
            queryset = Condor.objects.filter(organisation=user.agent.organisation, agent__isnull=False)
            # filter by logged in Agent
            queryset = queryset.objects.filter(agent__user=user)
        else:
            queryset = Condor.objects.filter(organisation=user.userprofile, agent__isnull=False)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(GenericListContent, self).get_context_data(**kwargs)
        user = self.request.user

        if user.is_owner:
            queryset = Condor.objects.filter(organisation=user.userprofile, agent__isnull=True)
            context.update({
                "unassigned_leads": queryset
            })

        return context


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
            queryset = Condor.objects.filter(organisation=user.userprofile)

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
        return Condor.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        return reverse("leads:condor")


class GenericDeleteLead(OwnerAndLoginMixin, DeleteView):
    template_name = "delete.html"
    context_object_name = "delete"

    def get_queryset(self):
        user = self.request.user
        return Condor.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        return reverse("leads:condor")


class AssignLead(OwnerAndLoginMixin, FormView):
    template_name = "assign_leads.html"
    form_class = AssignAgentForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignLead, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs

    def get_success_url(self):
        return reverse("leads:condor")

    def form_valid(self, form):
        agent = form.cleaned_data["agent"]
        lead = Condor.objects.all(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()
        return super(AssignLead, self).form_valid(form)


class CategoryListView(LoginRequiredMixin, ListView):
    template_name = "category/category_list.html"
    context_object_name = "category_list"

    def get_queryset(self):
        user = self.request.user
        if user.is_Agent:
            queryset = Category.objects.filter(organisation=user.agent.organisation)
            # filter by logged in Agent
        else:
            queryset = Category.objects.filter(organisation=user.userprofile)
        return queryset

