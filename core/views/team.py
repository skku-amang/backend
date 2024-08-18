from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models.team import Team
from core.serializers.team import TeamSerializer


class TeamListCreateAPIView(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
