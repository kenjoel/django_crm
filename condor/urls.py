from django.urls import path
from .views import (
    GenericListContent,
    GenericGetEachLead,
    GenericCreateLead,
    GenericUpdateLead,
    GenericDeleteLead
)

app_name = "leads"
urlpatterns = [
    path('leads/', GenericListContent.as_view(), name="condor"),
    path("<int:pk>/", GenericGetEachLead.as_view(), name="details"),
    path("create/", GenericCreateLead, name="create"),
    path("<int:pk>/update/", GenericUpdateLead.as_view(), name="update"),
    path("<int:pk>/delete/", GenericDeleteLead.as_view(), name="delete")
]
