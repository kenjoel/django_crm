from django.urls import path
from .views import (
    GenericListContent,
    GenericGetEachLead,
    GenericCreateLead,
    GenericUpdateLead,
    GenericDeleteLead,
    AssignLead,
    CategoryListView,
    CategoryDetailView,
    CategoryViewUpdate
)

app_name = "leads"
urlpatterns = [
    path('', GenericListContent.as_view(), name="condor"),
    path("<int:pk>/", GenericGetEachLead.as_view(), name="details"),
    path("create/", GenericCreateLead.as_view(), name="create"),
    path("<int:pk>/update/", GenericUpdateLead.as_view(), name="update"),
    path("<int:pk>/delete/", GenericDeleteLead.as_view(), name="delete"),
    path("<int:pk>/assign/", AssignLead.as_view(), name="assign-lead"),
    path("<int:pk>/category-update/", CategoryViewUpdate.as_view(), name="category_update"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category_detail")
]
