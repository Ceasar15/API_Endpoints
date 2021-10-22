"""API_Endpoints URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('tutorials.urls')),
    url(r'^', include('tickets.urls')),
    url(r'^', include('users.urls')),
    url(r'^', include('geo_location.urls')),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/', include('rest_auth.urls')),
    path('api/auth/reg/', include('rest_auth.registration.urls'))
]
