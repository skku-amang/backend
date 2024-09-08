import django_filters
from .models import CustomUser


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = "__all__"
