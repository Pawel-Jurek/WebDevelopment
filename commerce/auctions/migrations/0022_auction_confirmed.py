# Generated by Django 4.2.2 on 2023-07-12 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_alter_auction_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]