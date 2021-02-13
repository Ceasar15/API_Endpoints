from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from tickets.serializers import UserSerializer, TicketSerializer, CategorySerializer
from django.contrib.auth.models import User
from tickets.models import Ticket, Category

# Create your views here.
