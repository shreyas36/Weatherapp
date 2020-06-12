from django import forms
from .models import City

class CityForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'class':'form-control mr-sm-2','placeholder':'Search'}))
    class Meta:
        model = City
        fields = ['name']
