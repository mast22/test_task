from django.contrib.auth.base_user import BaseUserManager
from django.db import models as m
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as __


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_superuser(self, email, password):
        user = self.model(email=email, is_superuser=True)
        user.set_password(password)
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = m.EmailField(__('Email'), unique=True)
    is_superuser = m.BooleanField(__('Superuser status'), default=False)
    registered_on_holiday = m.BooleanField(__("User was registered on holiday"), null=True, default=None)
    country = m.CharField(max_length=100, null=True, default=None)  # TODO choices field

    USERNAME_FIELD = 'email'
    objects = UserManager()
