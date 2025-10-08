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
    user_responsible = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comand = models.ForeignKey(Command, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=CHOISES_STATUS, default='new')

    def __str__(self):
        return self.title
