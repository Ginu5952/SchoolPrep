# Generated by Django 5.0.7 on 2024-10-12 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Teacher", "0010_alter_attendance_unique_together"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="announcement",
            name="teacher",
        ),
    ]
