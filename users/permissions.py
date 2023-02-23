from rest_framework import permissions
from rest_framework.views import View, Request
from users.models import User


class IsOwnerUser(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, user: User) -> bool:
        return request.user == user


class IsSuperUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and request.user.is_superuser


class IsSuperUserToRead(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method not in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and request.user.is_superuser
