from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Legislation(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=1024)
    time = models.IntegerField(default=0)
    fine = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    type = models.CharField(
        max_length=32,
        choices=[
            ("info", "Misdemeanor"),
            ("warning", "Felony"),
            ("danger", "Critical"),
        ],
        default="info",
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.title
