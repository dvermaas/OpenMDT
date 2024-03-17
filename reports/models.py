from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Evidence(models.Model):
    title = models.CharField(max_length=256)
    picture = models.ImageField(upload_to="reports/images")

    def __str__(self):
        return self.title


class Report(models.Model):
    title = models.CharField(max_length=256)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
