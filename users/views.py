from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.parsers import JSONParser
from rest_framework import status, viewsets, generics

from rest_framework.decorators import api_view

from ..users.serializers import UserSerializer
# from users.models import Profile
# from users.serializers import ProfileSerialzer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
# Create your views here.




# @api_view(['GET'])
# def profile(request):
#     if request.method == 'GET':
#         profile = Profile.objects.all()

#         bio = request.query_params.get('bio', None)
#         if profile is not None:
#             profile = profile.filter(bio__icontains=bio) 
        
#         profile_serialzer = ProfileSerialzer(profile, many=True)
#         return JsonResponse(profile_serialzer.data, safe=False)
#     else:
#         return render(status = status.HTTP_400_BAD_REQUEST)

# class ProfileAPIView(APIView):
#     authentication_classes = (SessionAuthentication, TokenAuthentication, )
    
#     def get_queryset(self):
#         return Profile.objects.all()
    
#     def get(self, request, *args, **kwargs):
#         print(request.user)
#         profile = Profile.objects.all()
#         bio = request.query_params.get("bio", None)
#         if profile is not None:
#             profile = profile.filter(bio__icontains=bio) 
#         profile_serialzer = ProfileSerialzer(profile, many=True)
#         return Response(profile_serialzer.data)
        


# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerialzer
    