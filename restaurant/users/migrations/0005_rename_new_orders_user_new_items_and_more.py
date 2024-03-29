# Generated by Django 4.2.2 on 2023-10-01 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_order_completed_remove_order_user_and_more'),
        ('users', '0004_alter_user_shopping_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='new_orders',
            new_name='new_items',
        ),
        migrations.RemoveField(
            model_name='user',
            name='shopping_cart',
        ),
        migrations.AddField(
            model_name='user',
            name='orders',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orders.order'),
        ),
    ]
