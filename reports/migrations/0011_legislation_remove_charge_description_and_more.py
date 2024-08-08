# Generated by Django 5.0.7 on 2024-08-03 22:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0010_historicalreport_is_active_report_is_active"),
    ]

    operations = [
        migrations.CreateModel(
            name="Legislation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=256)),
                ("description", models.TextField(max_length=1024)),
            ],
        ),
        migrations.RemoveField(
            model_name="charge",
            name="description",
        ),
        migrations.RemoveField(
            model_name="charge",
            name="title",
        ),
        migrations.RemoveField(
            model_name="suspect",
            name="charges",
        ),
        migrations.AddField(
            model_name="charge",
            name="suspect",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="charges",
                to="reports.suspect",
            ),
        ),
        migrations.AddField(
            model_name="charge",
            name="legislation",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="reports.legislation",
            ),
        ),
    ]
