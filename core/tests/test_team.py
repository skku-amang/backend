from decimal import Decimal
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from core.models.session import Session
from core.models.performance import Performance
from core.models.generation import Generation
from core.models.team import MemberSession, MemberSessionMembership, Team
from django.contrib.auth import get_user_model


class TeamTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # 공연 생성
        performance_data = {
            "name": "Test Performance",
            "description": "Test Description",
            "location": "Test Location",
            "startDatetime": "2024-11-17T10:00:00Z",
            "endDatetime": "2024-11-17T12:00:00Z",
        }
        cls.performance = Performance.objects.create(**performance_data)

        # 기수 생성
        generation = Generation.objects.create(order=Decimal("35.5"))

        User = get_user_model()
        # 관리자 사용자 생성
        cls.admin_user = User.objects.create_superuser(
            email="admin@user.com",
            password="adminpassword",
            name="admin",
            nickname="admin",
            generation=generation,
        )

        # 다른 팀 소속의 일반 사용자 생성
        cls.other_team_normal_user = User.objects.create_user(
            email="user@user.com",
            password="userpassword",
            name="user",
            nickname="user",
            generation=generation,
        )

        # 팀장 생성
        cls.leader = User.objects.create_user(
            email="leader@user.com",
            password="leaderpassword",
            name="leader",
            nickname="leader",
            generation=generation,
        )

        data = {
            "name": "Test Team",
            "description": "Test Description",
            "leader": cls.leader,
            "performance": cls.performance,
            "isFreshmenFixed": True,
            "isSelfMade": False,
            "posterImage": None,
            "songName": "Test Song",
            "songArtist": "Test Artist",
            "songYoutubeVideoUrl": "vNePhmCMnbU",  # do you like beaver?
        }
        cls.team = Team.objects.create(**data)
        ms = MemberSession.objects.create(
            team=cls.team, session=Session.objects.create(name="보컬")
        )
        MemberSessionMembership.objects.create(
            memberSession=ms, member=cls.leader, index=0
        )
        MemberSessionMembership.objects.create(memberSession=ms, member=None, index=1)
        MemberSessionMembership.objects.create(memberSession=ms, member=None, index=2)

        # URL 설정
        cls.list_create_url = reverse("team-list_create")
        cls.retrieve_update_destroy_url = reverse(
            "team-retrieve_update_destroy", kwargs={"pk": str(cls.team.id)}
        )
        cls.apply_url = reverse("team-apply", kwargs={"pk": str(cls.team.id)})

    def setUp(self):
        self.client = APIClient()
        self.data = {
            "performanceId": self.performance.id,
            "startDatetime": "2024-11-17T10:00:00Z",
            "endDatetime": "2024-11-17T12:00:00Z",
        }

    def authenticate(self, user):
        refresh = RefreshToken.for_user(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    def test_retrieve_team(self):
        self.authenticate(self.other_team_normal_user)
        response = self.client.get(self.retrieve_update_destroy_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["performance"]["id"], self.performance.id)
        self.assertEqual(response.data["leader"]["id"], self.leader.id)

    def test_other_team_normal_user_update_team_raises_forbidden(self):
        self.authenticate(self.other_team_normal_user)
        updated_data = {"name": "edited team name"}
        response = self.client.put(
            self.retrieve_update_destroy_url, updated_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_team(self):
        self.authenticate(self.admin_user)
        response = self.client.delete(self.retrieve_update_destroy_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Team.objects.count(), 0)

    def test_other_team_normal_user_delete_team_raises_forbidden(self):
        self.authenticate(self.other_team_normal_user)
        response = self.client.delete(self.retrieve_update_destroy_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Team.objects.count(), 1)

    def test_apply_team(self):
        self.authenticate(self.other_team_normal_user)
        session = "보컬"
        index = 1
        response = self.client.post(
            self.apply_url,
            {"applications": [{"session": session, "index": index}]},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        vocalMemberSession = None
        for ms in response.data["memberSessions"]:
            if ms["session"] == session:
                vocalMemberSession = ms
                break
        self.assertEqual(vocalMemberSession["session"], session)
        self.assertEqual(
            vocalMemberSession["members"][index]["id"], self.other_team_normal_user.id
        )

    def test_apply_team_with_bulk(self):
        self.authenticate(self.other_team_normal_user)
        session = "보컬"
        index = 1
        response = self.client.post(
            self.apply_url,
            {
                "applications": [
                    {"session": session, "index": index},
                    {"session": session, "index": index + 1},
                ]
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        vocalMemberSession = None
        for ms in response.data["memberSessions"]:
            if ms["session"] == session:
                vocalMemberSession = ms
                break
        self.assertEqual(vocalMemberSession["session"], session)
        self.assertEqual(
            vocalMemberSession["members"][index]["id"], self.other_team_normal_user.id
        )
        self.assertEqual(
            vocalMemberSession["members"][index + 1]["id"],
            self.other_team_normal_user.id,
        )

    def test_apply_team_with_invalid_session(self):
        self.authenticate(self.other_team_normal_user)
        session = "보컬2"
        index = 1
        response = self.client.post(
            self.apply_url,
            {"applications": [{"session": session, "index": index}]},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data["session"], f"{session}는 존재하지 않는 session 입니다."
        )

    def test_apply_team_with_invalid_index(self):
        self.authenticate(self.other_team_normal_user)
        session = "보컬"
        index = 3
        response = self.client.post(
            self.apply_url,
            {"applications": [{"session": session, "index": index}]},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_apply_team_with_already_registered_user(self):
        self.authenticate(self.other_team_normal_user)
        session = "보컬"
        index = 0
        response = self.client.post(
            self.apply_url,
            {"applications": [{"session": session, "index": index}]},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
