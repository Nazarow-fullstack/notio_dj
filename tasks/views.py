from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Task
from .serializers import TaskSerializer, CreateUpdateTaskSerializer

class TaskViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        queryset = Task.objects.filter(
            Q(command__owner=user) | Q(assigned_to=user)
        ).distinct()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CreateUpdateTaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        command = serializer.validated_data.get('command')
        if command.owner != request.user:
            raise PermissionDenied("You are not the owner of this command and cannot create tasks.")

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        user = request.user
        task = get_object_or_404(Task, pk=pk)

        is_owner = task.command.owner == user
        is_assignee = task.assigned_to == user
        if not is_owner and not is_assignee:
            raise PermissionDenied("You do not have permission to view this task.")
            
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def update(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        
        if task.command.owner != request.user:
            raise PermissionDenied("Only the command owner can update this task.")
            
        serializer = CreateUpdateTaskSerializer(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        
        if task.command.owner != request.user:
            raise PermissionDenied("Only the command owner can update this task.")
            
        serializer = CreateUpdateTaskSerializer(task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        
        if task.command.owner != request.user:
            raise PermissionDenied("Only the command owner can delete this task.")
            
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)