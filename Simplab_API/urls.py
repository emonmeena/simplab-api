from django.urls import path
from . import views

urlpatterns = [
    path('users/<userid>', views.get_user, name='get user detail'),
    path('auth/<username>/<password>', views.auth_user, name='authenticate user'),
    path('users/', views.post_user, name='save a user in db'),
    path('create-team/', views.post_team, name='create a new team'),
    path('join-team/', views.join_team, name='join a team'),
    path('team-name/<team_id>', views.get_team_name, name='get team name'),
    path('team-detail/<team_id>', views.get_team_detail, name='get team detail'),
    path('simulations/', views.get_simulations, name='get all simulations for library'),
    path('simulation/<exp_id>', views.get_exp_detail, name='get experiment detail of an exp.'),
    path('assignments/', views.post_assignment, name='post an assignment'),
]
