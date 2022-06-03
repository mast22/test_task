from django.db.models import QuerySet
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from ipware import get_client_ip

from apps.users.auth.serializers import SignUpSerializer, SignUpRespSerializer
from apps.users.services.user_service import UserService


class SignupView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer

    def get_queryset(self):
        return QuerySet().none()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password_1 = serializer.validated_data['password']
        password_2 = serializer.validated_data['password_again']
        client_ip, _ = get_client_ip(request)
        UserService.register_user(email, client_ip, password_1, password_2)
        return Response(SignUpRespSerializer({"result": "done"}).data, status=status.HTTP_201_CREATED)
