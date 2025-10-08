from rest_framework.serializers import ModelSerializer
from .models import Task



class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','tittle','user_responsible','comand','created_at','status']
        read_only_fields = ['id', 'created_at']