from django.http import JsonResponse
from django.shortcuts import render
import json
import urllib.request
from django.conf import settings
import requests
# Create your views here.

def upperEachWord(text):
    words = text.split("+")
    for i in range(len(words)):  
        words[i] = words[i].capitalize()
    return " ".join(words)


def index(request):
    if request.method == "POST":
        postData = request.POST.get('city').replace(" ", "+")
        city = postData.split(",")[0]
        
        if not city:
            data = {"error": "City is required."}
            return render(request, "weatherApp/index.html", {"data": data})
        
        try:
            api_key = settings.WEATHER_API_KEY
            source = urllib.request.urlopen(
                f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}').read()

            listOfData = json.loads(source)

            data = {
                "city": str(upperEachWord(postData)),
                "country_code": str(listOfData['sys']['country']),
                "temp": str(listOfData['main']['temp']) + ' °C',
                "pressure": str(listOfData['main']['pressure']) + ' hPa',
                "main": str(listOfData['weather'][0]['main']),
                "description": str(listOfData['weather'][0]['description']),
                "icon": str(listOfData['weather'][0]['icon']),
            }

        except urllib.error.HTTPError as e:
            data = {"error": "City not found."}
        
        except json.JSONDecodeError as e:
            data = {"error": str(e)}

        return render(request, "weatherApp/index.html", {"data": data})

    else:
        return render(request, "weatherApp/index.html", {"data": {}})
    


def get_city_suggestions(request, input):
    if request.method == 'GET':
        api_key = settings.GOOGLE_API_KEY
        google_api_url = f"https://maps.googleapis.com/maps/api/place/autocomplete/json?key={api_key}&input={input}&types=(cities)"

        try:
            response = requests.get(google_api_url)
            data = response.json()
            predictions = [{'description': prediction['description']} for prediction in data.get('predictions', [])]
            return JsonResponse({'suggestions': predictions})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request'})