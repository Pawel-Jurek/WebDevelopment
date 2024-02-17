from django.shortcuts import redirect
from django.views.generic import DetailView
from .models import WeatherAppUser
from .forms import WeatherSettingsForm

class WeatherAppUserDetailView(DetailView):
    model = WeatherAppUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['form'] = WeatherSettingsForm(self.request.POST, instance=self.object.weather_settings)
        else:
            context['form'] = WeatherSettingsForm(instance=self.object.weather_settings)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = WeatherSettingsForm(request.POST, instance=self.object.weather_settings)
        if form.is_valid():
            form.save()
            return redirect('index')
        return self.render_to_response(self.get_context_data())