"""Circle permission classes."""

#Django REST Framework
from rest_framework.permissions import BasePermission

#Project
from cride.circles.models import Membership


class IsCircleAdmin(BasePermission):
    """Allow access only to the circle admins."""

    def has_object_permission(self, request, view, obj):
        """Verify if the user have a membership in the object and if is admin."""

        try:
            Membership.objects.get(
                user = request.user,
                circle = obj,
                is_admin = True,
                is_active = True
            )
        except Membership.DoesNotExist:
            return False


        return True
