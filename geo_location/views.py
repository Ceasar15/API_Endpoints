from django.http import response
from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    response = requests.get('http://freegeoip.net/json')
    geodata = response.json()
    context = {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    }
    return render(request, 'core/home', context)

