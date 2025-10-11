# models.py

from django.db import models
from authentication.models import CustomUser

class Command(models.Model):
    name_comand = models.CharField(max_length=100)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="owned_commands") 

    def __str__(self):
        return self.name_comand
    

class TeamMember(models.Model):

    command = models.ForeignKey(Command, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="team_memberships")
    date_joined = models.DateTimeField(auto_now_add=True)
    class Meta:

        unique_together = ('command', 'user')

    def __str__(self):
        return f"{self.user.username} in {self.command.name_comand}"