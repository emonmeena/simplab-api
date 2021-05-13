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
            serialized_user_detail = User_Detail_Serializer(data={"user": serialized_user.data['id'], "username": serialized_user.data['username']})
            if serialized_user_detail.is_valid():
                serialized_user_detail.save()
            return Response(serialized_user.data['id'])
        return Response(serialized_user.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def auth_user(request, username, password):
    try:
        user = User.objects.get(username=username , password=password)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_detail = User_Detail.objects.get(user=user.id)
        serializedData =  User_Detail_Serializer(user_detail)
        return Response(serializedData.data)

@api_view(['GET'])
def get_simulations(request):
    if request.method == 'GET':
        simulations = Experiment.objects.all()
        serializedData =  Experimennt_Serializer(simulations,many=True)
        return Response(serializedData.data)


@api_view(['GET'])
def get_exp_detail(request, exp_id):
    try:
        exp = Experiment.objects.get(pk=exp_id)
    except Experiment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializedData =  Experimennt_Serializer(exp)
        return Response(serializedData.data)

@api_view(['POST'])
def post_assignment(request):
    if request.method == 'POST':
        serialized_assignment = Assignment_Serializer(data=request.data)
        if serialized_assignment.is_valid():
            serialized_assignment.save()
            return Response(status=status.status.HTTP_201_CREATED)
        return Response(serialized_assignment.errors, status=status.HTTP_400_BAD_REQUEST)        