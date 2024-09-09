import django_filters
from .models import CustomUser


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        exclude = ["profileImage"]
        fields = "__all__"
