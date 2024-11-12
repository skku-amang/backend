from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from core.models.team import Team
from core.serializers.team import TeamSerializer
from core.models.performance import Performance
from core.serializers.performance import PerformanceSerializer
from core.views.filters import PerformanceFilter


# ===== Basic CRUD views for Performance =====
class PerformanceListCreateAPIView(ListCreateAPIView):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filterset_class = PerformanceFilter

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser()]
        return [IsAuthenticated()]


class PerformanceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAuthenticated()]
        return [IsAdminUser()]


# ===== Custom views for Performance =====
class PerformanceTeamListAPIView(ListAPIView):
    serializer_class = TeamSerializer

    def get_queryset(self):
        return Team.objects.filter(performance__id=self.kwargs["pk"])

    def get_permissions(self):
        return [IsAuthenticated()]
