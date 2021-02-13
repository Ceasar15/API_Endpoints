from django.urls import path, include 

from django.contrib.auth.models import User
from rest_framework import routers

from tickets.models import Ticket, Category
from tickets.views import UserViewSet, TicketViewSet, CategoryViewSet

