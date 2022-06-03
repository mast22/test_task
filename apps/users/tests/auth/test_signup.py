from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.common.utils import random_string, random_email
from apps.users.models import User


class SignUpTestCase(APITestCase):
    url = reverse('api:auth:signup')
    password_1 = random_string()
    password_2 = random_string()
    email = random_email()

    def test_signup(self):
        data = {
            'email': self.email,
            'password': self.password_1,
            'password_again': self.password_1
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_signup_same_email(self):
        data = {
            'email': self.email,
            'password': self.password_1,
            'password_again': self.password_1
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_different_passwords(self):
        data = {
            'email': self.email,
            'password': self.password_1,
            'password_again': self.password_2
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_setup_correctly(self):
        data = {
            'email': self.email,
            'password': self.password_1,
            'password_again': self.password_1
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(email=self.email)
        result = user.check_password(self.password_1)
        self.assertTrue(result)

    def test_user_can_login(self):
        data = {
            'email': self.email,
            'password': self.password_1,
            'password_again': self.password_1
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        token_url = reverse("api:auth:token_obtain_pair")
        response = self.client.post(token_url, {
            "email": self.email,
            "password": self.password_1
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
