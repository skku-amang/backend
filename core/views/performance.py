from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from core.models.performance import Performance
from core.serializers.performance import PerformanceSerializer
from core.views.filters import PerformanceFilter


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
