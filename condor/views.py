from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Condor
from .form import CreateLead, CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


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
    queryset = Condor.objects.all()
    context_object_name = "condor"


class GenericGetEachLead(LoginRequiredMixin, DetailView):
    template_name = "details.html"
    queryset = Condor.objects.all()
    context_object_name = "details"


class GenericCreateLead(LoginRequiredMixin, CreateView):
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


class GenericUpdateLead(LoginRequiredMixin, UpdateView):
    template_name = "update.html"
    queryset = Condor.objects.all()
    form_class = CreateLead
    context_object_name = "update"

    def get_success_url(self):
        return reverse("leads:condor")


class GenericDeleteLead(LoginRequiredMixin, DeleteView):
    template_name = "delete.html"
    queryset = Condor.objects.all()
    context_object_name = "delete"

    def get_success_url(self):
        return reverse("leads:condor")


