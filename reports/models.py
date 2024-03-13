from django.contrib.auth.models import User
from django.db import models


class Report(models.Model):
    #label =
    #status =
    title = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_by = kwargs.pop("user", None)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
