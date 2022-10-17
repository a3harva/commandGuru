from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.all_users, name='all_user_details'),
    path('users/<str:user_id>/', views.render_user, name='user_details'),
    path('commands/', views.get_commands, name='all_commands_details'),
    path('commands/<str:user_id>/', views.list_commands, name='command_details'),
    path('commands/delete/<str:command_id>/', views.delete_command, name='delete_command'),
    path('commands/update/<str:command_id>/', views.update_command_page, name='update_command_page'),
    path('commands/add', views.add_command_page, name='add_command_page'),
    path('commands/cmd_update', views.update_command, name='update_command'),
    path('commands/add/cmd_add/', views.add_command, name='add_command'),
]