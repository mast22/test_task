from rest_framework import serializers as s
from rest_framework.fields import CurrentUserDefault

from apps.posts.models.post import Post


class PostSerializer(s.ModelSerializer):
    likes = s.ReadOnlyField(source='likes.count')
    owner = s.HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'
