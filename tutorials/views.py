import tutorials
from django.http import request
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from tutorials.models import Tutorial
from tutorials.serializer import TutorialSerializer
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET','POST','DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorial_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorial_serializer.data, safe=False)
    
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 






