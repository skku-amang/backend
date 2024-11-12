from rest_framework import serializers

from .feedback import FeedbackSerializer
from ..models.performance import Performance


class PerformanceSerializer(serializers.ModelSerializer):
    feedback = FeedbackSerializer()
    
    class Meta:
        model = Performance
        fields = "__all__"
        depth = 1
