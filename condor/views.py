from django.shortcuts import render
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
    context = {
        "form": the_form
    }

    return render(request, "new_lead.html", context)


