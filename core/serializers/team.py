from rest_framework import serializers
from ..models import Team, Performance


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = "__all__"
        ref_name = "TeamPerformance"


class TeamSerializer(serializers.ModelSerializer):
    performance = PerformanceSerializer()

    class Meta:
        model = Team
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        performance_data = validated_data.pop("performance")
        performance = Performance.objects.create(**performance_data)

        team = Team.objects.create(performance=performance, **validated_data)
        return team

    def update(self, instance, validated_data):
        performance_data = validated_data.pop("performance")

        # Update or create performance
        if instance.performance:
            for attr, value in performance_data.items():
                setattr(instance.performance, attr, value)
            instance.performance.save()
        else:
            instance.performance = Performance.objects.create(**performance_data)

        # Update team instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
