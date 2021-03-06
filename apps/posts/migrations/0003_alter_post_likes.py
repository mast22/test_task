# Generated by Django 4.0.4 on 2022-05-31 21:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_like_alter_post_likes_like_post_like_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='liked_posts', through='posts.Like', to=settings.AUTH_USER_MODEL),
        ),
    ]
