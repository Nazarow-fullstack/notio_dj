from django.urls import path
from .views import CommandListCreateView, AddMemberView, UserListView

urlpatterns = [
    path('commands/', CommandListCreateView.as_view(), name='command-list-create'),
    path('commands/add-member/', AddMemberView.as_view(), name='add-member'),
    path('users/', UserListView.as_view(), name='user-list'),
]