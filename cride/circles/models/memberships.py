"""Membership model."""

#Django
from django.db import models

#Project
from cride.utils.models import CRideModel



class Membership(CRideModel):
    """Membership model.
    
    A membership model is the table that holds the relationship between a user and a circle.
    """

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    circle = models.ForeignKey('circles.Circle', on_delete=models.CASCADE)

    is_admin = models.BooleanField(
        'circle admin',
        default=False,
        help_text = 'Circle admin can update the circle\'s data and manage its members.'
    )

    #Invitation
    used_invitations = models.PositiveSmallIntegerField(default=0)
    remaining_invitations = models.PositiveSmallIntegerField(default=0)
    invited_by = models.ForeignKey(
        'users.User',
        null = True,
        on_delete = models.SET_NULL,
        related_name = 'invited_by'
    )

    #Stats
    rides_taken = models.PositiveSmallIntegerField(default=0)
    rides_offered = models.PositiveSmallIntegerField(default=0)

    #Status
    is_active = models.BooleanField(
        'active status',
        default = True,
        help_text = 'Only active users are allowed to interact in the circle.'
    )

    def __str__(self):
        """Return username and circle."""

        return '@{} at #{}'.format(
            self.user.username,
            self.circle.slug_name
        )



