# Generated by Django 4.2.2 on 2023-10-01 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_order_completed_remove_order_user_and_more'),
        ('users', '0006_rename_new_items_user_new_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='orders',
        ),
        migrations.AddField(
            model_name='user',
            name='orders',
            field=models.ManyToManyField(related_name='orders', to='orders.order'),
        ),
    ]
