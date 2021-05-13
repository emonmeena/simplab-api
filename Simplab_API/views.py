from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_user(request, userid):
    if request.method == 'GET':
        users = User_Detail.objects.get(user=userid)
        serializedData =  User_Detail_Serializer(users)
        return Response(serializedData.data)        

@api_view(['POST'])
def post_user(request):
    if request.method == 'POST':
        serialized_user = User_Serializer(data=request.data)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response(serialized_user.data['id'])
        return Response(serialized_user.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def auth_user(request, username, password):
    try:
        user = User.objects.get(username=username , password=password)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_detail = User_Detail.objects.get(user=username)
        serializedData =  User_Detail_Serializer(user_detail)
        return Response(serializedData.data)  