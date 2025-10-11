from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Project
from .serializers import ProjectSerializer, CreateUpdateProjectSerializer

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
        return Project.objects.filter(command__owner=user)

    def perform_create(self, serializer):
        command = serializer.validated_data.get('command')
        if command and command.owner != self.request.user:
            raise PermissionDenied("You can only create projects in your own commands.")
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        project = self.get_object()
        if project.owner != self.request.user:
            raise PermissionDenied("You can only edit your own projects.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied("You can only delete your own projects.")
        instance.delete()