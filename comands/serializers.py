from rest_framework import serializers
from .models import Command, TeamMember
from authentication.models import CustomUser

class TeamMemberSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = TeamMember
        fields = ['username', 'date_joined']

class AddMemberSerializer(serializers.Serializer):
    command_id = serializers.IntegerField()
    user_id = serializers.IntegerField()

    def validate_command_id(self, value):
        if not Command.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Command with this ID does not exist.")
        return value

    def validate_user_id(self, value):
        if not CustomUser.objects.filter(pk=value).exists():
            raise serializers.ValidationError("User with this ID does not exist.")
        return value

class CommandSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    members = TeamMemberSerializer(many=True, read_only=True)

    class Meta:
        model = Command
        fields = ['id', 'name_comand', 'owner', 'members']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username']