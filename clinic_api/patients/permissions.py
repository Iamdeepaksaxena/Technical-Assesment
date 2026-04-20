from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsStaffOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        # allow GET (read) for everyone
        if request.method in SAFE_METHODS:
            return True

        # only staff can create/update/delete
        return request.user and request.user.is_staff