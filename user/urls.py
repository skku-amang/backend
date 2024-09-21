from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path(
        "users/",
        views.UserListCreateAPIView.as_view(),
    ),
    path(
        "users/<int:pk>/",
        views.UserRetrieveUpdateDestroyAPIView.as_view(),
    ),
    path("auth/login/", views.CustomTokenObtainPairView.as_view()),
    path("auth/register/", views.RegisterAPIView.as_view()),
    path("auth/refresh/", TokenRefreshView.as_view()),
]
