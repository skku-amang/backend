from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from core.models.session import Session
from core.serializers.session import SessionSerializer
from core.views.filters import SessionFilter


class SessionListCreateAPIView(ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    filterset_class = SessionFilter

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser()]
        return []


class SessionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAuthenticated()]
        return [IsAdminUser()]
