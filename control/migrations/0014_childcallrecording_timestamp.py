# Generated by Django 5.0 on 2025-05-15 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("control", "0013_rename_audio_file_childcallrecording_record_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="childcallrecording",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2025, 5, 1, 0, 59, 17, 416000, tzinfo=datetime.timezone.utc
                ),
                help_text="Device timestamp of the call",
            ),
            preserve_default=False,
        ),
    ]
