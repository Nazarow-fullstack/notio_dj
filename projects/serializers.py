from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    command = serializers.StringRelatedField()
    
    class Meta:
        model = Project
        fields = ['id', 'name', 'owner', 'command', 'created_at']

class CreateUpdateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'command']