from core.models.performance import Performance
from ..models.feedback import Feedback, FeedbackQuestion, FeedbackAnswer
from rest_framework import serializers


class FeedbackSerializer(serializers.ModelSerializer):
    performanceId = serializers.PrimaryKeyRelatedField(
        queryset=Performance.objects.all(),
        required=True,
        source="performance",
        write_only=True,
    )

    class Meta:
        model = Feedback
        fields = ("performance", "performanceId", "startDatetime", "endDatetime")
        depth = 2


class FeedbackQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackQuestion
        fields = "__all__"
        depth = 1


class FeedbackAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackAnswer
        fields = "__all__"
        depth = 1
