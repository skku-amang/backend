from rest_framework import serializers

from .feedback import FeedbackSerializer
from ..models.performance import Performance


class PerformanceSerializer(serializers.ModelSerializer):
    feedback = FeedbackSerializer(required=False)
    
    class Meta:
        model = Performance
        fields = "__all__"
        depth = 1
