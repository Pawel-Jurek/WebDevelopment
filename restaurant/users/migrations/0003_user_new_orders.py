# Generated by Django 4.2.2 on 2023-09-30 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_shoping_cart_user_shopping_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='new_orders',
            field=models.IntegerField(default=0),
        ),
    ]
