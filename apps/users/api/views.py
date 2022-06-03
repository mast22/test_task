from rest_framework import viewsets as v
from apps.users.api.serializers import UserSerializer
from apps.users.models import User


class UserViewSet(v.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
