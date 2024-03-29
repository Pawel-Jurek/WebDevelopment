# Generated by Django 4.2.2 on 2023-07-08 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_auction_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auctionAutor', to=settings.AUTH_USER_MODEL),
        ),
    ]
