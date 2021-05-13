from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_user(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializedData =  User_Serializer(users, many=True)
        return Response(serializedData.data)

@api_view(['POST'])
def post_user(request):
    if request.method == 'POST':
        serialized_user = User_Serializer(data=request.data)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response(serialized_user.data['id'])
        return Response(serialized_user.errors, status=status.HTTP_400_BAD_REQUEST)