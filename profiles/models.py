from django.db import models
from simple_history.models import HistoricalRecords

from common.models import Tag


class Profile(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    body = models.TextField(max_length=2048, blank=True)
    birthday = models.DateField()
    picture = models.ImageField(upload_to="profiles/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)

    history = HistoricalRecords()

    @property
    def get_picture(self):
        default = "https://www.elevenforum.com/proxy.php?image=https%3A%2F%2Fi.hizliresim.com%2Fqde7y7b.png&hash=8840a7826b2be91b53ca4f36d7726152"
        return self.picture.url if self.picture else default

    def __str__(self):
        return f"{self.name} {self.surname}"
