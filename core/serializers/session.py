from rest_framework import serializers
from ..models.session import Session


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"
        depth = 1
