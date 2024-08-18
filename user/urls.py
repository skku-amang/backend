from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreateAPIView.as_view(), name='user-list_create'),
    path(
        "users/<int:pk>/",
        views.UserRetrieveUpdateDestroyAPIView.as_view(),
        name="user-retrieve_update_destroy",
    ),
]
