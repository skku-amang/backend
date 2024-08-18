from rest_framework import serializers
from ..models.generation import Generation


class GenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generation
        fields = '__all__'
        depth = 1
