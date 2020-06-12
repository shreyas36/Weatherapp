from django.shortcuts import render
import requests
from .forms import CityForm
from django.http import HttpResponse
from .models import City,CityWeather
import csv
# Create your views here.
def index(request):
    city='mumbai'
    cities= City.objects.all()
    #login in openweathermap for API id in url
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=d2aa5742ef4800a4fceabd18c2483bc2'
    if request.method == 'POST':
        #print(request.POST.dict()['name'])
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()

    form = CityForm()


    weather_list=[]

    for city in cities:

        r= requests.get(url.format(city)).json()
        #print(r)
        city_weather = {
            'city':r['name'],
            'temperature':round(r['main']['temp']-273.15,2),
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
            'humidity':r['main']['humidity'],
            'pressure':r['main']['pressure'],
            'windspeed':r['wind']['speed']
        }
        new_values = CityWeather(**city_weather)
        new_values.save()
        weather_list.append(city_weather)
    context_dict  = {'weather_list':weather_list,'form':form}
    return  render(request, 'weatherapp/weather.html',context=context_dict)


def export(request):
    response = HttpResponse()
    writer = csv.writer(response)
    writer.writerow(['date','city','temperature','description','humidity','pressure','windspeed'])
    for city in CityWeather.objects.all().values_list('date','city','temperature','description','humidity','pressure','windspeed'):
        writer.writerow(city)

    response['Content-Disposition']='attachment;filename="weatherhistory.csv"'
    return response
