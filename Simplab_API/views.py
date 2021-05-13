from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def list_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializedData =  User_Serializer(users, many=True)
        return Response(serializedData.data)