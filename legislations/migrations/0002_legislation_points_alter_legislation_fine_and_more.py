# Generated by Django 5.1.5 on 2025-02-24 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='legislation',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='legislation',
            name='fine',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='legislation',
            name='time',
            field=models.IntegerField(default=0),
        ),
    ]
