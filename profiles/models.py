from django.contrib.auth.models import User
from django.db import models
from reports.models import Tag, Charge


class Profile(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    birthday = models.DateField()
    picture = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    charges = models.ManyToManyField(Charge)

    def __str__(self):
        return f"{self.name} {self.surname}"
