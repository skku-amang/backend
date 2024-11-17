from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser

from ..models.feedback import Feedback
from ..serializers.feedback import FeedbackSerializer, FeedbackQuestionSerializer, FeedbackAnswerSerializer


class FeedbackListCreateAPIView(ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser()]
        return []


class FeedbackRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return []
        return [IsAdminUser()]
