from rest_framework import serializers

from core.models.session import Session
from core.models.team import MemberSession, MemberSessionMembership
from user.models import CustomUser
from user.serializers import CustomUserSerializer
from ..models import Team, Performance


class MemberSessionMemberShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberSessionMembership
        fields = ("index", "member")


class MemberSessionSerializer(serializers.ModelSerializer):
    session = serializers.CharField(source="session.name")
    members = MemberSessionMemberShipSerializer(many=True, read_only=True)
    membersId = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(
            queryset=CustomUser.objects.all(), allow_null=True
        ),
        write_only=True,
        source="members",
        required=False,
        allow_empty=True,
    )

    class Meta:
        model = MemberSession
        fields = ("session", "members", "membersId")
        ref_name = "TeamMemberSession"


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
        memberships = MemberSessionMembership.objects.filter(memberSession=obj)
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
        memberSessions = []

        for memberSession_data in memberSessions_data:
            members_data = memberSession_data.get("members", [])
            session = Session.objects.get(name=memberSession_data["session"]["name"])
            memberSession = MemberSession.objects.create(team=team, session=session)

            memberSessionMembership = []
            index = 0
            for member_data in members_data:
                memberSessionMembership.append(
                    MemberSessionMembership.objects.create(
                        memberSession=memberSession, member=member_data, index=index
                    )
                )
                index += 1
            memberSession.members.set(memberSessionMembership)
            memberSession.save()
            memberSessions.append(memberSession)

        team.memberSessions.set(memberSessions)
        return team

    # not implemented
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
