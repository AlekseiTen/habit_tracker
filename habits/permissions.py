from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Пользовательское разрешение, позволяющее редактировать объект только его владельцу.
    """

    def has_object_permission(self, request, view, obj):
        # Проверяем, является ли пользователь владельцем объекта
        return request.user == obj.user
