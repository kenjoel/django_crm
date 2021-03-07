from django.urls import path
from .views import GetAgents, CreateAgent, AgentDetails,AgentUpdateLead, AgentDeleteLead

app_name = "agents"

urlpatterns = [
    path("", GetAgents.as_view(), name="agent-list"),
    path("new_agent/", CreateAgent.as_view(), name="create-agent"),
    path("<int:pk>", AgentDetails.as_view(), name="agent-details"),
    path("<int:pk>/update/", AgentUpdateLead.as_view(), name="agent-update"),
    path("<int:pk>/delete/", AgentDeleteLead.as_view(), name="agent-delete")
]
