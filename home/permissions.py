from rest_framework import permissions


class NetaPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['create', 'update']:
            return request.user.is_superuser
        elif view.action in ['list', 'retrive']:
            return request.user.is_authenticated
        else:
            return False
