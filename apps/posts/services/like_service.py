from apps.posts.models import Like


class LikeService:
    @staticmethod
    def like(user: "User", post: "Post") -> int:
        post.likes.add(user)

    @staticmethod
    def dislike(user: "User", post: "Post"):
        Like.objects.filter(user=user, post=post).delete()