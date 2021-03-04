from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Condor
from .form import CreateLead


# Create your views here.
class GenericViewLanding(TemplateView):
    template_name = "landing.html"


class GenericListContent(ListView):
    template_name = "root.html"
    queryset = Condor.objects.all()
    context_object_name = "condor"


class GenericGetEachLead(DetailView):
    template_name = "details.html"
    queryset = Condor.objects.all()


class GenericCreateLead(CreateView):
    template_name = "new_lead.html"
    form_class = CreateLead

    def get_success_url(self):
        reverse("leads:condor")


class GenericUpdateLead(UpdateView):
    template_name = "update.html"
    queryset = Condor.objects.all()
    form_class = CreateLead

    def get_success_url(self):
        reverse("leads:details")


class GenericDeleteLead(DeleteView):
    template_name = "update.html"
    queryset = Condor.objects.all()

    def get_success_url(self):
        reverse("leads:condor")
