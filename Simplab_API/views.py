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

@api_view(['POST', 'GET'])
def post_user(request):
    if request.method == 'GET':
        users = User_Detail.objects.all()
        serializedData =  User_Detail_Serializer(users, many=True)
        return Response(serializedData.data)
        
    if request.method == 'POST':
        serialized_user = User_Serializer(data=request.data)
        if serialized_user.is_valid():
            serialized_user.save()
            serialized_user_detail = User_Detail_Serializer(data={"user": serialized_user.data['id'], "username": serialized_user.data['username'], "email": serialized_user.data["email"]})
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
            return Response(status=status.HTTP_201_CREATED)
        return Response(serialized_assignment.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
def post_team(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        serializedData =  Team_Serializer(teams, many=True)
        return Response(serializedData.data)

    if request.method == 'POST':
        serialized_team = Team_Serializer(data=request.data)
        if serialized_team.is_valid():
            serialized_team.save()
            return Response(serialized_team.data['id'])
        return Response(serialized_team.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def join_team(request, team_id, user_id):
    try:
        team = Team.objects.get(pk=team_id)
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
            
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    

    if request.method == 'PUT':
        team.students.add(user)
        team.save()
        return Response(st)

@api_view(['GET'])
def get_team_detail(request, team_id):
    if request.method == 'GET':
        team = Team.objects.get(pk=team_id)
        serializedData =  Team_Serializer(team)
        return Response(serializedData.data)

@api_view(['GET'])
def get_user_teams(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        teams = user.all_member_teams.all()
        serializedData =  Team_Serializer_Basic(teams, many=True)
        return Response(serializedData.data)

@api_view(['GET'])
def get_user_admin_teams(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        teams = user.team_set.all()
        serializedData =  Team_Serializer_Basic(teams, many=True)
        return Response(serializedData.data)

@api_view(['GET'])
def get_student_list(request, team_id):
    try:
        team = Team.objects.get(pk=team_id)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        students = team.team_members.all()
        serializedData =  User_Detail_Serializer_Basic(students, many=True)
        return Response(serializedData.data)        

@api_view(['GET'])
def get_all_team_assignments(request, team_id):
    try:
        team = Team.objects.get(pk=team_id)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        assignments = team.all_team_experiments.all()
        serializedData =  Assignment_Serializer(assignments, many=True)
        return Response(serializedData.data)


@api_view(['PUT'])
def put_user_detail(request, user_id):
    try:
        user_detail = User_Detail.objects.get(user=user_id)
    except User_Detail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)     

    if request.method == 'PUT':
        serialized_user_detail = User_Detail_Serializer(user_detail)
        if serialized_user_detail.is_valid():
            serialized_user_detail.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_password(request, user_id):
    try:
        user = User_Detail.objects.get(user=user_id)
    except User_Detail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)     

    if request.method == 'PUT':
        serialized_user = User_Serializer(data=request.data)
        if serialized_user.is_valid():
            serialized_user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_all_assignments(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        teams = user.all_member_teams.all()
        array = []
        for x in teams:
            s = Assignment_Serializer(x.all_team_experiments.all(), many=True)
            if s.data != []:
                array.append(s.data)
        print(array)    
        return Response(array)