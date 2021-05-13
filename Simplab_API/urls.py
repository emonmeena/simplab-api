from django.urls import path
from . import views

urlpatterns = [
    path('users/<userid>', views.get_user, name='get user detail'),
    path('auth/<username>/<password>', views.auth_user, name='authenticate user'),
    path('users/', views.post_user, name='save a user in db'),
    path('simulations/', views.get_simulations, name='get all simulations for library'),
    path('simulation/<exp_id>', views.get_exp_detail, name='get experiment detail of an exp.'),
    path('assignments/', views.post_assignment, name='post an assignment'),
]
