from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([User, Team, Experiment, Assignment, AssignmentSubmission, Chat, User_Detail])