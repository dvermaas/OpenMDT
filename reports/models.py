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


class Charge(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=1024)

    def __str__(self):
        return self.title


class ReportSuspect(models.Model):
    suspect = models.CharField(max_length=256)
    charges = models.ManyToManyField(Charge)

    def __str__(self):
        return self.suspect


class Report(models.Model):
    title = models.CharField(max_length=256)
    # suspect = models.OneToOneField(
    #     "profiles.Profile", on_delete=models.CASCADE, blank=False, null=False
    # )
    tags = models.ManyToManyField(Tag)
    suspects = models.ManyToManyField(ReportSuspect)

    is_warrant = models.BooleanField(default=False)
    is_processed = models.BooleanField(default=False)
    is_plead_guilty = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
