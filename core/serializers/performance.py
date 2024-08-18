from rest_framework import serializers
from ..models.performance import Performance


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'
        depth = 1
