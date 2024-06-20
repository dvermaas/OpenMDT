from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from simple_history.models import HistoricalRecords

from common.models import Tag
from profiles.models import Profile


class Evidence(models.Model):
    title = models.CharField(max_length=256)
    picture = models.ImageField(upload_to="reports/images")

    def __str__(self):
        return self.title


class Charge(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=1024)

    def __str__(self):
        return self.title


class Report(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField(max_length=2048)
    tags = models.ManyToManyField(Tag, blank=True)

    is_warrant = models.BooleanField(default=False)
    is_processed = models.BooleanField(default=False)
    is_plead_guilty = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    history = HistoricalRecords()

    def __str__(self):
        return self.title


class Suspect(models.Model):
    charges = models.ManyToManyField(Charge, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    report = models.ForeignKey(
        Report, on_delete=models.CASCADE, related_name="suspects"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.profile)
