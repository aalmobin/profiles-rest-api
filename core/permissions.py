from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow User is trying to edit their own Profile"""

    def has_object_permission(self, request, view, obj):
        """Check User is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnfeed(permissions.BasePermission):
    """Allow User is trying to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check User is trying to Update their own status"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
