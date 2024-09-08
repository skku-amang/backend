from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models.team import Team
from core.serializers.team import TeamSerializer
from core.views.filters import TeamFilter


class TeamListCreateAPIView(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filterset_class = TeamFilter


class TeamRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
