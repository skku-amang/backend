from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

from core.models.session import Session
from core.models.team import Team
from core.serializers.team import TeamSerializer
from core.views.filters import TeamFilter


class TeamListCreateAPIView(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filterset_class = TeamFilter

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser()]
        return [IsAuthenticated()]


class TeamRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAuthenticated()]
        return [IsAdminUser()]


class TeamApplyAPIView(GenericAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        print(request.user)
        team = self.get_object()
        session = Session.objects.get(name=request.data.get("session"))
        ms = team.memberSessions.get(session=session)
        oldMemberList = ms.members.all()
        newMembers = list(oldMemberList)
        if request.user not in oldMemberList:
            newMembers.append(request.user)
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
        print(request.user)
        team = self.get_object()
        session = Session.objects.get(name=request.data.get("session"))
        ms = team.memberSessions.get(session=session)
        oldMemberList = ms.members.all()
        newMembers = list(oldMemberList)
        if request.user in oldMemberList:
            newMembers.remove(request.user)
        else:
            return Response(
                {"detail": "세션에 등록되지 않은 유저입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        ms.members.set(newMembers)
        ms.save()

        serializer = self.serializer_class(team)
        return Response(serializer.data)
