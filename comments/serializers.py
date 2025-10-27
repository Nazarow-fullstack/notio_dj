from rest_framework import serializers
from .models import Comment
from tasks.serializers import TaskSerializer
from authentication.models import CustomUser 


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username']

class CommentSerializer(serializers.ModelSerializer):
    task = TaskSerializer(read_only=True)
    author = SimpleUserSerializer(read_only=True) 

    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'task', 'created_at']

class CreateUpdateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'task']