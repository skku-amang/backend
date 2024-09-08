from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models.performance import Performance
from core.serializers.performance import PerformanceSerializer
from core.views.filters import PerformanceFilter


class PerformanceListCreateAPIView(ListCreateAPIView):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filterset_class = PerformanceFilter


class PerformanceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
