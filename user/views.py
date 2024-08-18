from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from user.models import CustomUser
from user.serializers import CustomUserSerializer


class UserListCreateAPIView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
