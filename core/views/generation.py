from decimal import Decimal
from django.http import Http404
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

    def get_object(self):
        pk = self.kwargs.get('pk')
        try:
            # pk 값을 Decimal로 변환하여 조회
            decimal_pk = Decimal(pk)
        except Exception:
            # Decimal 변환에 실패하면 404 오류 반환
            raise Http404("Invalid Generation ID")

        # Decimal 값으로 Generation을 조회
        try:
            return Generation.objects.get(order=decimal_pk)
        except Generation.DoesNotExist:
            # 객체를 찾지 못하면 404 오류 반환
            raise Http404("Generation not found")
