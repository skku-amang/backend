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
    TokenRefreshView,
)
from rest_framework import status
from rest_framework.response import Response
from user.models import CustomUser
from user.serializers import CustomTokenObtainPairSerializer, CustomUserSerializer


class UserListCreateAPIView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class RegisterAPIView(APIView):
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
