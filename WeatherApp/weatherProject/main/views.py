from django.shortcuts import render
import json
import urllib.request
# Create your views here.

def index(request):
    if request.method == "POST":
        city = request.POST.get('city')

        if not city:
            data={"error": "City is required."}
            return render(request, "main/index.html", data)
        
        try:
            source = urllib.request.urlopen(
                'https://api.openweathermap.org/data/2.5/weather?q=' 
                + city + '&units=metric&appid=156310ef9775541a86d266a877a2c8af').read()

            listOfData = json.loads(source)

            data = {
                "city": str(city).capitalize(),
                "country_code": str(listOfData['sys']['country']),
                "temp": str(listOfData['main']['temp']) +' °C',
                "pressure": str(listOfData['main']['pressure']) +' hPa',
                "main": str(listOfData['weather'][0]['main']),
                "description": str(listOfData['weather'][0]['description']),
                "icon": str(listOfData['weather'][0]['icon']),
            }
            print(data)

        except urllib.error.HTTPError as e:
            data={"error": "City not found."}
        
        except json.JSONDecodeError as e:
            data={"error": {e}}

    else:
        data = {}

    return render(request, "main/index.html", data)