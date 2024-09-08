from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models.generation import Generation
from core.serializers.generation import GenerationSerializer
from core.views.filters import GenerationFilter


class GenerationListCreateAPIView(ListCreateAPIView):
    queryset = Generation.objects.all()
    serializer_class = GenerationSerializer
    filterset_class = GenerationFilter


class GenerationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Generation.objects.all()
    serializer_class = GenerationSerializer
