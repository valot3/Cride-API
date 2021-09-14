"""
Invitations permissions.
"""

#Django REST Framework
from rest_framework.permissions import BasePermission



# class IsSelfMember(BasePermission):
#     """
#     Allow access only to the owner of the invitations.
#     """

#     def has_permission(self, request, view):
#         """
#         Check if the obj owner are the same that the requesting user.
#         """

#         obj = view.get_object()

#         return request.user == obj.user #Bool


class IsSelfMember(BasePermission):
    """
    Allow access only to the owner of the invitations.
    """

    def has_permission(self, request, view):
        """
        Get the object and then call to `has_object_permission`.
        """
        obj = view.get_object()

        return self.has_object_permission(request, view, obj)

    
    def has_object_permission(self, request, view, obj):
        """
        Check if the obj owner are the same that the requesting user.
        """
        return request.user == obj.user

