from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Command
from .serializers import CommandSerializer

class CommandViewSet(viewsets.ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
    permission_classes = [permissions.IsAuthenticated]
