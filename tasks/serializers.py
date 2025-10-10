from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    
    assigned_to = serializers.StringRelatedField()
    command = serializers.StringRelatedField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'deadline', 'status', 'command', 'assigned_to', 'created_at']

class CreateUpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'status', 'command', 'assigned_to']