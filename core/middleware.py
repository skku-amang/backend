from django.http import HttpResponseForbidden
from django.core.cache import cache
from django.conf import settings


class BlockIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")
        if cache.get(ip):
            return HttpResponseForbidden("blocked")

        response = self.get_response(request)

        if response.status_code == 404 and request.path.endswith(".php"):
            attempts = cache.get(ip, 0) + 1
            cache.set(ip, attempts, timeout=36000)  # 10시간 동안 유지
            if attempts > 5:  # 5번 이상 404 에러 발생 시 차단
                cache.set(ip, True, timeout=36000)  # 10시간 동안 차단

        return response


class APIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ELB health check
        if request.path == "/":
            return self.get_response(request)

        api_key = request.headers.get("X-API-KEY")

        # API 키 확인
        if api_key not in settings.API_KEYS:
            return HttpResponseForbidden("Invalid API Key")

        # API 키가 유효한 경우 요청 처리
        return self.get_response(request)
