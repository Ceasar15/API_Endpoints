from django.http import response
from django.shortcuts import render
import requests
import json

# Create your views here.

def home(request):
    response = requests.get('http://freegeoip.app/json')
    geodata = response.json()
    context = {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    }
    return render(request, 'geo_location/core/home', context)

