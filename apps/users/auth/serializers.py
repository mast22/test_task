from rest_framework import serializers as s
from rest_framework.exceptions import ValidationError


class SignUpSerializer(s.Serializer):
    email = s.EmailField() # validates email
    password = s.CharField()
    password_again = s.CharField()

    def validate(self, attrs):
        if attrs['password'] != attrs['password_again']:
            raise ValidationError("passwords must match")
        return attrs


class SignUpRespSerializer(s.Serializer):
    result = s.CharField()
