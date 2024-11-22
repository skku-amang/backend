from decimal import Decimal
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from core.models.performance import Performance
from core.models.feedback import Feedback
from core.models.generation import Generation
from django.contrib.auth import get_user_model


class FeedbackTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        performance_data = {
            'name': 'Test Performance',
            'description': 'Test Description',
            'location': 'Test Location',
            'startDatetime': '2024-11-17T10:00:00Z',
            'endDatetime': '2024-11-17T12:00:00Z'
        }
        cls.performance = Performance.objects.create(**performance_data)
        data = {
            'performance': cls.performance,
            'startDatetime': '2024-11-17T10:00:00Z',
            'endDatetime': '2024-11-18T12:00:00Z'
        }
        cls.feedback = Feedback.objects.create(**data)
        generation = Generation.objects.create(order=Decimal("35.5"))

        User = get_user_model()
        # 관리자 사용자 생성
        cls.admin_user = User.objects.create_superuser(
            email="admin@admin.com",
            password="adminpassword",
            name="admin",
            nickname="admin",
            generation=generation
        )

        # 일반 사용자 생성
        cls.normal_user = User.objects.create_user(
            email="user@user.com",
            password="userpassword",
            name="user",
            nickname="user",
            generation=generation,
        )

        # URL 설정
        cls.list_create_url = reverse("feedback-list_create")
        cls.retrieve_update_destroy_url = reverse("feedback-retrieve_update_destroy", kwargs={"pk": str(cls.feedback.id)})

    def setUp(self):
        self.client = APIClient()
        self.data = {
            'performanceId': self.performance.id,
            'startDatetime': '2024-11-17T10:00:00Z',
            'endDatetime': '2024-11-17T12:00:00Z'
        }


    def authenticate(self, user):
        refresh = RefreshToken.for_user(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    def test_admin_create_feedback(self):
        self.authenticate(self.admin_user)
        new_performance_data = {
            'name': 'Test Performance2',
            'description': 'Test Description2',
            'location': 'Test Location2',
            'startDatetime': '2024-11-17T10:00:00Z',
            'endDatetime': '2024-11-17T12:00:00Z'
        }
        new_performance = Performance.objects.create(**new_performance_data)
        self.data['performanceId'] = new_performance.id
        response = self.client.post(self.list_create_url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feedback.objects.count(), 2)
    
    def test_normal_user_create_feedback_raises_forbidden(self):
        self.authenticate(self.normal_user)
        response = self.client.post(self.list_create_url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Feedback.objects.count(), 1)

    def test_retrieve_feedback(self):
        self.authenticate(self.normal_user)
        response = self.client.get(self.retrieve_update_destroy_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['performance']['id'], self.performance.id)

    def test_update_feedback(self):
        self.authenticate(self.admin_user)
        updated_data = {
            'performanceId': self.performance.id,
            'startDatetime': '2024-11-18T10:00:00Z',
            'endDatetime': '2024-11-18T12:00:00Z'
        }
        response = self.client.put(self.retrieve_update_destroy_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['performance']['id'], self.performance.id)
    
    def test_normal_user_update_feedback_raises_forbidden(self):
        self.authenticate(self.normal_user)
        updated_data = {
            'performanceId': self.performance.id,
            'startDatetime': '2024-11-18T10:00:00Z',
            'endDatetime': '2024-11-18T12:00:00Z'
        }
        response = self.client.put(self.retrieve_update_destroy_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_feedback(self):
        self.authenticate(self.admin_user)
        response = self.client.delete(self.retrieve_update_destroy_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Feedback.objects.count(), 0)

    def test_normal_user_delete_feedback_raises_forbidden(self):
        self.authenticate(self.normal_user)
        response = self.client.delete(self.retrieve_update_destroy_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Feedback.objects.count(), 1)
