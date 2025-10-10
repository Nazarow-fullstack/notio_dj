from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Command, TeamMember
from authentication.models import CustomUser
from .serializers import CommandSerializer, AddMemberSerializer, UserSerializer
from django.db import IntegrityError
from drf_yasg.utils import swagger_auto_schema

class CommandListCreateView(generics.ListCreateAPIView):
    serializer_class = CommandSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Command.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AddMemberView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddMemberSerializer 

    @swagger_auto_schema(request_body=AddMemberSerializer)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        command_id = serializer.validated_data['command_id']
        user_id = serializer.validated_data['user_id']
        
        command = Command.objects.get(pk=command_id)
        user_to_add = CustomUser.objects.get(pk=user_id)
        
        if command.owner != request.user:
            return Response(
                {'error': 'You are not the owner of this command and cannot add members.'},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            TeamMember.objects.create(command=command, user=user_to_add)
        except IntegrityError:
            return Response({'message': 'User is already a member of this command.'}, status=status.HTTP_200_OK)
        
        return Response({'message': f'{user_to_add.username} was added to the command.'}, status=status.HTTP_201_CREATED)
    

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]