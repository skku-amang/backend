from rest_framework import serializers
from .models import CustomUser, PositionChoices
from django.contrib.auth.hashers import make_password


class CustomUserSerializer(serializers.ModelSerializer):
    position = serializers.ChoiceField(
        required=False, choices=PositionChoices.choices()
    )

    class Meta:
        model = CustomUser
        fields = "__all__"
        read_only_fields = [
            "is_admin",
            "is_superuser",
            "is_staff",
            "date_joined",
            "created_datetime",
            "updated_datetime",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        if "password" in validated_data:
            validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if "password" in validated_data:
            validated_data["password"] = make_password(validated_data["password"])
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["position"] = (
            instance.get_position_display()
        )  # Enum의 이름 대신 값 반환
        representation["department"] = (
            instance.department.name if instance.department else None
        )
        return representation
