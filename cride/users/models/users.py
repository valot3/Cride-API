"""Users model."""

#Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

#Project
from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):
    """User model.
    
    Extends from Django's AbstractUser class, changing the username field
    to email and some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique = True,
        error_messages = {'unique': 'The email entered is already in use.'}
    )

    phone_regex = RegexValidator(
        regex = r'\+?1?\d{9,15}$',
        message = 'Phone number must be entered in the format +999999999. Up to 15 digits allowed.'
    )
    phone_number = models.CharField(
        'phone number',
        validators = [phone_regex],
        max_length = 17,
        blank = True
    )

    is_client = models.BooleanField(
        'client status',
        default = True,
        help_text = (
            'Help easily distinguish users and perform queries.'
            'Clients are the main types of user.'
        )
    )

    is_verified = models.BooleanField(
        'verified status',
        default = False,
        help_text = 'Set to true when the user have verified its email address.'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']


    def __str__(self):
        """Return the username."""
        return self.username

    def get_short_name(self):
        """Return the username."""
        return self.username