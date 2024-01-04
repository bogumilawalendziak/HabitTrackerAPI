from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUser(AbstractUser):
    objects = UserManager()

    def __str__(self):
        return self.username


class Habit(models.Model):
    name = models.TextField()
    description = models.TextField()
    status = models.BooleanField()
    start_date = models.TextField()
    is_active = models.BooleanField()
    is_completed = models.BooleanField()
    target_days = models.PositiveIntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
