from apps.common.utils import random_string
from apps.posts.models import Post


def create_post(owner: "User", **kwargs) -> Post:
    return Post.objects.create(content=random_string(), owner=owner, **kwargs)
