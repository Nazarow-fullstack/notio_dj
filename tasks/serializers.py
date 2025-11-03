from rest_framework import serializers
from .models import Task
from comands.models import Command 
from projects.models import Project

class SimpleCommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = ['id', 'name_comand', 'owner'] 

class SimpleProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'owner']

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.StringRelatedField()
    command = SimpleCommandSerializer(read_only=True) 
    project = SimpleProjectSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'deadline', 'status', 'project', 'command', 'assigned_to', 'created_at']

class CreateUpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'status', 'project', 'command', 'assigned_to']

    def validate(self, data):
        project = data.get('project')
        command = data.get('command')

        if project and command:
            if command not in project.commands.all():
                raise serializers.ValidationError({
                    'command': 'This command is not part of the selected project.'
                })
        return data