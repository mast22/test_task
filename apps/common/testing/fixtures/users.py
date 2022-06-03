from django.contrib.auth.models import Permission

from apps.common.utils import random_email
from apps.users.models import User


def create_user(**kwargs) -> User:
    user = User.objects.create(email=random_email(), **kwargs)
    permission = Permission.objects.get(name="Can add post")
    user.user_permissions.add(permission)
    return user
