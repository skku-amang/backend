from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

from core.models.session import Session
from core.models.team import MemberSessionMembership, Team
from core.permissions import IsTeamLeaderOrAdmin
from core.serializers.session import SessionSerializer
from core.serializers.team import TeamSerializer
from core.views.filters import TeamFilter
from user.models import CustomUser


class TeamListCreateAPIView(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filterset_class = TeamFilter

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return [IsAuthenticated()]


class TeamRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAuthenticated()]
        return [IsTeamLeaderOrAdmin()]

    def patch(self, request, *args, **kwargs):
        return Response(
            {"detail": "Method 'PATCH' not implemented."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )


class TeamApplyAPIView(GenericAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

    @staticmethod
    def _get_memberSessionMembershipOrErrorResponse(team, session, index):
        if session is None:
            return Response(
                {"session": "session 필드는 필수입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            session = Session.objects.get(name=session)
        except Session.DoesNotExist:
            return Response(
                {"session": f"{session}는 존재하지 않는 session 입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if index is None:
            return Response(
                {"index": "index 필드는 필수입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        ms = team.memberSessions.get(session=session)
        max_members_count = ms.members.count()
        if (index - 1) > max_members_count:
            return Response(
                {"index": f"{max_members_count}를 초과할 수 없습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        oldMemberSessionMemberShipList = ms.members.all()
        newMemberSessionMemberShipList = oldMemberSessionMemberShipList
        msship = newMemberSessionMemberShipList.get(index=index - 1)
        return msship

    def post(self, request, **kwargs):
        team = self.get_object()
        session_name = request.data.get("session")
        index = request.data.get("index")
        msship = self._get_memberSessionMembershipOrErrorResponse(
            team, session_name, index
        )
        if isinstance(msship, Response):
            return msship

        if msship.member == request.user:
            return Response(
                {
                    "detail": f"{request.user}는 {session_name}{index}에 이미 등록된 유저입니다."
                },
                status=status.HTTP_409_CONFLICT,
            )
        msship.member = request.user
        msship.save()

        serializer = self.serializer_class(team)
        return Response(serializer.data)

    def delete(self, request, **kwargs):
        team = self.get_object()
        session_name = request.data.get("session")
        index = request.data.get("index")
        msship = self._get_memberSessionMembershipOrErrorResponse(
            team, session_name, index
        )
        if isinstance(msship, Response):
            return msship

        if msship.member != request.user:
            return Response(
                {
                    "detail": f"{request.user}는 {session_name}{index}에 등록되지 않은 유저입니다."
                },
                status=status.HTTP_409_CONFLICT,
            )
        msship.member = None
        msship.save()

        serializer = self.serializer_class(team)
        return Response(serializer.data)
