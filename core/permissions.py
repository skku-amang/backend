from rest_framework.permissions import BasePermission


class IsTeamLeaderOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.leader.id == request.user.id
