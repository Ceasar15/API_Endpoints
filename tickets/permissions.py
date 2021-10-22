from rest_framework import permissions


class isAuthorOrReadOnly(permissions.BasePermission):
# Read only permission is available for all users
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # write permission are only allowed for the author
        return obj.author == request.user


