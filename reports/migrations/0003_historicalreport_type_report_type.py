# Generated by Django 5.1.3 on 2024-11-23 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_remove_historicalreport_is_plead_guilty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalreport',
            name='type',
            field=models.CharField(choices=[('Default', 'Default'), ('Announcement', 'Announcement')], default='Default', max_length=32),
        ),
        migrations.AddField(
            model_name='report',
            name='type',
            field=models.CharField(choices=[('Default', 'Default'), ('Announcement', 'Announcement')], default='Default', max_length=32),
        ),
    ]
