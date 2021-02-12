from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from tutorials.models import Tutorial
from tutorials.serializer import TutorialSerializer
from rest_framework.decorators import api_view


# Create your views here.


