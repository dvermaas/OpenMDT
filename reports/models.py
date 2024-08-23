from django.contrib.auth.models import User
from django.db import models
from simple_history.models import HistoricalRecords

from common.models import Tag
from legislations.models import Legislation
from profiles.models import Profile


class Evidence(models.Model):
    title = models.CharField(max_length=256)
    picture = models.ImageField(upload_to="reports/images")

    def __str__(self):
        return self.title


class Report(models.Model):
    is_active = models.BooleanField(default=True)
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
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="suspect_appearances"
    )
    report = models.ForeignKey(
        Report, on_delete=models.CASCADE, related_name="suspects"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def time(self):
        return self.charges

    def __str__(self):
        return str(self.profile)


class Charge(models.Model):
    legislation = models.ForeignKey(Legislation, on_delete=models.CASCADE)
    suspect = models.ForeignKey(
        Suspect,
        on_delete=models.CASCADE,
        related_name="charges",
    )

    def __str__(self):
        return str(self.legislation)
