from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Project
from .serializers import ProjectSerializer, CreateUpdateProjectSerializer
from comands.models import Command

class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CreateUpdateProjectSerializer
        return ProjectSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Project.objects.none()
        return Project.objects.filter(commands__owner=user).distinct()

    def perform_create(self, serializer):
        commands = serializer.validated_data.get('commands')
        if commands:
            for command in commands:
                if command.owner != self.request.user:
                    raise PermissionDenied("You can only create projects in your own commands.")
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        project = self.get_object()
        if project.owner != self.request.user:
            raise PermissionDenied("You can only edit your own projects.")
        
        if 'commands' in serializer.validated_data:
            new_commands = serializer.validated_data['commands']
            for command in new_commands:
                if command.owner != self.request.user:
                    raise PermissionDenied("You can only add your own commands to a project.")
        
        serializer.save()

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied("You can only delete your own projects.")
        instance.delete()