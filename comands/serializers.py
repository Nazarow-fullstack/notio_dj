from rest_framework.serializers import ModelSerializer
from .models import Command


class CommandSerializer(ModelSerializer):
    class Meta:
        model = Command
        fields = ['id', 'name_comand','owner', 'team']
        read_only_fields = ['id', 'owner']