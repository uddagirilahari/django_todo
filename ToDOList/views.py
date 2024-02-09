from django.shortcuts import render
from rest_framework import generics

from ToDOList.serializers import TodoSerializer

from .models import *

class ListTodo(generics.ListAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer

class CreateTodo(generics.CreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer

class DeleteTodo(generics.DestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer