from rest_framework import serializers

from core.models.session import Session
from core.models.team import MemberSession
from core.serializers.performance import PerformanceSerializer
from user.serializers import CustomUserSerializer
from ..models import Team, Performance


class MemberSessionSerializer(serializers.ModelSerializer):
    session = serializers.CharField(source="session.name")
    members = serializers.PrimaryKeyRelatedField(
        many=True,
        # source="members",
        queryset=CustomUserSerializer.Meta.model.objects.all(),
    )

    class Meta:
        model = MemberSession
        fields = ("id", "session", "members", "requiredMemberCount")
        ref_name = "TeamMemberSession"


class TeamSerializer(serializers.ModelSerializer):
    performance = PerformanceSerializer()
    memberSessions = MemberSessionSerializer(many=True)

    class Meta:
        model = Team
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        performance_data = validated_data.pop("performance")
        memberSessions_data = validated_data.pop("memberSessions")
        performance = Performance.objects.create(**performance_data)

        team = Team.objects.create(performance=performance, **validated_data)

        memberSessions = []
        for memberSession_data in memberSessions_data:
            members_data = memberSession_data.pop("members")
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
        # Update or create performance
        performance_data = validated_data.pop("performance")
        if instance.performance:
            for attr, value in performance_data.items():
                setattr(instance.performance, attr, value)
            instance.performance.save()
        else:
            instance.performance = Performance.objects.create(**performance_data)

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
