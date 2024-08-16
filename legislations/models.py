from django.db import models


class Legislation(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=1024)
    time = models.IntegerField()
    fine = models.IntegerField()
    type = models.CharField(
        max_length=32,
        choices=[
            ("info", "Misdemeanor"),
            ("warning", "Felony"),
            ("danger", "Critical"),
        ],
        default="info",
    )

    def __str__(self):
        return self.title
