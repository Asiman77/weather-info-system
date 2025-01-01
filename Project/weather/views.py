import requests
from django.shortcuts import render
from django.conf import settings

def get_weather(request):
    api_key = settings.OPENWEATHERMAP_API_KEY
    weather_data = None
    error_message = None

    if request.method == 'POST':
        city = request.POST.get('city')  #
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city_name': data['name'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description'],
            }

        else:
            error_message = "Daxil etdiyiniz bölgə tapılmadı."

    return render(request, 'weather/index.html', {'weather_data': weather_data, 'error_message': error_message})



