"""Profile model."""

#Django
from django.db import models

#Project
from cride.utils.models import CRideModel


class Profile(CRideModel):
    """Profile model.

    A profile holds a user's public data like biography, picture, and stadistics.
    """

    user = models.OneToOneField(
        to = 'users.User', 
        on_delete = models.CASCADE
    )

    picture = models.ImageField(
        'profile picture',
        upload_to = 'users/pictures/',
        blank = True,
        null = True 
    )

    biography = models.TextField(
        max_length = 500,
        blank = True
    )

    #Stats
    rides_taken = models.PositiveIntegerField(
        default = 0
    )

    rides_offered = models.PositiveIntegerField(
        default = 0
    )

    reputation = models.FloatField(
        default = 5.0,
        help_text = 'User\'s reputation based on the rides taken and offered.'
    )

    def __str__(self):
        """Return user's srt representation."""
        return str(self.user)


