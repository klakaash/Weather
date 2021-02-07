from django.shortcuts import render,redirect
import requests
from .models import City 
from .forms import CityForm
# Create your views here.
def index(request):

    cities= City.objects.all()
    er_msg=''
    message=''
    message_class=''
    #city_name= 'Delhi'
    if request.method =='POST':
        form= CityForm(request.POST)

        if form.is_valid():

            new_city=form.cleaned_data['city_name']
            existing_city_count= City.objects.filter(city_name=new_city).count()

            if(existing_city_count==0):
                url= 'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}&units=metric'.format(
                city_name=new_city, key='107f0bb3a6f90f8c582bfa6d95eda8da'
                )
                response=requests.get(url)
                myjson=response.json()
                
                if (myjson.get('cod')==200):
                    form.save()
                else:
                    er_msg='City does not exist'
            else:
                er_msg='City already exists in DB'
        if er_msg:
            message=er_msg
            message_class= 'is-danger'
        else:
            message= 'City added successfully '
            message_class='is-success'


    print(er_msg)
    form = CityForm()   
    weather_data=[]

    for city in cities :
        url= 'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}&units=metric'.format(
        city_name=city, key='107f0bb3a6f90f8c582bfa6d95eda8da'
        )

        response=requests.get(url)
        #print(response)
        #print(response.json())
        myjson=response.json()
        #print(myjson)

        city_weather= {
            'city':city.city_name,
            'tempreature': myjson.get('main',{}).get('temp'),
            'description': myjson.get('weather')[0].get('description'),
            'icon': myjson.get('weather')[0].get('icon'),
        }

        weather_data.append(city_weather)

    #print(weather_data)
    #print(city_weather)
    context= {
        'weather_data':weather_data, 
        'form':form ,
        'message':message,
        'message_class':message_class
        }
    return render(request,'weather/weather.html',context)

def delete_city(request,city_name):
    City.objects.get(city_name=city_name).delete()
    print('success deletion')


    return redirect('home')