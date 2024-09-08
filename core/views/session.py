from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models.session import Session
from core.serializers.session import SessionSerializer
from core.views.filters import SessionFilter


class SessionListCreateAPIView(ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    filterset_class = SessionFilter


class SessionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
