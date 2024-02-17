# Generated by Django 4.2.2 on 2024-02-16 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weatherappuser',
            name='settings',
        ),
        migrations.AddField(
            model_name='weatherappuser',
            name='weather_settings',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.weathersettings'),
        ),
    ]
