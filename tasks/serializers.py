from rest_framework import serializers
from .models import Task
from comands.models import Command 

class SimpleCommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = ['id', 'name_comand', 'owner'] 

class TaskSerializer(serializers.ModelSerializer):
    
    assigned_to = serializers.StringRelatedField()
    command = SimpleCommandSerializer(read_only=True) 

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'deadline', 'status', 'command', 'assigned_to', 'created_at']

class CreateUpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'status', 'command', 'assigned_to']