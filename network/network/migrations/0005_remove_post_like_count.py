# Generated by Django 4.2.2 on 2023-08-23 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_remove_user_followers_user_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like_count',
        ),
    ]
