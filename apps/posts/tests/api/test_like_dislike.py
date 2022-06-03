from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.common.testing.fixtures.posts import create_post
from apps.common.testing.fixtures.users import create_user
from apps.common.utils import random_string
from apps.users.models import User


class LikeDislikeTestCase(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.post = create_post(self.user)

        self.post_url = reverse("api:post-detail", args=[self.post.id])
        self.like_path = reverse("api:post-like", args=[self.post.id])
        self.dislike_path = reverse("api:post-dislike", args=[self.post.id])

    def request(self, path: str, user: User or None = None):
        if user is not None:
            self.client.force_authenticate(user=self.user)
        return self.client.post(path, {})

    def test_like(self):
        response = self.request(self.like_path, self.user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_like_as_anonymous_user(self):
        response = self.request(self.like_path)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_dislike(self):
        response = self.request(self.dislike_path, self.user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_dislike_as_anonymous(self):
        response = self.request(self.dislike_path)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_like_and_dislike(self):
        response = self.request(self.like_path, self.user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(self.post_url)
        likes = response.data['likes']
        self.assertEqual(likes, 1)

        response = self.request(self.dislike_path, self.user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(self.post_url)
        likes = response.data['likes']
        self.assertEqual(likes, 0)

    def test_dislike_inliked_post(self):
        pass


class UserCanAddPost(APITestCase):
    # Usually I wouldn't write this, but due to unreliable permissions assignment
    # I would rather test it here.
    # In a real project permissions system would be much more sophisticated
    url = reverse("api:post-list")

    def setUp(self):
        self.user = create_user()

    def test_user_add_post(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.url, {"content": random_string()})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
