from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    CHOISES = (
        ('admin', 'Admin'),
        ('member', 'Member'),
    )
    role = models.CharField(max_length=10, choices=CHOISES, default='member')