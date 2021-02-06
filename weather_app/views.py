from django.shortcuts import render
import requests

# Create your views here.
def index(request):

    city_name= 'Bengaluru'
    url= 'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}&units=metric'.format(
        city_name=city_name, key='107f0bb3a6f90f8c582bfa6d95eda8da'
    )

    response=requests.get(url)
    #print(response)
    #print(response.json())
    myjson=response.json()

    city_weather= {
        'city':city_name,
        'tempreature': myjson.get('main').get('temp'),
        'description': myjson.get('weather')[0].get('description'),
        'icon': myjson.get('weather')[0].get('icon'),
    }
    print(city_weather)
    return render(request,'weather/weather.html')