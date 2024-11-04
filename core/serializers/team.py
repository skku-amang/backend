from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.models.session import Session
from core.models.team import MemberSession, MemberSessionMembership
from user.models import CustomUser
from user.serializers import CustomUserSerializer
from ..models import Team, Performance


class MemberSessionSerializer(serializers.ModelSerializer):
    session = serializers.CharField(source="session.name")
    members = serializers.SerializerMethodField()
    membersId = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(
            queryset=CustomUser.objects.all(), allow_null=True
        ),
        write_only=True,
        source="members",
        required=False,
        allow_empty=True,
    )

    def get_members(self, obj):
        memberships = MemberSessionMembership.objects.filter(
            memberSession=obj
        ).order_by("index")
        return [
            CustomUserSerializer(membership.member).data if membership.member else None
            for membership in memberships
        ]

    class Meta:
        model = MemberSession
        fields = ("session", "members", "membersId")


class TeamSerializer(serializers.ModelSerializer):
    memberSessions = MemberSessionSerializer(many=True)
    performanceId = serializers.PrimaryKeyRelatedField(
        queryset=Performance.objects.all(), source="performance"
    )

    class Meta:
        model = Team
        fields = "__all__"
        depth = 2

    def create(self, validated_data):
        memberSessions_data = validated_data.pop("memberSessions")
        team = Team.objects.create(
            **validated_data, leader=self.context["request"].user
        )

        for memberSession_data in memberSessions_data:
            members_data = memberSession_data.get("members", [])
            session = Session.objects.get(name=memberSession_data["session"]["name"])

            if MemberSession.objects.filter(team=team, session=session).exists():
                raise ValidationError(
                    f"MemberSession with session '{session.name}' already exists for this team.",
                    code='duplicate_session'
                )

            memberSession = MemberSession.objects.create(team=team, session=session)

            for index, member_data in enumerate(members_data):
                MemberSessionMembership.objects.create(
                    memberSession=memberSession, member=member_data, index=index
                )

        return team

    def update(self, instance, validated_data):
        instance.memberSessions.all().delete()

        memberSessions_data = validated_data.pop("memberSessions")
        for memberSession_data in memberSessions_data:
            members_data = memberSession_data.get("members", [])
            session = Session.objects.get(name=memberSession_data["session"]["name"])

            if MemberSession.objects.filter(team=instance, session=session).exists():
                raise ValidationError(
                    f"MemberSession with session '{session.name}' already exists for this team.",
                    code='duplicate_session'
                )

            memberSession = MemberSession.objects.create(team=instance, session=session)

            for index, member_data in enumerate(members_data):
                MemberSessionMembership.objects.create(
                    memberSession=memberSession, index=index, member=member_data
                )

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
