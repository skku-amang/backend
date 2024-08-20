from typing import Any
from django.urls import get_resolver
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "template/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data()
        resolver = get_resolver()
        url_patterns = resolver.url_patterns
        context["url_patterns"] = url_patterns
        return context
