from django.urls import path
from . import views

app_name = "workout"

urlpatterns = [
    path("workout_types/", views.get_workout_types, name="workout_types"),
    path("logs/", views.post_log, name="logs"),
    path("history/", views.list_history, name="history"),
    path("logs/<int:pk>/", views.LogRetrieveDestroyView.as_view(), name="log"),
    path("dashboard/", views.graph_log_list, name="dashboard"),
]
