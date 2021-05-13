from rest_framework import serializers
from .models import *

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'

class Team_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields='__all__'

class Experimennt_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields='__all__'

class Assignment_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment_Assignment
        fields='__all__'

class Submission_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields='__all__'

class Chat_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields='__all__'

class User_Detail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Detail
        fields='__all__'        

class Team_Name_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['team_name']       