import django_filters
from core.models import Generation
from core.models.performance import Performance
from core.models.session import Session
from core.models.team import Team


class GenerationFilter(django_filters.FilterSet):
    class Meta:
        model = Generation
        fields = "__all__"


class PerformanceFilter(django_filters.FilterSet):
    class Meta:
        model = Performance
        fields = "__all__"


class SessionFilter(django_filters.FilterSet):
    class Meta:
        model = Session
        fields = "__all__"


class TeamFilter(django_filters.FilterSet):
    class Meta:
        model = Team
        fields = "__all__"
