from django.contrib.auth.models import AbstractUser
from django.db import models


class Rank(models.Model):
    title = models.CharField(max_length=64)
    abbreviated_title = models.CharField(max_length=8)
    clearance = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class User(AbstractUser):
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE, blank=True, null=True)
    badge_number = models.IntegerField(unique=True, blank=True, null=True)

    def __str__(self):
        return f"({self.badge_number}) {self.rank.abbreviated_title} {self.last_name}"
