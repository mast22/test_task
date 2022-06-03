from rest_framework import serializers as s

from apps.users.models import User


class UserSerializer(s.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
