from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.db.models import Q
from .models import Task
from .serializers import TaskSerializer, CreateUpdateTaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CreateUpdateTaskSerializer
        return TaskSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Task.objects.none()
        
        return Task.objects.filter(
            Q(command__owner=user) | Q(assigned_to=user)
        ).distinct()

    def perform_create(self, serializer):
        command = serializer.validated_data.get('command')
        if command and command.owner != self.request.user:
            raise PermissionDenied("You are not the owner of this command and cannot create tasks.")
        serializer.save()

    def perform_update(self, serializer):
        task = self.get_object()
        if task.command.owner != self.request.user:
            raise PermissionDenied("Only the command owner can update this task.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.command.owner != self.request.user:
            raise PermissionDenied("Only the command owner can delete this task.")
        instance.delete()