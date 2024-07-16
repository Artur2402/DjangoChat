import os

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import Room, ChatUser, Message
from .serializers import ChatUserSerializer, RoomSerializer, UserSerializer, MessageSerializer

class AllUsersView(generics.ListAPIView):
  queryset = User.objects.order_by('-last_login')
  serializer_class = UserSerializer


class AllChatUsersView(generics.ListAPIView):
  queryset = ChatUser.objects.order_by('-name__last_login')
  serializer_class = ChatUserSerializer
  
    
class ChangeChatUserView(generics.UpdateAPIView):
  queryset = ChatUser.objects.all()
  serializer_class = ChatUserSerializer
  parser_classes = [MultiPartParser, FormParser]
  
  def put(self, request, pk):
    chat_user = self.get_object()
    user = User.objects.get(pk=chat_user.name.pk)
    user.username = request.data['name']
    user.save()
    chat_user.avatar = request.data['avatar']
    chat_user.save()
    return Response({'message': 'Profile is changed'})
  

class AllRoomView(generics.ListCreateAPIView):
  queryset = Room.objects.all()
  serializer_class = RoomSerializer
  
  
class RoomView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Room.objects.all()
  serializer_class = RoomSerializer
  
  def put(self, request, pk):
    room = self.get_object()
    guests = request.data['users']
    room.users.set(guests)
    room.save()
    return Response({'message': 'Some guests are changed'})
  
  
class AllMessageView(generics.ListCreateAPIView):
  queryset = Message.objects.order_by('-created_date')
  serializer_class = MessageSerializer