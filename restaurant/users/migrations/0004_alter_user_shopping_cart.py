# Generated by Django 4.2.2 on 2023-09-30 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
        ('users', '0003_user_new_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='shopping_cart',
            field=models.ManyToManyField(related_name='shopping_cart', to='orders.order'),
        ),
    ]
