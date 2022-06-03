# Generated by Django 4.0.4 on 2022-06-02 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_groups_user_user_permissions_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='registered_on_holiday',
            field=models.BooleanField(default=None, null=True, verbose_name='User was registered on holiday'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='Superuser status'),
        ),
    ]
