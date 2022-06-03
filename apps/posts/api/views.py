from rest_framework import status, viewsets as v
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.posts.api.serializers import PostSerializer
from apps.posts.models.post import Post
from apps.posts.services.like_service import LikeService


class PostViewSet(v.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post: "Post" = self.get_object()
        user: "User" = request.user
        LikeService.like(user, post)

        return Response({}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def dislike(self, request, pk=None):
        post: "Post" = self.get_object()
        user: "User" = request.user
        LikeService.dislike(user, post)

        return Response({}, status=status.HTTP_200_OK)
