from django.contrib import admin
from django.urls import path
from . import views

app_name = "leads"
urlpatterns = [
    path('', views.intro, name="condor"),
    path("<int:pk>/", views.get_each, name="details"),
    path("create/", views.create, name="create"),
    path("<int:pk>/update/", views.update_lead, name="update"),
    path("<int:pk>/delete/", views.delete_lead, name="delete")
]
