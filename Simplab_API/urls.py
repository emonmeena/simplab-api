from django.urls import path
from . import views

urlpatterns = [
    path('users/<userid>', views.get_user, name='get user detail'),
    path('auth/<username>/<password>', views.auth_user, name='authenticate user'),
    path('users/', views.post_user, name='save a user in db'),
    path('edit/user-detail/<user_id>', views.put_user_detail, name='put request to modify userdetail'),
    path('auth/change-password/<usr_id>', views.update_password, name='modify user password'),
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
]
