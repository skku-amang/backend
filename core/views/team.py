from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
)
from rest_framework.response import Response
from rest_framework import status

from core.models.session import Session
from core.models.team import Team
from user.models import CustomUser
from core.serializers.team import TeamSerializer
from core.views.filters import TeamFilter


class TeamListCreateAPIView(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filterset_class = TeamFilter


class TeamRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamApplyAPIView(GenericAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def post(self, request, **kwargs):
        # TODO: requestUser = JWT 토큰에서 읽어야 함
        requestUser = CustomUser.objects.all()[0]  # 임시 유저
        team = self.get_object()
        session = Session.objects.get(name=request.data.get("session"))
        ms = team.memberSessions.get(session=session)
        oldMemberList = ms.members.all()
        newMembers = list(oldMemberList)
        if requestUser not in oldMemberList:
            newMembers.append(requestUser)
        else:
            return Response(
                {"detail": "세션에 이미 등록된 유저입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        ms.members.set(newMembers)
        ms.save()

        serializer = self.serializer_class(team)
        return Response(serializer.data)

    def delete(self, request, **kwargs):
        # TODO: requestUser = JWT 토큰에서 읽어야 함
        requestUser = CustomUser.objects.all()[0]  # 임시 유저
        team = self.get_object()
        session = Session.objects.get(name=request.data.get("session"))
        ms = team.memberSessions.get(session=session)
        oldMemberList = ms.members.all()
        newMembers = list(oldMemberList)
        if requestUser in oldMemberList:
            newMembers.remove(requestUser)
        else:
            return Response(
                {"detail": "세션에 등록되지 않은 유저입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        ms.members.set(newMembers)
        ms.save()

        serializer = self.serializer_class(team)
        return Response(serializer.data)
