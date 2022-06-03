from django.db import models as m


class Post(m.Model):
    content = m.TextField()
    likes = m.ManyToManyField("users.User", related_name='liked_posts', through='posts.Like')
    owner = m.ForeignKey("users.User", on_delete=m.CASCADE, related_name='posts')

    def __str__(self):
        return self.content[:20]
