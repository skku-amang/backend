from decimal import Decimal
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from core.models.generation import Generation
from django.contrib.auth import get_user_model

class GenerationTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.generation = Generation.objects.create(order=Decimal("35.5"))

        User = get_user_model()
        # 관리자 사용자 생성
        cls.admin_user = User.objects.create_superuser(
            email="admin@admin.com",
            password="adminpassword",
            name="admin",
            nickname="admin",
            generation=cls.generation
        )

        # 일반 사용자 생성
        cls.normal_user = User.objects.create_user(
            email="user@user.com",
            password="userpassword",
            name="user",
            nickname="user",
            generation=cls.generation,
        )

        # URL 설정
        cls.list_create_url = reverse("generation-list_create")
        cls.detail_url = reverse("generation-retrieve_update_destroy", kwargs={"pk": str(cls.generation.order)})

    def setUp(self):
        self.client = APIClient()
        self.data = {
            "order": "35.0",
            "leader": self.normal_user.id,
        }


    def authenticate(self, user):
        refresh = RefreshToken.for_user(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    def test_list_generations(self):
        self.authenticate(self.normal_user)
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["order"], "35.5")

    def test_create_generation_as_admin(self):
        self.authenticate(self.admin_user)
        response = self.client.post(self.list_create_url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Generation.objects.count(), 2)
        self.assertEqual(response.data["order"], self.data["order"])
        self.assertEqual(response.data["leader"], self.data["leader"])

    def test_create_generation_as_non_admin(self):
        self.client.login(username="user", password="userpassword")
        response = self.client.post(self.list_create_url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_generation(self):
        self.authenticate(self.normal_user)
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["order"], "35.5")

    def test_retrieve_generation_with_invalid_pk(self):
        self.authenticate(self.normal_user)
        invalid_pk_url = reverse("generation-retrieve_update_destroy", kwargs={"pk": "invalid"})
        response = self.client.get(invalid_pk_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_nonexistent_generation(self):
        self.authenticate(self.normal_user)
        nonexistent_detail_url = reverse("generation-retrieve_update_destroy", kwargs={"pk": "99.9"})
        response = self.client.get(nonexistent_detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_generation_as_admin(self):
        self.authenticate(self.admin_user)
        response = self.client.patch(self.detail_url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["order"], self.data["order"])
        self.assertEqual(response.data["leader"], self.data["leader"])

    def test_update_generation_as_non_admin(self):
        self.authenticate(self.normal_user)
        response = self.client.put(self.detail_url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_referenced_generation_raises_bad_request(self):
        self.authenticate(self.admin_user)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_generation_as_non_admin(self):
        self.authenticate(self.normal_user)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
