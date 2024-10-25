import itertools
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from user.models import CustomUser
from user.serializers import CustomTokenObtainPairSerializer, CustomUserSerializer


class UserListCreateAPIView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser()]
        return [IsAuthenticated()]


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return []
        return [IsAdminUser()]


class RegisterAPIView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if not serializer.is_valid():
            errorDetails = list(itertools.chain(*serializer.errors.values()))
            codes = [errorDetail.code for errorDetail in errorDetails]
            hasConflictError = "unique" in codes
            if hasConflictError:
                return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()

        token = TokenObtainPairSerializer.get_token(user)
        res = serializer.data | {
            "access": str(token.access_token),
            "refresh": str(token),
        }
        return Response(res)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
