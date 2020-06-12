from django.urls import path,include
from weatherapp import views

app_name = 'weatherapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('export/',views.export,name='export'),
]
