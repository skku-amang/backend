from django.urls import path
from .views import generation, performance, session, team

urlpatterns = [
    path(
        "generations/",
        generation.GenerationListCreateAPIView.as_view(),
        name="generation-list_create",
    ),
    path(
        "generations/<str:pk>/",
        generation.GenerationRetrieveUpdateDestroyAPIView.as_view(),
        name="generation-retrieve_update_destroy",
    ),
    path(
        "performances/",
        performance.PerformanceListCreateAPIView.as_view(),
        name="performance-list_create",
    ),
    path(
        "performances/<int:pk>/",
        performance.PerformanceRetrieveUpdateDestroyAPIView.as_view(),
        name="performance-retrieve_update_destroy",
    ),
    path(
        "sessions/",
        session.SessionListCreateAPIView.as_view(),
        name="session-list_create",
    ),
    path(
        "sessions/<int:pk>/",
        session.SessionRetrieveUpdateDestroyAPIView.as_view(),
        name="session-retrieve_update_destroy",
    ),
    path("teams/", team.TeamListCreateAPIView.as_view(), name="team-list_create"),
    path(
        "teams/<int:pk>/",
        team.TeamRetrieveUpdateDestroyAPIView.as_view(),
        name="team-retrieve_update_destroy",
    ),
    path("teams/<int:pk>/apply/", team.TeamApplyAPIView.as_view(), name="team-apply"),
]
