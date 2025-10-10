from django.db import models
from authentication.models import CustomUser
from comands.models import Command


class Task(models.Model):
    CHOISES_STATUS = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('overdue', 'Overdue'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=20, choices=CHOISES_STATUS, default='new')

    command = models.ForeignKey(Command, on_delete=models.CASCADE, related_name="tasks")
    
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
