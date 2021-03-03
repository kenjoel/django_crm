from django.shortcuts import render, redirect
from .models import Condor
from .form import CreateLead


# Create your views here.
def intro(request):
    condor = Condor.objects.all()
    context = {
        "condor": condor
    }
    return render(request, "root.html", context)


def get_each(request, pk):
    condor = Condor.objects.get(id=pk)
    context = {
        "condor": condor
    }
    return render(request, "details.html", context)


def create(request):
    the_form = CreateLead()
    if request.method == "POST":
        form = CreateLead(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": the_form
    }
    return render(request, "new_lead.html", context)


def update_lead(request, pk):
    condor = Condor.objects.get(id=pk)
    condor_form = CreateLead(instance=condor)
    if request.method == "POST":
        if condor_form.is_valid():
            condor_form.save()
        return redirect("/")
    context = {
        "condor": condor,
        "form": condor_form
    }
    return render(request, "update.html", context)


def delete_lead(request, pk):
    condor = Condor.objects.get(id=pk)
    condor.delete()
    return redirect("/")





