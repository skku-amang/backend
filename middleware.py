import os
from dotenv import load_dotenv
from django.http import HttpResponseRedirect
from django.urls import reverse

load_dotenv(dotenv_path=".env.local")


class CustomAPIKeyOrLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 로그인 URL 예외 처리: 무한루프 방지
        if request.path == reverse("login"):
            return self.get_response(request)

        # API 키 검증
        authorization = request.headers.get("Authorization")
        request_api_key = authorization.split("Api-Key ")[1] if authorization else None
        valid_api_key = os.getenv("DJANGO_API_KEY")
        if request_api_key == valid_api_key:
            return self.get_response(request)

        # 로그인 검증
        if request.user.is_authenticated:
            return self.get_response(request)

        # API 키와 로그인 둘 다 실패한 경우 로그인 페이지로 리다이렉트
        return HttpResponseRedirect(reverse("login"))
