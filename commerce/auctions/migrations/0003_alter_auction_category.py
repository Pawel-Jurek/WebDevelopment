# Generated by Django 4.2.2 on 2023-07-05 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auction_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auctionCategory', to='auctions.category'),
        ),
    ]