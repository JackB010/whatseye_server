# Generated by Django 5.0 on 2025-05-03 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("control", "0007_day_remove_schedule_days_of_week_schedule_days"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="schedule",
            name="days",
        ),
        migrations.DeleteModel(
            name="Day",
        ),
    ]
