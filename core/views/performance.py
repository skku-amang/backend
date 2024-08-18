from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models.performance import Performance
from core.serializers.performance import PerformanceSerializer


class PerformanceListCreateAPIView(ListCreateAPIView):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer


class PerformanceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
