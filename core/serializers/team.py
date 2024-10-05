from rest_framework import serializers

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
        depth = 1

    def create(self, validated_data):
        memberSessions_data = validated_data.pop("memberSessions")
        team = Team.objects.create(
            **validated_data, leader=self.context["request"].user
        )

        for memberSession_data in memberSessions_data:
            members_data = memberSession_data.get("members", [])
            session = Session.objects.get(name=memberSession_data["session"]["name"])
            memberSession = MemberSession.objects.create(team=team, session=session)

            for index, member_data in enumerate(members_data):
                MemberSessionMembership.objects.create(
                    memberSession=memberSession, member=member_data, index=index
                )

        return team

    def update(self, instance, validated_data):
        # 기존 memberSessions 삭제
        instance.memberSessions.all().delete()

        # TODO: 모두 삭제하고 다시 만드는 것이 아니라, 수정된 것만 수정하고 추가된 것만 추가하는 방법으로 변경

        # Update or create memberSessions
        memberSessions_data = validated_data.pop("memberSessions")
        for memberSession_data in memberSessions_data:
            members_data = memberSession_data.get("members", [])
            session = Session.objects.get(name=memberSession_data["session"]["name"])
            memberSession = MemberSession.objects.create(team=instance, session=session)

            # Update or create members
            for index, member_data in enumerate(members_data):
                MemberSessionMembership.objects.create(
                    memberSession=memberSession, index=index, member=member_data
                )

        # Update team instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
