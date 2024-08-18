from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models.generation import Generation
from core.serializers.generation import GenerationSerializer


class GenerationListCreateAPIView(ListCreateAPIView):
    queryset = Generation.objects.all()
    serializer_class = GenerationSerializer


class GenerationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Generation.objects.all()
    serializer_class = GenerationSerializer
