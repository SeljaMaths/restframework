from rest_framework import permissions


class IsAdminUserReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user and request.user.is_staff


class IsOwneronly(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, post):
        if request.user:
            return post.author == request.user
        return False
