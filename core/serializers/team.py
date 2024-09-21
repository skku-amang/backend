from rest_framework import serializers

from core.models.session import Session
from core.models.team import MemberSession
from user.serializers import CustomUserSerializer
from ..models import Team, Performance


class MemberSessionSerializer(serializers.ModelSerializer):
    session = serializers.CharField(source="session.name")
    members = CustomUserSerializer(many=True, read_only=True)
    membersId = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=CustomUserSerializer.Meta.model.objects.all(),
        write_only=True,
        source="members",
        required=False,
    )

    class Meta:
        model = MemberSession
        fields = ("id", "session", "members", "membersId", "requiredMemberCount")
        ref_name = "TeamMemberSession"


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
        memberSessions = []

        for memberSession_data in memberSessions_data:
            members_data = memberSession_data.get("members", [])
            session = Session.objects.get(name=memberSession_data["session"]["name"])
            requiredMemberCount = memberSession_data["requiredMemberCount"]
            memberSession = MemberSession.objects.create(
                team=team, session=session, requiredMemberCount=requiredMemberCount
            )
            memberSession.members.set(members_data)
            memberSession.save()
            memberSessions.append(memberSession)

        team.memberSessions.set(memberSessions)
        return team

    def update(self, instance, validated_data):
        # Update or create memberSessions
        memberSessions_data = validated_data.pop("memberSessions")
        for memberSession_data in memberSessions_data:
            members_data = memberSession_data.pop("members")
            if memberSession_data["id"]:
                memberSession = MemberSession.objects.get(id=memberSession_data["id"])
                for attr, value in memberSession_data.items():
                    setattr(memberSession, attr, value)
                memberSession.members.set(members_data)
                memberSession.save()
            else:
                memberSession = MemberSession.objects.create(
                    team=instance, session=memberSession_data["session"]
                )
                memberSession.members.set(members_data)
                memberSession.save()

        # Update team instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
