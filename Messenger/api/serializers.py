from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Room, ChatUser, Message


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username']
    
    
class ChatUserSerializer(serializers.ModelSerializer):
  name = UserSerializer()
  class Meta:
    model = ChatUser
    field = ['id', 'name', 'avatar']
    
    
class MessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Message
    fields = ['id', 'author', 'room', 'created_date', 'content']
    

class RoomSerializer(serializers.models):
  class Meta:
    model = Room
    fields = ['id', 'name', 'author', 'created_date', 'users']
    

class RoomUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Room
    fields = ['id', 'users']