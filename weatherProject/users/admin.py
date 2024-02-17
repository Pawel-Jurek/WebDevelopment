from django.contrib import admin
from .models import WeatherAppUser, WeatherSettings



@admin.register(WeatherAppUser)
class WeatherAppUserAdmin(admin.ModelAdmin):
    pass

@admin.register(WeatherSettings)
class WeatherSettingsAdmin(admin.ModelAdmin):
    pass