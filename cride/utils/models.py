from django.db import models


class CRideModel(models.Model):
    """Comparte Ride base model.
    
    CRideModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created_at[DateTime]: Store the datetime the object was created.
        + modified_at[DateTime]: Store the last datetime the object was modified.
    """

    created_at = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )

    modified_at = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        """Meta definition for CRideModel."""

        abstract=True
        get_latest_by='created'
        ordering=['-created_at', '-modified_at']
        
