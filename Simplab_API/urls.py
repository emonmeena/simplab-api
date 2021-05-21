from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('users/<userid>', views.get_user, name='get user detail'),
    path('auth/change-password/<user_id>/<password>', views.update_password, name='modify user password'),
    path('auth/<username>/<password>', views.auth_user, name='authenticate user'),
    path('users/', views.post_user, name='save a user in db'),
    path('edit/user-detail/<user_id>', views.put_user_detail, name='put request to modify userdetail'),
    path('create-team/', views.post_team, name='create a new team'),
    path('teams/<user_id>', views.get_user_teams, name='show all teams with user_id'),
    path('admin-teams/<user_id>', views.get_user_admin_teams, name='show all teams with user_id'),
    path('students/<team_id>', views.get_student_list, name='show all students with team_id'),
    path('join-team/<team_id>/<user_id>', views.join_team, name='join a team'),
    path('team-detail/<team_id>', views.get_team_detail, name='get team detail'),
    path('simulations/', views.get_simulations, name='get all simulations for library'),
    path('simulation/<exp_id>', views.get_exp_detail, name='get experiment detail of an exp.'),
    path('assignments/', views.post_assignment, name='post an assignment'),
    path('assignments/<team_id>', views.get_all_team_assignments, name='get all the assignments of a team'),
    path('all-assignments/<user_id>', views.get_all_assignments, name='get all assignments of all teams'),
    path('chat/<teamid>', views.getchat , name =' get chat of a team'),
    path('delete-team/<teamid>', views.delete_team, name = 'delete team'),
    path('leave-team/<teamid>/<userid>',views.leave_team, name = 'leave team'),
    path('post-chat/', views.post_chat, name = 'add new message in chat'),
    #path('delete-submission/<sid>', views.delete_submission, name = 'delete a submission'),
    path('add-member/<teamid>/<user_email>',views.add_member, name = 'add member to a team'),
    path('edit/assignment-detail/<assignment_id>',views.put_assignment_detail,name = 'put request to modify assignment detail'),
    path('create_assignment/',views.create_assignment,name='create more assignment'),
    path('submissions-list/<assignment_id>',views.submission_list, name= 'get submission list of a assignment'),
    path('submit-assignment/',views.post_submission, name= 'post assignment submission'),
    path('leave-member/<teamid>/<user_name>',views.leave_member, name = 'leave member'),
    path('get-assignment-detail/<assignment_id>',views.get_assignment_detail,name = 'get details of a assignment'),
    path('files/<teamid>',views.get_chat_files, name = 'get chat files'),
    path('post-assignment-submission/',views.post_assignment_submission, name = 'post assignment submission'),
]
