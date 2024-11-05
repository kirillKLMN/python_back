from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if username is None:
            raise ValueError('Users must have username')
        if email is None:
            raise ValueError('Users must have email')
        if password is None:
            raise ValueError('Users must have password')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields

        )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, username, password, **extra_fields):
        user = self.create_user(
            email,
            username,
            password,
            is_superuser=True,
            is_staff=True,
            **extra_fields
        )
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    command = models.ForeignKey('main.Command', on_delete=models.CASCADE, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    def __str__(self):
        return self.username
    objects = UserManager()