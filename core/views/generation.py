from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser

from core.models.generation import Generation
from core.serializers.generation import GenerationSerializer
from core.views.filters import GenerationFilter


class GenerationListCreateAPIView(ListCreateAPIView):
    queryset = Generation.objects.all()
    serializer_class = GenerationSerializer
    filterset_class = GenerationFilter

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser()]
        return []


class GenerationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Generation.objects.all()
    serializer_class = GenerationSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return []
        return [IsAdminUser()]
