from django.shortcuts import render
from rest_framework import generics, routers, serializers, viewsets, permissions
from tickets.serializers import UserSerializer, TicketSerializer, CategorySerializer
from django.contrib.auth.models import User
from tickets.models import Ticket, Category


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def perform_update(self, serializer):
        instance = self.get_object()
        self.request.data.get("title", None)
        if self.request.user.is_authenticated:
            updated_instance = serializer.save(author=self.request.user)
        else:
            updated_instance = serializer.save()

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
