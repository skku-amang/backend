from decimal import Decimal
from rest_framework import serializers
from ..models.generation import Generation


class GenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generation
        fields = "__all__"
        depth = 1

    def validate_order(self, value):
        # 소수점 부분이 0 혹은 5인지 확인
        if value % Decimal(0.5) != 0:
            raise serializers.ValidationError("Order 값은 0.5 단위로 입력해주세요.")
        return value