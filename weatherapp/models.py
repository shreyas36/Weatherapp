from django.db import models
from datetime import datetime
# Create your models here.

class City(models.Model):
    # TODO: Define fields here
    name = models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='cities'

class CityWeather(models.Model):
    # TODO: Define fields here
    city = models.CharField(max_length=100)
    temperature = models.FloatField(max_length=10)
    pressure = models.FloatField(max_length=10)
    windspeed = models.FloatField(max_length=10)
    humidity = models.FloatField(max_length=10)
    description = models.CharField(max_length=50)
    icon = models.SlugField(null=True)
    date = models.DateTimeField(default=datetime.now()) 
    def __str__(self):
        return self.city
