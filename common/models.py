from django.db import models

from accounts.models import User


class Tag(models.Model):
    title = models.CharField(max_length=256)
    icon = models.CharField(max_length=32, default="circle-fill")

    def __str__(self):
        return self.title


class Notification(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField(max_length=1024)
    type = models.CharField(
        max_length=32,
        choices=[("info", "Info"), ("warning", "Warning"), ("danger", "Error")],
        default="info",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Announcement(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    body = models.TextField(max_length=2048)

    def __str__(self):
        return self.title
