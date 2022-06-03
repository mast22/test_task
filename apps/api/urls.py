from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.posts.api import views as posts_views
from apps.users.api import views as users_views

from apps.users.auth import urls as auth_urls


router = DefaultRouter()
router.register('posts', posts_views.PostViewSet)
router.register('users', users_views.UserViewSet)

app_name = 'api'
urlpatterns = [
    path('auth/', include(auth_urls, namespace='auth')),
] + router.urls
