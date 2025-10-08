from django.db import models
from authentication.models import CustomUser

class Command(models.Model):
    name_comand = models.CharField(max_length=100)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="owner_comand")
    team = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="team_comand")
    def __str__(self):
        return self.name_comand
