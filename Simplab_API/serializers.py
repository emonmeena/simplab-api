from rest_framework import serializers
from .models import *

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id', 'username', 'email', 'password']

class Team_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields='__all__'

class Team_Serializer_Basic(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields=['id', 'team_name', 'admin']

class Experimennt_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields='__all__'

class Assignment_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields='__all__'

class Ass_Submission_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields='__all__'

class Chat_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields='__all__'

class Chat_File_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields=['chat_file', 'date', 'sender', 'id']

class User_Detail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Detail
        fields='__all__'        

class User_Detail_Serializer_Basic(serializers.ModelSerializer):
    class Meta:
        model = User_Detail
        fields=['username', 'profile_image', 'email']      