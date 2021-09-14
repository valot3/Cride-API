"""Circles permission classes."""

#Django REST Framework
from rest_framework.permissions import BasePermission

#Project
from cride.circles.models import Membership



class IsActiveCircleMember(BasePermission):
    """Allow access only to circle members.
    
    Expect that the views implementing this permission
    have a 'circle' attribute assigned.
    """


    def has_permission(self, request, view):
        """Verify user is an active member of the circle."""

        try:
            Membership.objects.get(
                user = request.user,
                circle = view.circle,
                is_active = True
            )
        except Membership.DoesNotExist:
            return False
        
        
        return True 


class IsAdminOrMembershipOwner(BasePermission):
    """
    Allow access to the membership only to Admin users
    or membership owners.
    """

    def has_permission(self, request, view):
        membership = view.get_object()

        #If requesting user is the membership owner, return true.
        if membership.user == request.user:
            return True
        
        #else
        #Verify if the requesting user is an admin of the circle. 
        try:
            Membership.objects.get(
                circle = view.circle,
                user = request.user,
                is_active = True,
                is_admin = True
            )
        except Membership.DoesNotExist:
            return False
        
        return True
           
    
    
        
