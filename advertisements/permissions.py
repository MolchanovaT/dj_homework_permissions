from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение, позволяющее доступ только владельцу объекта для изменения или удаления.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешено только для методов GET, HEAD и OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешить доступ только создателю объекта
        return obj.creator == request.user
