from django.contrib import admin
from django.urls import path
from . import views

app_name = "condor"
urlpatterns = [
    path('', views.intro, name="leads"),
    path("<int:pk>/", views.get_each, name="details"),
    path("/create ", views.create(), name="create")
]
