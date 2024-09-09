import os
from dotenv import load_dotenv
from django.http import JsonResponse

load_dotenv(dotenv_path=".env.local")


class CustomAPIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        authorization = request.headers.get("Authorization")
        requestAPIKey = authorization.split("Api-Key ")[1] if authorization else None
        if requestAPIKey is None:
            return JsonResponse({"detail": "API KEY 가 필요합니다."}, status=401)
        if requestAPIKey != os.getenv("DJANGO_API_KEY"):
            return JsonResponse({"detail": "유효하지 않은 API KEY 입니다."}, status=401)

        return self.get_response(request)
