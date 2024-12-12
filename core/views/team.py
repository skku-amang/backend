from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

from core.models.session import Session
from core.models.team import MemberSession, MemberSessionMembership, Team
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
    def validate_application(team, session, index):
        # session 필드가 없거나 session이 존재하지 않는 경우
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

        # index 필드가 없는 경우
        if index is None:
            return Response(
                {"index": "index 필드는 필수입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 잘못된 index가 입력된 경우
        try:
            ms = team.memberSessions.get(session=session)
        except MemberSession.DoesNotExist:
            return Response(
                {"session": f"{session}는 {team}에 존재하지 않는 session입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        newMemberSessionMemberShipList = ms.members.all()
        try:
            return newMemberSessionMemberShipList.get(index=index)
        except MemberSessionMembership.DoesNotExist:
            return Response(
                {"index": f"{session}{index}는 존재하지 않는 index입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def post(self, request, **kwargs):
        team = self.get_object()
        applications = request.data.get("applications")
        if applications is None:
            return Response(
                {"applications": "applications 필드는 필수입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 각 application에 대해 유효성 검사를 수행
        valid_applications = []
        for application in applications:
            session = application.get("session")
            index = application.get("index")
            msship_or_error_response = self.validate_application(
                team, session, index
            )

            if isinstance(msship_or_error_response, Response):
                return msship_or_error_response
            
            # 이미 본인이 등록된 경우
            if msship_or_error_response.member == request.user:
                return Response(
                    {"detail": f"{request.user}는 {session}{index}에 이미 등록된 유저입니다."},
                    status=status.HTTP_409_CONFLICT,
                )

            # 이미 다른 유저가 등록한 경우
            if msship_or_error_response.member is not None:
                return Response(
                    {"detail": f"{session}{index}는 이미 다른 유저가 등록했습니다."},
                    status=status.HTTP_409_CONFLICT,
                )

            valid_applications.append(msship_or_error_response)

        # 모든 유효성 검사를 통과한 경우
        # TODO: 트랜잭션 처리 -> 실패 시 롤백
        for msship in valid_applications:
            msship.member = request.user
            msship.save()

        serializer = self.serializer_class(team)
        return Response(serializer.data)

    def delete(self, request, **kwargs):
        team = self.get_object()
        session_name = request.data.get("session")
        index = request.data.get("index")
        msship = self.validate_application(team, session_name, index)
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
