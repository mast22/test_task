from rest_framework.exceptions import APIException


class SameUserAlreadyExistsException(APIException):
    status_code = 400
    default_detail = 'User with this email already exists'
    default_code = 'user_already_exists'


class PasswordsDontMatch(APIException):
    status_code = 400
    default_detail = 'Passwords don\'t match'
    default_code = 'passwords_dont_match'
