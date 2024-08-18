from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models.session import Session
from core.serializers.session import SessionSerializer


class SessionListCreateAPIView(ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class SessionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
