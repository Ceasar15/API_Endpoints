from rest_framework import serializers

from django.contrib.auth.models import User
from tickets.models import Ticket, Category

# Serializers define the API 
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'title', 'ticket_id', 'user', 'content', 'category', 'created', 'modified')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')
    
