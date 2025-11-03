from django.db import models
from authentication.models import CustomUser
from comands.models import Command

class Project(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="projects")
    commands = models.ManyToManyField(Command,related_name="projects")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name