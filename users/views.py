from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer