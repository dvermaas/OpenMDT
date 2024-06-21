from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=256)
    icon = models.CharField(max_length=32, default="circle-fill")

    def __str__(self):
        return self.title
