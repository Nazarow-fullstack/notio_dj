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
            Q(project__owner=user) | Q(assigned_to=user)
        ).select_related('project', 'command', 'assigned_to').distinct()

    def perform_create(self, serializer):
        project = serializer.validated_data.get('project')
        if project and project.owner != self.request.user:
            raise PermissionDenied("You can only create tasks in your own projects.")
        serializer.save()

    def perform_update(self, serializer):
        task = self.get_object()
        if task.project.owner != self.request.user:
            raise PermissionDenied("You can only edit tasks in your own projects.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.project.owner != self.request.user:
            raise PermissionDenied("You can only delete tasks in your own projects.")
        instance.delete()