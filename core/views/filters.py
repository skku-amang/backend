import django_filters
from core.models import Generation


class GenerationFilter(django_filters.FilterSet):
    order = django_filters.NumberFilter()
    leader = django_filters.CharFilter()

    class Meta:
        model = Generation
        fields = "__all__"
