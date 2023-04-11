from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_super_user(self, email, name, password):
        """Create and save a new superuser"""
        """No necesito pasar self aquí porque ya se pasa una evz cuando se define la función de crear ususario"""
        user = self.create_user(email, name, password)

        """is_superUser se crea automáticamente como uno de los atributos de la clase user gracias a PermissionsMixin"""
        user.is_superuser = True
        iser.is_staff = True
        user.save(using=self._db)

        return user

"""Hay que definir esta clase en settings.py para que se use esta en vez del modelo por defecto que viene con Django"""
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of the user"""
        return self.name

    def get_short_name(self):
        """Retrieve a shorter version of the name"""
        return self.name

    def get_email(self):
        """Retrieve the email"""
        return self.email

    """Esto se hace para que cuando hacemos el toSring del objeto, se nos devuelva un campo representativo"""
    def __str__(self):
        """Retrieve a string representating the user"""
        return self.email