# Generated by Django 5.1.2 on 2024-10-19 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="picture",
            field=models.ImageField(blank=True, upload_to="profiles/"),
        ),
    ]
