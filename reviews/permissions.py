from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReviewPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(obj.user == request.user or request.user.is_staff)
