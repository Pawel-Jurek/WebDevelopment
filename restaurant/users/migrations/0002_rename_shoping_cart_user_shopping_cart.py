# Generated by Django 4.2.2 on 2023-09-30 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='shoping_cart',
            new_name='shopping_cart',
        ),
    ]
