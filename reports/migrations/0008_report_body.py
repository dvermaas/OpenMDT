# Generated by Django 5.0.6 on 2024-06-14 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0007_alter_report_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="body",
            field=models.TextField(default="", max_length=2048),
            preserve_default=False,
        ),
    ]