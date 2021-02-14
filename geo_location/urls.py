from django.conf.urls import url
from django.urls import path
from geo_location import views


urlpatterns = [
    path('home/', views.home, name='home')
]


