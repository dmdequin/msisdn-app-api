"""
Models for the database.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:  # Require user to enter an email address
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create, save and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User for the API."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()  # assign user manager

    USERNAME_FIELD = 'email'


class MSISD(models.Model):
    """MSISD object."""
    msisdn = models.PositiveIntegerField()
    MNO = models.CharField(max_length=255)
    country_code = models.PositiveIntegerField()
    subscriber_number = models.PositiveIntegerField()
    country_identifier = models.CharField(max_length=255)

    def __str__(self):
        return self.msisdn
