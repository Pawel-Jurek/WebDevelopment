from django import forms
from .models import WeatherSettings

class WeatherSettingsForm(forms.ModelForm):
    class Meta:
        model = WeatherSettings
        fields = '__all__'