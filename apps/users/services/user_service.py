from datetime import datetime

from django.contrib.auth.models import Permission

from apps.users.exceptions import SameUserAlreadyExistsException, PasswordsDontMatch
from apps.users.models import User
from apps.users.tasks import set_user_country_and_registered_on_holiday


class UserService:
    @staticmethod
    def register_user(email: str, client_ip: str, password_1: str, password_2: str):
        same_email_user_exists = User.objects.filter(email=email).exists()

        if password_1 != password_2:
            raise PasswordsDontMatch()

        if same_email_user_exists:
            raise SameUserAlreadyExistsException()

        user = User(email=email)
        user.set_password(password_1)
        user.save()
        permission = Permission.objects.get(name="Can add post")
        user.user_permissions.add(permission)
        date = datetime.now()
        year = date.year
        month = date.month
        day = date.day

        set_user_country_and_registered_on_holiday.send(user.id, client_ip, year, month, day)
