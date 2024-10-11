# Generated by Django 5.0.7 on 2024-10-10 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Teacher", "0005_remove_lunchmenu_timetable_alter_timetable_class_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attendance",
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
                ("date", models.DateField()),
                ("is_present", models.BooleanField(default=False)),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Teacher.teacher",
                    ),
                ),
            ],
        ),
    ]
