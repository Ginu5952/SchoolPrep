# Generated by Django 5.0.7 on 2024-10-08 15:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Teacher", "0002_timetable_lunchmenu"),
    ]

    operations = [
        migrations.RenameField(
            model_name="lunchmenu",
            old_name="week",
            new_name="week_end_date",
        ),
        migrations.AddField(
            model_name="lunchmenu",
            name="week_start_date",
            field=models.DateField(default=datetime.date(2024, 10, 7)),
            preserve_default=False,
        ),
    ]
