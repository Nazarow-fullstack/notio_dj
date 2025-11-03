from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    commands = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Project
        fields = ['id', 'name', 'owner', 'commands', 'created_at']

class CreateUpdateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'commands']