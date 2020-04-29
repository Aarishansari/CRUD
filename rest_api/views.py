from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
#from rest_framework.views import APIView
#from rest_framework.response import Response
from rest_framework import viewsets
from .models import users
from .serializers import usersSerializer

class userViewSet(viewsets.ModelViewSet):
     queryset = users.objects.all().order_by('Name')
     serializer_class = usersSerializer
