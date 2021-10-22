from django.urls import path, include 

from django.contrib.auth.models import User
from rest_framework import routers
from rest_framework import urlpatterns
from tickets.views import UserViewSet, TicketViewSet,  CategoryViewSet

router = routers.DefaultRouter()

router.register(r'api/users', UserViewSet)

router.register(r'api/tickets', TicketViewSet)
router.register(r'api/tickets/update', TicketViewSet) 
router.register(r'api/category', CategoryViewSet)


urlpatterns = [
    path(r'', include(router.urls)),
]

