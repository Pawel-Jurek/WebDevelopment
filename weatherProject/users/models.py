from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class WeatherSettings(models.Model):
    temp = models.BooleanField(default=True)
    feels_like = models.BooleanField(default=False)
    temp_min = models.BooleanField(default=False)
    temp_max = models.BooleanField(default=False)
    wind = models.BooleanField(default=False)
    clouds = models.BooleanField(default=False)
    pressure = models.BooleanField(default=True)
    main = models.BooleanField(default=True)
    description = models.BooleanField(default=True)

class WeatherAppUser(AbstractUser):
    weather_settings = models.OneToOneField(WeatherSettings, on_delete=models.CASCADE, null=True)


@receiver(post_save, sender=WeatherAppUser)
def create_weather_settings(sender, instance, created, **kwargs):
    if created:
        WeatherSettings.objects.create()
        instance.weather_settings = WeatherSettings.objects.last()
        instance.save()

