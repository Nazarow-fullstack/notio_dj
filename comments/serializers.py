from rest_framework.serializers import ModelSerializer
from .models import Comment

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'task', 'created_at']
        read_only_fields = ['id', 'author','task', 'created_at']